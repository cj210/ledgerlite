
# ARCHITECTURE JOURNAL

## Purpose
To document the engineering journey, reflect on the day's work, capture key learnings, and plan the next steps.

## Scope
The scope includes all the activities done on a given day and the learning outcomes for the day.

## Current Status
Active

## Date: 02/08/2026

### Summary: 
Continued setting up the engineering foundation for LedgerLite. Established the project documentation structure, created the bootstrap automation script, documented architectural decisions, and standardized repository organization.


### Work Completed
- Created complete docs directory structure
- Initiated all major documents
- Updated Decision log
- Created bootstrap script for environment setup
- Configured python virtual environment


### Questions Explored
1. What belongs in the machine layer versus the project layer?
Software common for development in general belongs to machine layer and specific to project belongs to project layer.


### Decisions made
- Decision 008 finalized
- Decision 009 finalized
- Decision 010 finalized


### Lessons learned
The following principles emerged from today's work and will guide future development:
1. Separate machine-level setup from project-level setup.
The machine provides the foundation; the project is responsible only for its own dependencies.
2. Development automation should be idempotent.
Running the same setup script multiple times should always produce the same development environment.
3. Documentation is an engineering tool, not just project paperwork.
Good documentation preserves product vision, architectural reasoning, and reduces future communication gaps.
4. Engineering decisions should record the reasoning, not just the outcome.
Capturing alternatives considered is as valuable as recording the accepted solution.
5. Simplicity should be preserved unless complexity provides clear value.
Avoid introducing new tables, flags, or abstractions when the existing design already satisfies the requirements.

### Challenges faced
1. Bash scripting - Lost touch, had to put efforts to finish bootstrap.sh
2. Time management - Couldn't finish daily task and had to extend to next day
3. Git approach - Adopted a Git workflow different from the one used at work. Initially unfamiliar, but understood the reasoning by the end of the day.

### Biggest Insight
Good engineering is not only about writing code; it is about creating a process that keeps the project understandable, maintainable, and easy to evolve.

### Next steps
1. Finalize the remaining project documentation.
2. Begin documenting the domain model in detail.
3. Design the database schema from the finalized domain model.
4. Initialize the FastAPI application structure.
5. Start implementing the first working backend components.

## Date: 03/08/2026

### Summary

Continued building the backend foundation of LedgerLite by transforming the project from a simple FastAPI application into a modular backend architecture. Established centralized configuration, created the reusable database connection layer, and introduced router-based endpoint organization.

### Work Completed
- Created the application package structure organized by responsibility.
- Built the first FastAPI application entry point.
- Implemented centralized configuration using BaseSettings.
- Created reusable SQLite connection and session layers.
- Implemented the first router (health.py).
- Registered routers using app.include_router().
- Verified the application through / and /health endpoints.

### Questions Raised
1. How does main.py discover routes defined in other modules?
2. Why separate routing, configuration, and database responsibilities instead of placing everything in main.py?
3. Should health endpoints verify only application availability or external dependencies like the database?

### Decisions Made
- Decision 011 finalized
- Decision 012 finalized
- Decision 013 finalized
- Decision 014 finalized

### Lessons Learned
1. Python modules export objects, functions, and classes. Importing a router is no different from importing the settings object.
2. main.py should compose the application rather than implement individual features.
3. Routers own endpoint implementations, while the application is only responsible for registering them.
4. Centralizing configuration allows the same application code to run in different environments without modification.
5. Separating connection management from business logic reduces coupling and simplifies future database migrations.
6. A modular architecture keeps growth predictable; adding a new feature becomes creating a new router and registering it.

### Challenges Faced
1. Understanding how routers defined in separate modules become part of the FastAPI application.
2. Distinguishing between Python imports and FastAPI route registration.
3. Recognizing that architectural boundaries are about responsibilities rather than simply splitting files.

### Biggest Insight
Applications are assembled by composing independent modules that explicitly expose responsibilities.

### Next Steps
1. Continue expanding the backend foundation following the established architecture.
2. Begin defining the first domain models.
3. Design the initial database schema.
4. Introduce API modules for business functionality beyond health checks.

---

## Date

2026-08-04

## Summary

Today's work focused on completing the API contract layer for LedgerLite. The objective was not to build persistence, but to establish clear boundaries between the HTTP layer, domain models, and future business logic.

