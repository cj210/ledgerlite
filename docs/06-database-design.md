
# DATABASE DESIGN

## Purpose

Define the persistent data model for LedgerLite.

This document describes the database structure, relationships, ownership model, constraints, and business rules that govern how application data is stored.

It serves as the reference for implementing SQLAlchemy models and database migrations.

---

## Scope

This document covers:

- Database tables
- Table relationships
- Foreign keys
- Constraints
- Ownership model
- Delete behavior
- Recurring transaction model

It does not cover:

- API contracts
- Business logic implementation
- SQLAlchemy syntax
- Database migrations

---

## Current Status

The following tables are part of the MVP database design.

- User
- Category
- Tag
- Goal
- FinancialRecord

---

# Ownership Model

Every business entity belongs to exactly one user.

Categories, tags, goals, and financial records are always user-owned.

Starter categories, tags, and goals are copied into each user's account during onboarding. After creation there is no distinction between starter data and user-created data.

---

# User

## Columns

- id
- user_name
- display_name
- password_hash
- user_type
- status
- description
- email
- mobile
- created_at
- updated_at

## Constraints

- user_name must be unique.
- email must be unique when provided.
- mobile must be unique when provided.

## Notes

- user_name is immutable after account creation.
- display_name is used throughout the user interface.
- password_hash is system-owned and is never returned through the API.
- status represents whether an account is active or deactivated.

---

# Category

## Columns

- id
- user_id
- name
- description
- created_at
- updated_at

## Constraints

- UNIQUE(user_id, name)

## Delete Behavior

Deleting a category sets category_id to NULL in related financial records.

---

# Tag

Structure and constraints are identical to Category.

## Constraints

- UNIQUE(user_id, name)

## Delete Behavior

Deleting a tag sets tag_id to NULL in related financial records.

---

# Goal

Structure and constraints are identical to Category.

## Constraints

- UNIQUE(user_id, name)

## Delete Behavior

Deleting a goal sets goal_id to NULL in related financial records.

---

# FinancialRecord

## Columns

- id
- user_id
- record_type
- name
- amount
- transaction_date
- category_id
- description
- frequency
- is_fixed
- due_month
- due_day
- end_date
- tag_id
- goal_id
- recorded_date
- created_at
- updated_at

## Relationships

- user_id → User
- category_id → Category (nullable)
- tag_id → Tag (nullable)
- goal_id → Goal (nullable)

## Recurring Transactions

LedgerLite MVP supports only:

- Monthly recurring transactions
- Yearly recurring transactions

Weekly and custom recurrence rules are intentionally excluded from the MVP.

Recurring fields are:

- frequency
- due_month
- due_day
- end_date
- is_fixed

Examples:

Monthly

- frequency = MONTHLY
- due_month = NULL
- due_day = 15

Yearly

- frequency = YEARLY
- due_month = 8
- due_day = 15

## Notes

Recurring and fixed are independent concepts.

Examples:

- Monthly Rent → recurring, fixed
- Electricity Bill → recurring, variable
- Income Tax → yearly recurring, variable

---

# Delete Behavior

| Parent | Child | Action |
|---------|-------|--------|
| User | Category | Cascade |
| User | Tag | Cascade |
| User | Goal | Cascade |
| User | FinancialRecord | User account is deactivated instead of deleted (MVP design) |
| Category | FinancialRecord | SET NULL |
| Tag | FinancialRecord | SET NULL |
| Goal | FinancialRecord | SET NULL |

---

# Design Principles

- Every business entity belongs to exactly one user.
- Financial records represent historical facts and should not be deleted when classifications are removed.
- Categories, tags, and goals are metadata that may change independently of historical records.
- Recurring schedule and fixed amount are independent business concepts.
- Database constraints enforce data integrity while business rules remain in the service layer.
