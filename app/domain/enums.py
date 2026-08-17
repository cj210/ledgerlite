from enum import Enum

class RecordType(str, Enum):

    EXPENSE = "expense"
    INCOME = "income"

class UserType(str, Enum):

    INDIVIDUAL = "individual"
    BUSINESS = "business"

class Frequency(str, Enum):

    MONTHLY = "monthly"
    YEARLY = "yearly"

class Status(str, Enum):

    ACTIVE = "active"
    DEACTIVATED = "deactivated"