---

## Completed

- Completed `User` API router.
  - `POST /users`
  - `GET /user`

- Completed `FinancialRecord` API router.
  - `POST /financial_records`
  - `GET /financial_records/{record_id}`

- Validated request and response schemas using FastAPI and Pydantic.

- Tested all endpoints using `curl` and FastAPI Swagger UI (`/docs`).

---

## Architectural Decisions

### API Contracts Before Persistence

The API contract should be designed and validated before introducing a database or ORM.

This allowed the request and response models to evolve independently of persistence concerns.

---

### Routers Only Handle HTTP

Routers are responsible for:

- Receiving HTTP requests.
- Validating request data.
- Routing requests to the appropriate service.
- Returning HTTP responses.

Routers are **not** responsible for:

- Business rules.
- Database operations.
- Password hashing.
- Validation requiring business knowledge.
- Authorization logic.

---

### Response Models Represent System-Owned Data

Separate request and response schemas remain justified because they represent different ownership.

Client-owned data:

- username
- display_name
- amount
- transaction_date
- description

System-owned data:

- id
- user_id
- created_at
- updated_at

The API contract should expose only the fields appropriate for each request type.

---

### REST Resource Design

Single resources are addressed using identifiers in the URL.

Examples:

- `GET /financial_records/{record_id}`
- `POST /financial_records`

The collection endpoint represents the resource collection, while the identifier represents an individual resource.

---

## Lessons Learned

- FastAPI automatically converts incoming JSON into strongly typed Pydantic objects before calling the route function.
- `response_model` is not only documentation; it validates and serializes responses before they are returned.
- Path parameters become typed Python objects in the route function.
- Swagger UI (`/docs`) provides an interactive client generated directly from the API contract.

---

## Reflection

The focus shifted away from learning FastAPI syntax and toward understanding backend architecture.

The important realization today was that frameworks are implementation tools, while the architecture defines responsibilities and boundaries.

The API layer now provides a stable contract that future service and persistence layers can build upon without changing the external behavior of the application.

---

## Next Session

- Review and finalize the database design.
- Validate tables, relationships, constraints, and ownership.
- Introduce SQLAlchemy models as the persistence representation of the already-defined business domain.


## Date

2026-08-05

## Summary

Today's work completed the database design phase of LedgerLite.

The focus was on validating the business model rather than writing code. Several design decisions were revisited and refined to improve consistency, preserve historical financial data, and simplify the MVP without sacrificing future extensibility.

The backend architecture for Week 1 is now considered complete.

---

## Completed

- Finalized the `User` business model.
- Finalized the `Category`, `Tag`, and `Goal` relationships.
- Completed the `FinancialRecord` database design.
- Completed `06-database-design.md`.
- Reviewed documentation structure across the project.
- Planned the Week 2 implementation roadmap.

---

## Architectural Decisions

### User Deactivation Instead of Deletion

Users will be deactivated rather than permanently deleted.

This preserves historical financial records, maintains ownership relationships, and simplifies future reporting and auditing.

---

### Simplified Recurring Transaction Model

LedgerLite MVP will support only:

- Monthly recurrence
- Yearly recurrence

Weekly and custom recurrence patterns are intentionally postponed until after the MVP.

---

### Separate Business Concepts

Recurring schedule and fixed transaction amount represent different business concepts.

Recurring answers:

> "When does this transaction occur?"

Fixed answers:

> "Does the amount remain constant?"

These concepts are modeled independently.

---

### Nullable Classifications

Financial records may exist without:

- Category
- Tag
- Goal

Deleting these classifications will not remove historical financial records.

Instead, the related reference becomes `NULL`.

---

## Documentation

The documentation structure became clearer during today's discussion.

Each document now has a distinct responsibility.

Examples:

- Domain Model → Business concepts.
- Database Design → Persistence design.
- Decision Log → Why architectural decisions were made.
- Engineering Principles → Reusable design principles.
- Roadmap → Development milestones.

This separation prevents duplication and keeps documentation easier to maintain.

---

## Lessons Learned

- Domain models describe business concepts rather than database tables.
- Database design documents should describe persistence, not architectural reasoning.
- Decision logs should capture *why* a design changed rather than implementation details.
- Engineering principles should describe reusable patterns rather than project-specific decisions.

