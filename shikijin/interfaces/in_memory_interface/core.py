from collections.abc import Sequence
from typing import Dict, Optional

from ...fields import BlobId, ComponentName, TaskId
from ...loggers.base import BaseLogger
from ...types import Assignment, BaseCapability, BaseTask, Blob
from ..base import BaseInterface
from ..exceptions import (
    AssignmentNotFoundError,
    BlobNotFoundError,
    NoCapableTaskError,
    TaskNotFoundError,
)


class InMemoryInterface(BaseInterface):
    def __init__(self, logger: BaseLogger, name: Optional[ComponentName]):
        super(InMemoryInterface, self).__init__(logger=logger, name=name)
        self._task_map: Dict[TaskId, BaseTask] = {}
        self._assignment_map: Dict[TaskId, Assignment] = {}
        self._blobs: Dict[BlobId, Blob] = {}

    def abandon_assignment(self, assignment: Assignment) -> None:
        if assignment.task_id not in self._assignment_map:
            self.log_error(f"assignment {assignment} not found")
            raise AssignmentNotFoundError(assignment_id=assignment.id)
        self._assignment_map.pop(assignment.task_id)

    def get_blob(self, blob_id: BlobId) -> Blob:
        if id not in self._blobs:
            self.log_error(f"blob {blob_id} not found")
            raise BlobNotFoundError(blob_id=blob_id)
        return self._blobs[id]

    def save_blob(self, blob: Blob) -> None:
        self._blobs[blob.id] = blob

    def add_task(self, task: BaseTask) -> None:
        self._task_map[task.id] = task

    def get_task(self, task_id: TaskId) -> BaseTask:
        if id not in self._task_map:
            self.log_error(f"task {task_id} not found")
            raise TaskNotFoundError(task_id=task_id)
        return self._task_map[id]

    def pickup_task(self, capabilities: Sequence[BaseCapability]) -> BaseTask:
        for k, v in self._task_map.items():
            if v.is_capable(capabilities):
                if k not in self._assignment_map:
                    return v
        raise NoCapableTaskError(capabilities=capabilities)
