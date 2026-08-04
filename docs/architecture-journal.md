
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