---

## Reflection

Today marked the completion of the design phase.

At this point, the project has:

- A defined business domain.
- Stable API contracts.
- A documented database design.
- Architectural principles.
- Recorded design decisions.

The next stage is no longer about deciding how LedgerLite should work.

It is about implementing the architecture that has already been designed.

---

## Next Session

- Begin Week 2.
- Translate the database design into SQLAlchemy models.
- Introduce the persistence layer.
- Understand how SQLAlchemy represents the domain model without changing the architecture.

---

## Date

2026-08-06

## Summary

Today's work shifted from database design into understanding the persistence layer before writing any SQLAlchemy code.

Rather than immediately learning SQLAlchemy syntax, the focus was on building a conceptual understanding of how an Object Relational Mapper (ORM) bridges object-oriented programming and relational databases.

By the end of the session, the responsibilities of Pydantic, FastAPI, SQLAlchemy, and the database were clearly separated.

---

## Completed

- Reviewed the role of SQLAlchemy within the application architecture.
- Distinguished Pydantic schemas from SQLAlchemy models.
- Established the mapping between object-oriented concepts and relational database concepts.
- Understood the purpose of metadata in SQLAlchemy.
- Explored why ORM relationships exist in addition to database foreign keys.
- Prepared the conceptual foundation for implementing SQLAlchemy models.

---

## Architectural Understanding

### Separation of Responsibilities

The backend architecture consists of independent layers, each with a single responsibility.

- FastAPI receives and routes HTTP requests.
- Pydantic validates and serializes API data.
- SQLAlchemy represents the persistence model.
- The database stores and enforces relational data.

Each layer remains independent and communicates through clearly defined contracts.

---

### SQLAlchemy Models Represent Persistence

A SQLAlchemy model is a Python class enriched with database metadata.

The model serves two purposes simultaneously:

- As a normal Python object during application execution.
- As the mapping definition for a relational database table.

This separates persistence concerns from API validation.

---

### Metadata Describes Structure

Metadata does not represent business data.

Instead, it describes how business data should be stored.

Examples include:

- Table names
- Column types
- Maximum lengths
- Nullability
- Uniqueness
- Primary keys
- Foreign keys

The metadata exists even before any business data is stored.

---

### Object Navigation vs Database Relationships

A relational database connects tables using foreign keys.

Object-oriented code connects objects through references.

SQLAlchemy bridges these two representations by allowing object navigation while maintaining relational integrity.

Examples:

Database:

- `financial_records.user_id`

Python:

- `financial_record.user`
- `user.financial_records`

This abstraction allows business logic to operate on objects rather than manually following foreign keys.

---

## Lessons Learned

- ORM stands for Object Relational Mapper because it maps object-oriented concepts to relational database concepts.
- Tables map to classes.
- Rows map to object instances.
- Columns map to object attributes.
- Foreign keys describe relationships in the database.
- SQLAlchemy relationships describe navigation between Python objects.
- Pydantic metadata describes validation rules.
- SQLAlchemy metadata describes persistence rules.

---

## Reflection

A major realization today was that SQLAlchemy introduces very little that is conceptually new.

Most of the ORM is built upon ordinary Python classes with additional metadata describing how those classes should be persisted.

Understanding the concepts before the syntax significantly reduced the apparent complexity of SQLAlchemy.

Instead of viewing the ORM as a framework to memorize, it is now understood as a translation layer between two different representations of the same business domain.

---

## Next Session

- Begin implementing SQLAlchemy models.
- Create the project `Base` class.
- Build the `User` model.
- Introduce `Mapped`, `mapped_column`, and `relationship`.
- Translate the finalized database design into SQLAlchemy models.
---

## Date

2026-08-07

## Summary

Today's work completed the transition from the finalized database design into SQLAlchemy persistence models.

The session began by translating the database specification into Python classes and gradually built an understanding of how SQLAlchemy represents database structure, ownership, relationships, constraints, defaults, and delete behavior.

Rather than treating SQLAlchemy relationships as replacements for database foreign keys, the distinction between **database integrity** and **Python object navigation** was established.

The finalized models were then validated through SQLAlchemy metadata inspection, confirming that the persistence model matches the intended database design.

---

## Completed

