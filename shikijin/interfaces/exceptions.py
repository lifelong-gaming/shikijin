from collections.abc import Sequence

from ..exceptions import BaseError
from ..fields import AssignmentId, BlobId, TaskId
from ..types import BaseCapability


class BaseInterfaceError(BaseError):
    pass


class BlobNotFoundError(BaseInterfaceError):
    def __init__(self, blob_id: BlobId):
        super(BlobNotFoundError, self).__init__(f"blob {blob_id} not found")


class TaskNotFoundError(BaseInterfaceError):
    def __init__(self, task_id: TaskId):
        super(TaskNotFoundError, self).__init__(f"task {task_id} not found")


class AssignmentNotFoundError(BaseInterfaceError):
    def __init__(self, assignment_id: AssignmentId):
        super(AssignmentNotFoundError, self).__init__(f"assignment {assignment_id} not found")


class NoCapableTaskError(BaseInterfaceError):
    def __init__(self, capabilities: Sequence[BaseCapability]):
        super(NoCapableTaskError, self).__init__(f"no capable task found for capabilities {capabilities}")
