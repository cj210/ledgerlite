# Architecture Journal

## Purpose

This journal records significant architectural decisions, implementation milestones, lessons learned, and remaining architectural work for LedgerLite.

It is not intended to duplicate detailed architecture documentation. Its purpose is to preserve the reasoning behind important decisions so that future implementation can continue without losing architectural context.

---

# Current Architecture

LedgerLite follows a layered backend architecture:

    API / Routes
         ↓
    Schemas
         ↓
    Services
         ↓
    Repositories
         ↓
    Models
         ↓
    Database

Supporting areas include:

    app/
    ├── core/
    ├── database/
    ├── models/
    ├── repositories/
    ├── services/
    ├── schemas/
    ├── routers/
    ├── domain/
    └── scripts/

The architecture separates:

- HTTP/API concerns
- validation and serialization
- business logic
- database access
- persistence models
- domain concepts
- configuration and infrastructure

The objective is to keep responsibilities isolated so completed features can remain stable while new functionality is added.

---

# Architectural Philosophy

LedgerLite is being developed feature-by-feature using user stories.

The objective is not to build every possible abstraction before implementing functionality.

The approach is:

1. Establish the architectural boundary.
2. Implement the feature.
3. Validate the boundary.
4. Test the feature.
5. Preserve the completed behavior.
6. Extend the architecture only when new functionality requires it.

Completed features should normally become stable legacy functionality.

Future features should primarily add new classes, methods, modules, or flows rather than unnecessarily modifying completed functionality.

If completed functionality unexpectedly breaks, it should be treated as a regression or production defect rather than normal development behavior.

---

# Database Architecture

SQLAlchemy is used as the database abstraction layer.

The application uses:

- SQLAlchemy models
- SQLAlchemy Engine
- SQLAlchemy Session
- repositories for database interaction

The database implementation should remain replaceable.

The application architecture should not depend unnecessarily on SQLite-specific behavior.

PostgreSQL remains a supported target for validation.

Database portability will be deliberately tested during development rather than assumed.

---

# Engine and Session

Database infrastructure was established before continuing with repository implementation.

Current structure:

    app/database/
    ├── engine.py
    └── session.py

The Engine is responsible for database connectivity.

The Session provides the unit-of-work interface used by repositories.

Repositories receive or use the session rather than creating their own database infrastructure.

This keeps database infrastructure separate from repository and service logic.

---

# Models

SQLAlchemy models represent the persistence structure of the application.

Current entities include:

- User
- Category
- Goal
- Tag
- FinancialRecord

The SQLAlchemy declarative base is defined separately.

Models are imported through the models package so SQLAlchemy can resolve relationships between mapped classes.

Relationship annotations use appropriate typing information so SQLAlchemy can correctly resolve collection relationships.

The model layer should remain focused on persistence representation and relationships rather than becoming a container for application-level business logic.

---

# Repository Layer

The repository layer was introduced as part of Deliverable 6.

Its purpose is to isolate database interaction from services and higher layers.

Typical flow:

    Service
       ↓
    Repository
       ↓
    Session
       ↓
    SQLAlchemy
       ↓
    Database

Repositories are responsible for persistence operations such as:

- retrieving records
- inserting records
- updating records
- deleting records where appropriate

Repositories should not contain business calculations or application workflow logic that belongs in services.

The repository layer prevents the rest of the application from becoming tightly coupled to SQLAlchemy query details.

---

# Service Layer

The service layer is responsible for application and business behavior.

Typical flow:

    API
     ↓
    Schema
     ↓
    Service
     ↓
    Repository

Services should:

- coordinate application operations
- apply business rules
- perform calculations
- coordinate repositories
- determine application behavior

Services should not directly implement HTTP concerns.

Services should not bypass repositories to perform database operations directly.

---

# Schema Layer

Schemas define the data contract between the API and the application.

They are responsible for:

- request validation
- response serialization
- input/output structure
- API-facing data representation