* Created a clean project-level SQLAlchemy `Base` class.
* Implemented the `User` SQLAlchemy model.
* Implemented the `Category` SQLAlchemy model.
* Implemented the `Tag` SQLAlchemy model.
* Implemented the `Goal` SQLAlchemy model.
* Implemented the `FinancialRecord` SQLAlchemy model.
* Added typed SQLAlchemy mappings using `Mapped` and `mapped_column`.
* Added database foreign keys for ownership and classification relationships.
* Added bidirectional SQLAlchemy relationships using `relationship` and `back_populates`.
* Added composite uniqueness constraints for user-owned metadata.
* Added database-level delete behavior using `CASCADE` and `SET NULL`.
* Added financial-record validation constraints for `due_month` and `due_on`.
* Added appropriate defaults for dates, timestamps, and `is_fixed`.
* Distinguished `transaction_date` from `recorded_date`.
* Validated the complete SQLAlchemy metadata successfully.

---

## Architectural Understanding

### Base as the Declarative Foundation

A dedicated project `Base` class was retained even though it currently contains no LedgerLite-specific fields.

`Base` now serves as the common declarative foundation for all SQLAlchemy models.

This keeps SQLAlchemy infrastructure centralized without coupling the base class to LedgerLite-specific persistence fields.

---

### Foreign Keys and Relationships Have Different Responsibilities

A foreign key establishes the relational connection at the database level.

For example:

```text
categories.user_id → users.id
```

The SQLAlchemy relationship provides object-level navigation:

```text
category.user
user.categories
```

Therefore, the foreign key is responsible for **database integrity**, while the relationship is responsible for **ORM object navigation**.

Both are useful and serve different purposes.

---

### Bidirectional Relationships

Relationships were implemented in both directions where navigation is useful.

For example:

```text
Category
    user
      ↓
    User

User
    categories
      ↓
    List[Category]
```

`back_populates` explicitly connects the two relationship definitions so SQLAlchemy understands that they represent the two sides of the same relationship.

The same pattern is used for:

* User ↔ Category
* User ↔ Tag
* User ↔ Goal
* User ↔ FinancialRecord
* Category ↔ FinancialRecord
* Tag ↔ FinancialRecord
* Goal ↔ FinancialRecord

---

### User Ownership

Every business entity is explicitly associated with a user through a foreign key.

This makes ownership part of the persistence model rather than something that exists only as an application-level assumption.

The resulting ownership structure is:

```text
User
 ├── Categories
 ├── Tags
 ├── Goals
 └── Financial Records
```

---

### Historical Financial Records

Financial records were deliberately separated from their classification metadata.

A financial record may reference:

* Category
* Tag
* Goal

but those references are nullable.

When classification metadata is deleted, the corresponding reference becomes `NULL` rather than deleting the financial record.

This preserves historical financial facts independently of mutable metadata.

---

### Recurring Transactions

The model represents recurring transactions through separate fields rather than treating recurrence as a single concept.

The relevant fields are:

* `frequency`
* `due_month`
* `due_on`
* `end_date`

`is_fixed` remains independent of recurrence.

This allows combinations such as:

```text
Monthly + Fixed
Monthly + Variable
Yearly + Fixed
Yearly + Variable
```

without coupling the two concepts.

---

### Transaction Date vs Recorded Date

Two different dates were intentionally retained:

* `transaction_date` — the date the financial event actually occurred.
* `recorded_date` — the date the event was entered into LedgerLite.

`recorded_date` defaults to the current date because it represents when LedgerLite received the record.

This distinction allows historical transactions to be entered after the actual event without losing information about when they entered the system.

---

## Validation

A dedicated model-validation script was used to inspect SQLAlchemy metadata before moving further into database implementation.

The validation confirmed:

* All five tables were registered.
* Column types and lengths matched the database design.
* Nullability matched the intended model.
* Primary keys were present.
* Unique constraints were present.
* Foreign keys pointed to the correct tables.
* `CASCADE` and `SET NULL` delete behaviors were present.
* Financial-record check constraints were registered.
* Enum mappings were recognized.
* Defaults and update behavior were registered.

The metadata validation completed successfully.

---

## Lessons Learned

