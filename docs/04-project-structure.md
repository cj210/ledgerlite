# Project Structure

## Purpose

Define the architectural organization of the LedgerLite repository.

The repository contains the backend, frontend, tests, and project documentation.

Each major area has a clear responsibility and should avoid unnecessary overlap with other areas.

---

# Repository Structure

    ledgerlite/
    ├── app/                    # Backend application
    ├── ui/                     # Frontend application
    ├── tests/                  # Backend tests
    ├── docs/                   # Project documentation
    ├── .venv/                  # Backend virtual environment
    ├── requirements.txt        # Backend dependencies
    └── ...

---

# Backend

The backend application is contained within `app/`.

    app/
    ├── api/
    ├── core/
    ├── database/
    ├── domain/
    ├── schemas/
    ├── models/
    ├── repositories/
    └── services/

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

Schemas are used for communication between clients and the backend.

---

## models/

Contains SQLAlchemy models.

Responsibilities:

- Database tables
- Relationships
- Constraints

Models describe how data is stored.

---

## repositories/

Contains database access logic.

Responsibilities:

- CRUD operations
- Database queries
- Persistence

Repositories communicate directly with SQLAlchemy.

---

## services/

Contains business logic.

Responsibilities:

- Validation beyond schemas
- Business rules
- Workflow orchestration
- Coordination between repositories

Services are independent of HTTP and the database implementation.

---

# Backend Layered Architecture

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

---

# Frontend

The frontend application is contained within `ui/`.

The initial structure is:

    ui/
    ├── package.json
    ├── package-lock.json
    └── src/
        ├── components/
        ├── pages/
        ├── api/
        ├── utils/
        ├── App.jsx
        └── main.jsx

Detailed frontend architectural decisions are documented in:

`15-frontend-architecture.md`

UI conventions and design decisions are documented in:

`16-ui-guidelines.md`

---

# Design Principles

- Each major area has a clear responsibility.
- Backend layers should not overlap responsibilities.
- Frontend and backend remain separate applications.
- Frontend communication with the backend occurs through the API contract.
- Internal implementation details should remain within their respective application.
- Project structure should evolve when actual complexity requires it.

## Backend Dependencies

    api
     ↓
    services
     ↓
    repositories
     ↓
    models
     ↓
    database