Schemas should not become a replacement for domain or business logic.

Validation representing API input requirements belongs in schemas.

Business rules requiring application decisions belong in the service or domain layer.

---

# API / Router Layer

The API layer exposes application functionality through HTTP.

Typical flow:

    HTTP Request
         ↓
    API Route
         ↓
    Schema Validation
         ↓
    Service
         ↓
    Repository
         ↓
    Database

Routes should remain thin.

They should primarily:

- receive requests
- validate and parse input
- invoke services
- return responses
- translate appropriate application errors into HTTP responses

Business logic should not accumulate inside route functions.

---

# Configuration

Application configuration is centralized under:

    app/core/config.py

The database URL is configuration-driven rather than hardcoded into application components.

The architecture should allow the database implementation to be changed through configuration without modifying models, services, or repositories.

---

# Database Initialization

Database initialization is handled separately from application runtime.

The project contains:

    scripts/init_db.py

The initialization script imports model metadata and creates the required tables through the configured SQLAlchemy Engine.

Database creation therefore does not belong inside repositories or services.

---

# US-001 — Create an Account

The latest completed implementation milestone is:

    Backend: Implement US-001 — Create an Account

US-001 established the first complete backend flow across the relevant layers.

The implementation changed User-related files across:

- models
- repositories
- services
- schemas
- API

The backend implementation of US-001 is now complete.

Testing is the next major activity.

---

# US-001 Testing Strategy

Testing will proceed from the inside out.

The order is:

    Models
       ↓
    Repositories
       ↓
    Services
       ↓
    Schemas
       ↓
    API

The purpose is to establish confidence in each layer before moving outward.

Each meaningful class and method changed for US-001 should receive appropriate unit-test coverage.

Tests should verify meaningful behavior rather than artificially forcing every trivial implementation detail to have its own test.

---

# Backend Unit Testing

The backend unit-test framework will use:

- pytest

Location:

    app/tests/unit_test/

Unit tests will not use a real database.

Dependencies will be mocked where isolation requires it.

For example:

    Service
       ↓
    Mock Repository

and:

    Repository
       ↓
    Mock Session

Unit tests should verify:

- input reaches the dependency correctly
- dependency calls are correct
- dependency responses are handled correctly
- expected output is generated
- expected errors are raised or propagated

The unit-test suite provides detailed coverage for:

- validation
- negative scenarios
- edge cases
- business rules
- error handling
- individual method behavior

---

# Integration Testing

After backend unit tests are complete, US-001 integration testing will be implemented.

Location:

    app/tests/integration_test/

Integration tests will not mechanically mirror the application directory.

They will represent meaningful application flows.

For example:

    API
     ↓
    Schema
     ↓
    Service
     ↓
    Repository
     ↓
    Model
     ↓
    Database

The purpose is to verify that concrete components integrate correctly.

Integration tests should not simply repeat every unit test.

---

# Integration Database Strategy

Integration tests will use a real isolated database.

The initial implementation will use an in-memory database where appropriate.

Setup and teardown are mandatory.

Expected lifecycle:

    Fresh Database
         ↓
    Test Setup
         ↓
    Test
         ↓
    Cleanup
         ↓
    Fresh State

Tests must not depend on records created by previous tests.

Tests may create and delete their own records, but the overall fixture lifecycle must still guarantee isolation.

Tests should be executable in randomized order.

Randomized execution is intended to expose:

- leaked state
- fixture pollution
- incomplete teardown
- order-dependent behavior

---

# Factories

Test factories are a core part of the testing infrastructure.

Factories provide reusable test data.

Factories should generate valid domain data by default.

Tests can override specific fields when testing invalid or special cases.

Example:

    UserFactory()

produces a valid user.

An invalid scenario can deliberately override a field:

    UserFactory(mobile="123")

Factories may use randomized values to broaden reasonable test coverage.

Randomization is not intended to exhaustively test every possible input.