* A SQLAlchemy foreign key and a SQLAlchemy relationship are not interchangeable.
* Foreign keys enforce relational integrity.
* Relationships provide object-level navigation.
* `back_populates` explicitly connects both sides of an ORM relationship.
* A collection relationship represents the "many" side of a one-to-many relationship.
* SQLAlchemy metadata can be inspected before a real database exists.
* Database constraints can be represented directly in SQLAlchemy models.
* Defaults such as `date.today` and `datetime.now` should be passed as callables rather than evaluated during model definition.
* `transaction_date` and `recorded_date` represent different business events and should remain separate.
* A clean declarative `Base` provides a useful project boundary even when it contains no application-specific fields.

---

## Reflection

Today's work was less about writing SQLAlchemy syntax and more about translating an already-established database design into an ORM representation.

The most important architectural distinction was between the **database model** and the **Python object graph**.

The database needs foreign keys and constraints to preserve integrity.

The application needs relationships to navigate those records naturally as Python objects.

SQLAlchemy provides the bridge between these two representations without replacing either one.

The successful metadata validation also established an important workflow for the project: the persistence model can be checked structurally before introducing the database engine, sessions, migrations, or CRUD operations.

This keeps the implementation incremental and makes structural problems easier to identify before they spread into later layers.

---

## Next Session

* Introduce the SQLAlchemy database engine.
* Configure the database connection.
* Introduce session management.
* Decide how database initialization should be handled.
* Prepare the persistence layer for actual database operations.

---

## Date

2026-08-08

## Summary

Today's work completed **Deliverable 6 — Repository Layer** and established the architectural boundary between database persistence and business logic.

The session began by clarifying SQLAlchemy session management and the difference between a `sessionmaker` factory and an actual SQLAlchemy `Session`.

The repository layer was then implemented for all five LedgerLite entities:

* User
* Category
* Goal
* Tag
* FinancialRecord

Rather than treating repositories as generic CRUD wrappers, their responsibilities were designed from the actual LedgerLite ownership model and business requirements.

The most important architectural outcome was establishing that repositories are responsible for **database interaction**, while services will own **business rules and transaction decisions**.

The completed repository layer is now ready to support the service layer.

---

## Completed

* Confirmed `sessionmaker(engine)` creates a session factory.
* Confirmed `SessionLocal()` creates an actual SQLAlchemy `Session`.
* Removed the obsolete database connection approach.
* Established `SessionLocal` as the application's session factory.
* Resolved SQLAlchemy model relationship-registration issues.
* Added model imports required for SQLAlchemy relationship resolution.
* Created the `UserRepository`.
* Created the `CategoryRepository`.
* Created the `GoalRepository`.
* Created the `TagRepository`.
* Created the `FinancialRecordRepository`.
* Implemented user-scoped retrieval.
* Implemented creation operations.
* Implemented physical deletion for applicable entities.
* Implemented financial-record filtering by category.
* Implemented financial-record filtering by goal.
* Implemented financial-record filtering by tag.
* Implemented financial-record filtering by recorded-date range.
* Verified repository queries against the existing SQLite database.
* Confirmed an empty database returns `None` for a missing user rather than failing.

---

## Architectural Understanding

### Session Factory vs Session

The distinction between the SQLAlchemy session factory and an actual session was established.

The application defines:

```python
SessionLocal = sessionmaker(engine)
```

`SessionLocal` is a **factory**, not a database session.

An actual session is created when:

```python
session = SessionLocal()
```

is executed.

The session is then passed into repositories:

```text
SessionLocal()
    ↓
Session
    ↓
Repository
```

This allows repositories to operate on the session without creating or owning the application's session lifecycle themselves.

---

### Repository Responsibility

The repository layer is responsible for **database interaction**.

Repositories may:

* Retrieve model objects.
* Add model objects to the session.
* Mark model objects for deletion.
* Return model objects or collections of model objects.

Repositories do not own business decisions.

The intended boundary is:

```text
Repository
    │
    ├── Query database
    ├── Add objects to session
    └── Mark objects for deletion
```

Repositories do not handle:

```text
Business calculations
Business rules
Application-level decisions
API responses
Transaction boundaries
```

Those responsibilities belong to the service/application layer.

---

### Repository Does Not Commit

A major architectural decision was made that repositories will not call:

```python
session.commit()
```

or:

```python
session.rollback()
```

For example:

