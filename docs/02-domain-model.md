# DOMAIN MODEL

## Purpose

Define the core business entities of LedgerLite and the relationships between them.

This document describes the business domain independently of any database or implementation details.

---

# User

Represents a person or business that owns financial data within LedgerLite.

Each user owns:

- Categories
- Tags
- Goals
- Financial Records

A user cannot access data belonging to another user.

---

# Category

Represents the type of a financial transaction.

Examples:

- Food
- Fuel
- Salary
- Rent
- Entertainment

Categories answer the question:

> "What kind of transaction is this?"

---

# Tag

Represents a past or ongoing event associated with a financial transaction.

Examples:

- Birthday Party
- Vacation 2026
- Diwali
- Wedding
- House Warming

Multiple financial records may share the same tag.

Tags answer the question:

> "What event is this transaction associated with?"

---

# Goal

Represents a future financial objective.

Examples:

- Emergency Fund
- New Car
- House
- Vacation

Goals answer the question:

> "What future objective is this transaction related to?"

A financial record may optionally be associated with a goal.

---

# Financial Record

Represents a historical financial transaction.

A financial record belongs to exactly one user.

It may optionally belong to:

- one category
- one tag
- one goal

A financial record stores:

- transaction type
- amount
- transaction date
- recurrence information
- descriptive information

---

# Record Type

LedgerLite currently supports:

- Expense

Future versions may include:

- Income
- Transfer
- Savings
- Investment

---

# Recurring Transactions

LedgerLite supports two recurring schedules:

- Monthly
- Yearly

Recurring transactions define when a transaction is expected to occur.

Recurring schedule and transaction amount are independent concepts.

Examples:

Monthly Rent

- recurring
- fixed amount

Electricity Bill

- recurring
- variable amount

Income Tax

- yearly recurring
- variable amount

---

# Ownership Model

Every business entity belongs to exactly one user.

Starter categories, tags, and goals are created during user onboarding.

After onboarding there is no distinction between starter data and user-created data.

---

# Business Relationships

```text
User
 ├── Category
 ├── Tag
 ├── Goal
 └── Financial Record

Financial Record
 ├── Category (optional)
 ├── Tag (optional)
 └── Goal (optional)
```
