# PROJECT STRUCTURE

## Purpose

Define the architectural organization of the LedgerLite backend.

Each package has a single responsibility and should not overlap with another package.

---

# app/

Contains the application source code.

---

## api/

Handles HTTP communication.

Responsibilities:

- API routes
- Request handling
- Response generation
- HTTP status codes

This layer communicates with the Service layer.

It contains no business logic and no database logic.

---

## core/

Contains application-wide configuration.

Examples:

- Settings
- Configuration
- Dependency injection
- Shared utilities

---

## database/

Contains database configuration.

Examples:

- Database connection
- Session management
- Engine configuration

This package does not contain business logic.

---

## domain/

Contains business constants.

Examples:

- Enums
- Shared business definitions

These represent concepts used throughout the application.

---

## schemas/

Contains Pydantic models.

Responsibilities:

- Request validation
- Response serialization
- API contracts

Typical schema types:

- Base
- Create
- Update
- Response

Schemas are used only for communication between clients and the backend.

---

## models/ (Week 2)

Contains SQLAlchemy models.

Responsibilities:

- Database tables
- Relationships
- Constraints

Models describe how data is stored.

---

## repositories/ (Week 2)

Contains database access logic.

Responsibilities:

- CRUD operations
- Database queries
- Persistence

Repositories communicate directly with SQLAlchemy.

---

## services/ (Week 2)

Contains business logic.

Responsibilities:

- Validation beyond schemas
- Business rules
- Workflow orchestration
- Coordination between repositories

Services are independent of HTTP and the database implementation.

---

# Layered Architecture

```
HTTP Request
        │
        ▼
     Router
        │
        ▼
    Pydantic Schema
        │
        ▼
      Service
        │
        ▼
    Repository
        │
        ▼
 SQLAlchemy Model
        │
        ▼
     Database
```

---

# Design Principles

- Every package has a single responsibility.
- Routers never contain business logic.
- Services never handle HTTP requests.
- Repositories never contain business rules.
- Models describe persistence.
- Schemas describe API contracts.
- Domain contains business concepts shared across the application.


## Dependencies
api
    ↓
services
    ↓
repositories
    ↓
models
    ↓
database