```python
def create(self, category):
    self.session.add(category)
    return category
```

and:

```python
def delete(self, category):
    self.session.delete(category)
    return category
```

The repository changes the state of the SQLAlchemy session.

The service layer will decide whether the overall operation should be committed or rolled back.

This becomes particularly important when a single business operation involves multiple repositories.

For example:

```text
Service
   │
   ├── Repository A
   ├── Repository B
   └── Repository C
          │
          ▼
       commit()
```

This allows several database operations to participate in one transaction.

---

## User Repository

The `UserRepository` provides:

```text
get_by_id(user_id)
get_by_user_name(user_name)
create(user)
```

User retrieval is intentionally limited to the application's actual requirements.

There is no physical `delete()` operation for users.

User deletion is a business operation that changes the user's status to `deactivated`.

---

## User Ownership

A major principle established during repository design is that user-owned data must remain explicitly scoped to the user.

For example:

```python
get_by_name(user_id, name)
```

rather than:

```python
get_by_name(name)
```

This is particularly important for:

* Categories
* Goals
* Tags
* Financial Records

The application should never assume that a resource name is globally unique when its uniqueness is actually scoped to a user.

---

## Category, Goal, and Tag Repositories

Category, Goal, and Tag all share the same ownership model.

Each uses:

```text
(user_id, name)
```

as its logical lookup identity because the database defines:

```text
UNIQUE(user_id, name)
```

Therefore their repositories provide:

```text
get_by_name(user_id, name)
create(object)
delete(object)
```

This means two different users can independently have resources with the same name:

```text
User 1 → Category: Food
User 2 → Category: Food
```

while the same user cannot have two categories with the same name.

---

## FinancialRecord Repository

Financial records were treated differently from Category, Goal, and Tag because their `name` is not unique.

A user may have many records with the same name:

```text
Salary
Salary
Salary
```

Therefore, retrieving financial records by name is not an appropriate repository operation.

Instead, FinancialRecord retrieval is primarily filter-based.

The repository currently provides:

```text
get_by_category(user_id, category_id)
get_by_goal(user_id, goal_id)
get_by_tag(user_id, tag_id)
get_by_date_range(user_id, start_date, end_date)
```

All retrieval methods require `user_id`.

This ensures that filtering operations remain within the authenticated user's data boundary.

---

### Foreign Key Columns vs Relationships

While implementing financial-record filtering, the distinction between a relationship and its foreign-key column was reinforced.

For example:

```text
FinancialRecord
    category_id
    category
```

`category_id` is the database foreign-key column.

`category` is the SQLAlchemy relationship object.

Therefore, repository queries use:

```python
FinancialRecord.category_id == category_id
```

rather than treating the relationship itself as the database column.

The same principle applies to:

* `goal_id` / `goal`
* `tag_id` / `tag`

---

### Date Range Filtering

The repository provides a low-level date-range operation:

```text
get_by_date_range(user_id, start_date, end_date)
```

The repository is responsible for executing the database query.

The service layer will determine what a business concept means.

For example:

```text
"This month"
"Last month"
"This financial year"
"Previous quarter"
```

These concepts require business logic to calculate their actual date boundaries.

Therefore:

```text
Service
    "This month"
        ↓
    start_date / end_date
        ↓
Repository
    get_by_date_range(...)
```

This keeps business-period calculations out of the repository.

---

## Creation Operations

All repositories that support creation follow the same pattern:

```python
def create(self, object):
    self.session.add(object)
    return object
```

`session.add()` places the object into the SQLAlchemy session and causes SQLAlchemy to track it.

The repository returns the same object so that the service layer can continue working with it.

The repository does not commit the transaction.

---

## Deletion Policy

The deletion behavior of each entity was clarified.

```text
User
    → Deactivate user

Category
    → Physical deletion

Goal
    → Physical deletion

Tag
    → Physical deletion

FinancialRecord
    → Physical deletion
```

User deletion is therefore a business-state transition rather than a repository-level physical delete.

Categories, goals, tags, and financial records may be physically deleted according to LedgerLite's business requirements.

---

### Returning Deleted Objects

The repository's `delete()` methods return the object that was marked for deletion:

```python
def delete(self, category):
    self.session.delete(category)
    return category
```

Although `session.delete()` itself returns `None`, the original Python object remains available.

