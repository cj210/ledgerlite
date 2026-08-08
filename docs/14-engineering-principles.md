# ENGINEERING PRINCIPLES

## Purpose
To document the engineering philosophy followed throughout LedgerLite. These principles guide technical decisions, ensure consistency across the project, and provide architectural reasoning beyond implementation details.

---

## Principle 001

### Title
Keep It Simple

### Statement
Choose the simplest design that satisfies the current requirements. Introduce complexity only when it provides clear value.

### Why
Simple systems are easier to understand, maintain, test, debug, and evolve.

### Applied In
- Dashboard data is computed instead of stored.
- Removed redundant `is_recurring` flag.
- Avoided introducing a separate `RecurringCommitments` table.
- Deferred future many-to-many goal implementation until required.

---

## Principle 002

### Title
Single Source of Truth

### Statement
A piece of information should exist in one authoritative place whenever possible.

### Why
Duplicated data increases maintenance cost and creates opportunities for inconsistencies.

### Applied In
- Dashboard derives its data from Financial Records.
- Recurring payment calculations use Financial Records instead of duplicate tables.
- Categories are used for organization rather than storing additional business logic.

---

## Principle 003

### Title
Build for Today's Requirements, Design for Tomorrow

### Statement
Implement only the functionality required today while ensuring the design does not block future enhancements.

### Why
Premature implementation increases complexity, but poor design limits future growth.

### Applied In
- Goals designed to support future many-to-many relationships.
- SQLite selected for MVP with a planned migration path to PostgreSQL.
- Documentation prepared before implementation to support project growth.

---

## Principle 004

### Title
Record the Reasoning

### Statement
Document not only what was decided, but why it was decided and what alternatives were considered.

### Why
The reasoning behind a decision is often more valuable than the decision itself.

### Applied In
- Decision Log.
- Alternatives considered for every architectural decision.
- Living decision philosophy for documenting future changes.

---

## Principle 005

### Title
Documentation is Part of Engineering

### Statement
Documentation is a core engineering activity, not a task performed after development.

### Why
Documentation preserves project vision, reduces communication gaps, improves onboarding, and supports long-term maintenance.

### Applied In
- Product Vision.
- Development Environment.
- Decision Log.
- Architecture Journal.
- README.
- Domain documentation.

---

## Principle 006

### Title
Automate Repetitive Work

### Statement
Developer setup and repetitive tasks should be automated whenever practical.

### Why
Automation reduces human error, improves consistency, and saves development time.

### Applied In
- bootstrap.sh
- Idempotent development environment setup.

---

## Principle 007

### Title
Optimize for Maintainability

### Statement
Prefer solutions that future developers can easily understand, modify, and extend.

### Why
Software spends far more time being maintained than being initially written.

### Applied In
- Clear project structure.
- Temporary feature branches.
- Organized documentation.
- Simple database design.

---

## Principle 008

### Title
Software Evolves

### Statement
Expect requirements, architecture, and decisions to change. Design systems that can evolve instead of assuming perfect foresight.

### Why
Successful software adapts to changing requirements without unnecessary rework.

### Applied In
- Living Decision Log.
- Architecture Journal.
- Planned migration from SQLite to PostgreSQL.
- Future roadmap documentation.

---

## Principle 009

### Title
Compose Applications, Don't Accumulate Them

### Statement
Build applications by composing independent modules with well-defined responsibilities instead of continuously expanding a central application file.

### Why
Composing applications keeps the architecture scalable, maintainable, and easy to understand. The application entry point should focus on assembling components rather than implementing business functionality.

### Applied In
- `main.py` acts only as the application composition and startup entry point.
- API endpoints are implemented in dedicated router modules.
- Routers are explicitly registered using `app.include_router()`.
- Features can be added or removed with minimal impact on the application entry point.

---

## Principle 010

### Title
Prefer Uniform Ownership Models

### Statement
Design business entities to follow a single ownership model whenever possible. Avoid introducing special cases such as shared system-owned records when the same outcome can be achieved through initialization or templating.

### Why
A uniform ownership model reduces conditional logic, simplifies authorization and querying, improves maintainability, and makes the system easier to understand and extend.

### Applied In
- Starter categories are copied into each user's account during onboarding.
- Starter tags are copied into each user's account during onboarding.
- Starter goals are copied into each user's account during onboarding.
- All business entities are owned by exactly one user after creation.

---

## Principle 011

### Title

Represent Business Concepts Explicitly

### Statement

Represent stable business domain concepts explicitly rather than relying on free-form primitive values.

### Why

Explicit domain types (such as enums):

- Prevent invalid values from entering the system.
- Make business rules self-documenting.
- Improve type safety and validation.
- Reduce duplicated string comparisons throughout the codebase.
- Establish a single source of truth for business constants.
- Improve readability, maintainability, and IDE support.

### Applied In

- `RecordType`
- `UserType`
- `Frequency`
- Future business-owned constants with a fixed set of valid values.

---

## Principle 012

### Title

Separate Independent Business Concepts

### Statement

Model independent business concepts independently, even when they frequently appear together.

### Why

Combining unrelated concepts into a single field or abstraction makes the model harder to understand and evolve.

Separating concepts improves clarity, validation, and future extensibility.

### Applied In

- Recurring schedule is represented independently of whether the transaction amount is fixed.
- `frequency` describes **when** a transaction occurs.
- `is_fixed` describes **whether the amount changes**.


---

## Principle 013

### Title

Separate Responsibilities, Preserve Contracts

### Statement

Separate independent application responsibilities while maintaining stable contracts between them.

The frontend and backend should be independently evolvable applications. Internal implementation changes should be contained within the respective application whenever possible, while communication between applications should occur through an explicit API contract.

### Why

Separating responsibilities reduces unnecessary dependencies and allows individual parts of the system to evolve without requiring changes throughout the application.

A stable contract provides a clear boundary between frontend and backend while allowing each side to change its internal implementation independently.

The frontend may understand business domain concepts such as transactions, accounts, categories, and users. This represents shared business vocabulary rather than coupling to backend implementation details.

### Applied In

- Frontend and backend are maintained as separate applications.
- Frontend communication with the backend occurs through the API contract.
- Frontend does not depend on backend implementation details.
- Backend implementation changes should not require frontend changes when the API contract remains unchanged.
- Frontend implementation changes should not require backend changes when the API contract remains unchanged.
- Shared business concepts are expressed using consistent domain terminology across the API boundary.
