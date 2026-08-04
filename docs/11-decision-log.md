# DECISION LOG

## Purpose
To record significant architectural and project decisions, the reasoning behind them, and the alternatives considered.

## Rule: Each decision represents one architectural question. If the answer evolves over time, the existing decision is updated with the reason for the change. A new decision is created only when a new architectural question arises.

## Scope
The scope of the documentation is limited to the decisions made during the project and regarding the project dependencies. Decisions related to machine provisioning and day-to-day project management are out of scope.

## Current Status
Active
Last updated :- 02/08/2026

## Decision 001 
**Date:** 2026-07-31
bootstrap.sh shall be idempotent

### Reason
- Safe to execute repeatedly
- Predictable
- Supports automation
- Future CI/CD

### Alternatives Considered
- Always recreate environment
- Ask user for confirmation

### Status
Accepted

## Decision 002
**Date:** 2026-07-31
SQLite is the database for the MVP.

### Reason
- Simplicity
- Zero infrastructure
- Easy local development
- Future migration plan

### Alternatives Considered
- Mysql
- Postgres Sql

### Status
Accepted

## Decision 003
**Date:** 2026-08-01
Recurring transactions require manual confirmation

### Reason
- Avoid recording transactions that never happened.
- Allow users to modify recurring transaction details before saving the next occurrence.

### Alternatives Considered
- Auto creation of recurring transaction periodically

### Status
Accepted


## Decision 004
**Date:** 2026-08-01
Dashboard data is computed from financial records and never stored separately.

### Reason
- Avoid duplication of data and maintain single source of truth

### Alternatives Considered
- Creating a table specifically for dashboard data

### Status
Accepted


## Decision 005
**Date:** 2026-08-01
Categories are user owned 

### Reason
- Categories are personal organizing tools
- Users should be free to create, modify and delete their own categories independently
- Categories are used for grouping and filtering but not as shared system-wise classifications

### Alternatives Considered
- Having standard categories for all users

### Status
Accepted


## Decision 006
**Date:** 2026-08-01
Financial records store recurrence information.

### Reason
- Avoid redundant RecurringCommitments table
- Keep the model simple

### Alternatives Considered
- Creating a RecurringCommitments table for recurring information

### Status
Accepted


## Decision 007
**Date:** 2026-08-02
One tag per financial record

### Reason
- An expense usually belongs to one event
- Keep the reporting simple

### Alternatives Considered
- Allow multiple tags per financial record

### Status
Accepted


## Decision 008
**Date:** 2026-08-02
Goals defined for future many-to-many relationships
Implementation deffered

### Reason
- Future proof the domain model without adding the current complexity

### Alternatives Considered
- Keep the goals table with one-to-many relationships

### Status
Accepted


## Decision 009
**Date:** 2026-08-02
Feature branches are temporary and deleted after merge.

### Reason
- Small isolated changes
- Clean git history

### Alternatives Considered
- Keeping branches after completing development

### Status
Accepted

## Decision 010
**Date:** 2026-08-02
Documentation-first development

### Reason
- Preserve project vision
- Preserve architectural knowledge.
- Ensure changes made are logical and well reasoned
- Improve onboarding
- Support project stories

### Alternatives Considered
- Minimum documentation

### Status
Accepted

## Decision 011
**Date:** 2026-08-03

API endpoints are organized using dedicated routers

### Reason
- Organize endpoints by responsibility
- Keep `main.py` focused on application composition
- Improve maintainability and scalability
- Provide predictable locations for API endpoints

### Alternatives Considered
- Define all endpoints directly inside `main.py`

### Status
Accepted

## Decision 012
**Date:** 2026-08-03

Application configuration is centralized through a shared Settings object

### Reason
- Establish a single source of truth for configuration
- Avoid scattered configuration values throughout the codebase
- Support different environments without changing application code
- Simplify future configuration management

### Alternatives Considered
- Hardcode configuration values in multiple modules
- Maintain independent configuration variables in each file

### Status
Accepted


## Decision 013
**Date:** 2026-08-03

Database access is performed through a dedicated connection and session layer

### Reason
- Separate connection management from business logic
- Keep database implementation isolated
- Simplify future migration to another database engine
- Improve maintainability and testability

### Alternatives Considered
- Create database connections directly wherever they are required

### Status
Accepted

## Decision 014
**Date:** 2026-08-02

`main.py` is responsible only for application composition and startup

### Reason
- Keep the application entry point simple and readable
- Prevent business logic from accumulating in `main.py`
- Clearly separate application composition from feature implementation
- Simplify onboarding by making the startup flow easy to understand

### Alternatives Considered
- Allow feature implementations and route definitions directly inside `main.py`

### Status
Accepted

---

## Decision 015

### Title
Starter Data Through User Onboarding

### Status
Accepted

### Context
LedgerLite should provide common categories, tags, and goals so new users can start using the application immediately without manual setup.

### Alternatives Considered

#### Option 1 — Shared System-Owned Records
Maintain a set of system-owned categories, tags, and goals that are shared by all users.

**Pros**
- Only one copy of the starter data.
- Easy to update centrally.

**Cons**
- Users cannot safely rename or modify starter records.
- Requires special authorization rules.
- Queries must handle both system-owned and user-owned records.
- Introduces special cases throughout the application.


#### Option 2 — User-Owned Starter Data (Chosen)
During user onboarding, copy a predefined set of starter categories, tags, and goals into the new user's account.

**Pros**
- Every business entity follows the same ownership model.
- Users can freely rename, edit, or delete starter data.
- Authorization becomes straightforward.
- Database queries remain simple and consistent.
- Eliminates special-case logic.

**Cons**
- Stores duplicate starter records for each user.
- Updating the starter template affects only future users.

### Decision

LedgerLite will seed starter categories, tags, and goals during user onboarding. After creation, all business entities are user-owned and treated identically by the application.

### Consequences
- Every business entity belongs to exactly one user.
- Onboarding is responsible for seeding starter data.
- No distinction exists between starter and user-created records after onboarding.
- Simpler authorization, querying, and maintenance.

Business domain constants are represented using domain enums.