Returning it allows the service or API layer to use information such as:

```text
Category 12 deleted
Goal 5 deleted
Tag 8 deleted
Financial record 31 deleted
```

without requiring the repository to construct an API response.

---

## Final Repository Structure

The completed repository layer is:

```text
app/repositories/
├── user.py
├── category.py
├── goal.py
├── tag.py
└── financial_record.py
```

The repository contracts are:

```text
UserRepository
├── get_by_id(user_id)
├── get_by_user_name(user_name)
└── create(user)

CategoryRepository
├── get_by_name(user_id, name)
├── create(category)
└── delete(category)

GoalRepository
├── get_by_name(user_id, name)
├── create(goal)
└── delete(goal)

TagRepository
├── get_by_name(user_id, name)
├── create(tag)
└── delete(tag)

FinancialRecordRepository
├── get_by_category(user_id, category_id)
├── get_by_goal(user_id, goal_id)
├── get_by_tag(user_id, tag_id)
├── get_by_date_range(user_id, start_date, end_date)
├── create(record)
└── delete(financial_record)
```

---

## Layer Responsibility

The architecture now has a clearer persistence boundary:

```text
Request
    ↓
Router
    ↓
Pydantic Schema
    ↓
Service
    ↓
Repository
    ↓
SQLAlchemy Session
    ↓
SQLite
```

The repository layer is now responsible for the part between the service and the database.

The service layer will sit above it and coordinate business operations.

---

## Lessons Learned

* `sessionmaker(engine)` creates a session factory rather than an actual session.
* `SessionLocal()` creates an actual SQLAlchemy session.
* A repository should receive a session rather than create its own database session.
* `session.add()` adds an object to the session and allows SQLAlchemy to track it.
* `session.delete()` marks an object for deletion but does not itself commit the deletion.
* Repository methods should not automatically commit transactions.
* Repository methods should not contain business logic.
* SQLAlchemy query expressions use `==` for comparisons.
* Python `and` should not be used to combine SQLAlchemy query expressions.
* `.first()` returns one object or `None`.
* `.all()` returns a collection of matching records.
* Foreign-key columns should be queried directly when filtering by related IDs.
* User ownership should be explicitly included in user-scoped repository queries.
* Database uniqueness constraints and repository lookup methods should reflect the actual ownership model.
* A resource's database ID does not always need to be the application's primary retrieval mechanism.
* Financial records are better retrieved through meaningful filters than by assuming transaction names are unique.
* Business concepts such as "this month" belong in the service layer rather than the repository.
* Returning a model object from `create()` or `delete()` allows higher layers to use the result without making the repository responsible for API responses.
* Physical deletion and business-level deactivation are different concepts.
* Database `CASCADE` and `SET NULL` behavior defines what happens to related rows when a physical deletion occurs; it does not itself define whether the application should allow that deletion.

---

## Reflection

Today's work marked an important transition from defining **what the database looks like** to defining **how the application interacts with the database**.

The most important lesson was that a repository is not simply a collection of CRUD functions.

Its real purpose is to establish a clean boundary around persistence.

The repository knows:

```text
How to query
How to add
How to delete
How to retrieve
```

The service will know:

```text
Why the operation is allowed
What business rules apply
What other operations must happen
Whether the transaction should succeed
```

This separation prevents database-access code from becoming mixed with business logic.

The design of `FinancialRecordRepository` also demonstrated why repositories should be designed from the application's domain rather than blindly implementing generic CRUD.

A financial record is not naturally retrieved by its name or only by its ID. In LedgerLite, users primarily work with records through categories, goals, tags, and time periods.

The repository therefore exposes those meaningful persistence queries while leaving the interpretation of business concepts to the service layer.

This completed the repository foundation needed for the next layer of the architecture.

---

## Next Session

Begin **Deliverable 7 — Service Layer**.

Focus on:

* Moving business rules out of routers.
* Defining service responsibilities.
* Password hashing.
* Duplicate username handling.
* User deactivation.
* Category business rules.
* Goal and tag business rules.
* Recurring transaction validation.
* Starter data creation during onboarding.
* Transaction coordination across repositories.

The next architectural boundary will be:

```text
Router
    ↓
Service
    ↓
Repository
    ↓
SQLite
```

---