When randomized data contributes to a failure, the generated data must be visible enough to reproduce the scenario.

The exact random-seed mechanism will be decided when the factory framework is implemented.

Factories must not contain application business logic.

---

# Fixtures

Fixtures manage resources and lifecycle.

Factories manage test data.

These responsibilities remain separate.

Fixtures may manage:

- database setup
- database teardown
- sessions
- application clients
- test configuration
- reusable dependencies

Factories create entities and domain test data.

---

# Testing Independence

Every test should be independent.

Tests must not rely on:

- execution order
- another test's data
- persistent developer database state
- previous test side effects

The test suite should support randomized execution.

A failure caused by test ordering or state leakage indicates a problem with the test infrastructure.

---

# Database Portability Testing

The application is designed to avoid unnecessary database-specific coupling.

After several features have been implemented, the integration suite can deliberately be run against another supported database.

For example:

    Features 1–3 complete
          ↓
    Switch database
          ↓
    Run full integration suite
          ↓
    Identify database coupling
          ↓
    Fix architectural issues
          ↓
    Continue development

This is a deliberate validation exercise rather than a requirement to switch databases continuously.

---

# Testing Architecture

The complete backend testing approach is:

    Backend Application

          API
           ↓
         Schema
           ↓
        Service
           ↓
      Repository
           ↓
         Model
           ↓
       Database


    Unit Testing

    Model
       ↓
    Repository     → mocked dependencies
       ↓
    Service        → mocked repository
       ↓
    Schema
       ↓
    API            → mocked dependencies


    Integration Testing

    API
     ↓
    Schema
     ↓
    Service
     ↓
    Repository
     ↓
    Model
     ↓
    Real isolated test database

Unit tests validate individual responsibilities.

Integration tests validate concrete application flows.

E2E testing will later validate the complete application from the user's perspective.

Regression testing will be a selected subset of E2E tests protecting completed user stories.

---

# Environment Strategy

LedgerLite uses three environments:

    DEV
     ↓
    TEST
     ↓
    PROD

There is no separate staging environment.

The TEST environment serves as the staging-equivalent validation environment.

## DEV

DEV is used for:

- active development
- fast unit testing
- local integration testing
- local E2E testing where useful

Developer testing discipline remains important.

CI is not a replacement for regular local testing.

## TEST

TEST is the main validation environment.

It is used for:

- integration tests
- E2E tests
- regression tests
- performance tests
- load tests
- concurrency tests
- reliability tests

## PROD

PROD is not used for normal automated testing.

Heavy automated validation occurs before production deployment.

Production verification should remain minimal and safe.

---

# CI/CD Direction

GitHub Actions will eventually provide CI automation.

The project will use available free GitHub Actions capabilities and will not introduce paid infrastructure for this practice project.

Intended pipeline:

    Developer
       ↓
    Local Tests
       ↓
    Commit
       ↓
    Push
       ↓
    GitHub Actions
       ↓
    Automated Test Suites
       ↓
    Deployment Gate
       ↓
    TEST
       ↓
    PROD

CI is a safety net and should not replace developer testing discipline.

---

# Deployment Gates

Deployment gates should be deliberately strong.

The project should not avoid running tests simply because a test suite takes time.

Developers are expected to maintain tests regularly so CI remains reliable.

Required validation should pass before deployment.

The exact split between fast and heavy CI stages can be optimized during implementation.

---

# Performance, Load, Concurrency and Reliability

These categories will remain deliberately simple.

The strategy is:

    Performance      → one E2E-level test
    Load             → one E2E-level test
    Concurrency      → one E2E-level test
    Reliability      → one E2E-level test

All will run in the TEST environment.

The project does not require a large performance-testing infrastructure.

The objective is basic protection against significant regressions while keeping the strategy appropriate for a practice project.

---

# Browser Coverage

Playwright browser coverage will focus on:

- Chrome
- Firefox

Supported operating-system coverage will include:

