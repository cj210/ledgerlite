from enum import Enum

class RecordType(str, Enum):

    EXPENSE = "expense"
    INCOME = "income"

class UserType(str, Enum):

    INDIVIDUAL = "individual"
    ORGANIZATION = "organization"

class Frequency(str, Enum):
    # ONE_TIME = "one_time"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
