from enum import Enum


class Status(Enum):
    CANCELED = "canceled"
    PENDING = "pending"
    COMPLETED = "completed"