- Windows
- Linux

Other Chromium-derived browsers are not a priority.

The project will not spend disproportionate effort testing every browser variant.

---

# Current Status

## Completed

- Backend architecture established
- SQLAlchemy model layer implemented
- Database Engine implemented
- Session factory implemented
- Database initialization implemented
- User model relationships resolved
- Model import and mapper issues resolved
- Repository layer introduced
- Service layer established
- Schema layer established
- API route established
- US-001 backend implementation completed
- Testing strategy defined and consolidated
- Test environments defined
- CI/CD direction defined

Latest commit:

    Backend: Implement US-001 — Create an Account

---

# Immediate Next Work

The immediate work is backend testing for US-001.

Frontend work is intentionally deferred until the backend testing phase is complete.

The next sequence is:

    US-001 Backend
          ↓
    Backend Unit Tests
          ↓
    Models
          ↓
    Repositories
          ↓
    Services
          ↓
    Schemas
          ↓
    API

For each layer:

1. inspect the changed implementation
2. identify meaningful classes and methods
3. determine the correct unit-test boundary
4. create the test
5. run pytest
6. investigate failures
7. correct implementation or test design where necessary
8. continue to the next layer

Only after the complete US-001 backend unit-test suite is passing will integration testing begin.

---

# Remaining Work for US-001

The intended sequence is:

    US-001 Backend Implementation
             ↓
    Backend Unit Tests
             ↓
    Backend Integration Tests
             ↓
    Frontend Implementation
             ↓
    Frontend Unit Tests
             ↓
    Frontend Integration Tests
             ↓
    E2E
             ↓
    Regression Coverage
             ↓
    CI/CD Validation

After US-001 becomes fully validated, development continues with the next user story.

The same architectural and testing approach will be reused for subsequent features.

---

# Long-Term Development Cycle

The desired development cycle is:

    User Story
         ↓
    Architecture
         ↓
    Implementation
         ↓
    Unit Tests
         ↓
    Integration Tests
         ↓
    Frontend
         ↓
    E2E
         ↓
    Regression Protection
         ↓
    CI
         ↓
    Complete Feature

The architecture should become more stable as the application grows.

New functionality should primarily extend existing boundaries rather than bypass them.

The testing suite should grow with the application and become the safety net that allows completed features to remain stable while new functionality is introduced.

---

# Lessons Learned

## Database Infrastructure Before Repositories

The repository layer depends on a working SQLAlchemy Engine and Session.

Repositories should not be implemented before the database infrastructure they depend upon is understood and established.

## SQLAlchemy Relationship Resolution

SQLAlchemy relationships require correct type annotations and model registration.

When models reference each other, all mapped models must be discoverable by SQLAlchemy before mapper configuration completes.

## Repository Responsibility

Repositories own database interaction.

Services should not bypass repositories to directly manipulate persistence.

## Service Responsibility

Services coordinate application behavior and business rules.

They should not become database-access layers or HTTP handlers.

## Schema Responsibility

Schemas validate and serialize API data.

They should not become containers for unrelated business logic.

## API Responsibility

Routes should remain thin.

Business logic belongs below the API boundary.

## Testing Responsibility

Unit tests isolate.

Integration tests integrate.

E2E tests behave like users.

Regression protects completed user stories.

---

# Architectural Rule Going Forward

When implementing a new feature, ask:

    Does this belong to:

    Model?
    Repository?
    Service?
    Schema?
    API?

If it does not clearly belong to one layer, determine the responsibility before adding the code.

Likewise for tests:

    Is this testing one unit?
        ↓
    Unit test

    Is this testing multiple concrete backend components?
        ↓
    Integration test

    Is this testing the complete user workflow?
        ↓
    E2E

    Is this protecting a completed user workflow?
        ↓
    Regression subset

The objective is not to maximize the number of abstractions or tests.

The objective is to make the architecture predictable, testable, replaceable, and safe to extend.
