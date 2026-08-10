# TESTING STRATEGY

## 1. Purpose

This document defines the testing strategy for LedgerLite across the backend, frontend, and complete application.

The strategy is based on user-story-driven development.

Each user story represents a feature. A feature is considered complete only when its implementation and appropriate automated tests are complete 
and passing.

The testing architecture is designed to:

- isolate individual units of code
- verify integration between concrete application components
- verify complete user workflows
- protect completed features from regressions
- detect environment, database, and integration problems
- keep test data isolated and reproducible
- provide strong deployment gates without unnecessary testing infrastructure

The strategy intentionally avoids creating separate testing systems where an existing test layer already provides the required coverage.

---

# 2. Testing Architecture

LedgerLite uses four primary testing layers:

1. Unit testing
2. Integration testing
3. End-to-end testing
4. Regression testing

Regression testing is a subset of end-to-end testing rather than a separate implementation or framework.

Additional E2E-based checks are used for:

- Performance
- Load
- Concurrency
- Reliability

The overall architecture is:

                         END-TO-END
                         Playwright
                             |
                   +---------+---------+
                   |                   |
              Regression           Other E2E
                                       |
                           +-----------+-----------+
                           |           |           |
                       Performance    Load    Concurrency
                                               Reliability
                           |
              +------------+-------------+
              |                          |
      Backend Integration       Frontend Integration
            pytest                Vitest + RTL + MSW
              |                          |
              +------------+-------------+
                           |
                     Unit Testing
                    +------+------+
                    |             |
               Backend Unit   Frontend Unit
                  pytest      Vitest + RTL


---

# 3. Unit Testing

## 3.1 Purpose

Unit tests verify individual functions, methods, classes, components, hooks, or other meaningful units of behavior in isolation.

Dependencies outside the unit under test are replaced with mocks or other test doubles where appropriate.

Unit tests should be:

- isolated
- fast
- deterministic except for deliberate data randomization
- focused on one primary behavior
- independent of the database
- independent of external services

Unit testing is the primary layer for detailed validation, negative scenarios, edge cases, and individual business rules.

---

# 4. Backend Unit Tests

## 4.1 Tool

Backend unit tests use:

- pytest

## 4.2 Location

    app/tests/unit_test/

## 4.3 Structure

The unit-test structure mirrors the testable application code.

It does not mechanically mirror every file in the application.

For example:

    app/
    ├── services/
    │   └── user.py
    ├── repositories/
    │   └── user.py
    ├── models/
    │   └── user.py
    └── domain/
        └── user.py

may have:

    app/tests/unit_test/
    ├── services/
    │   └── test_user.py
    ├── repositories/
    │   └── test_user.py
    ├── models/
    │   └── test_user.py
    └── domain/
        └── test_user.py

Trivial definitions such as simple enums do not automatically require dedicated test files.

The structure exists for organization and traceability, not to impose artificial test counts.

## 4.4 Dependencies

Backend unit tests do not use a real database.

Database interaction is represented through mocks or other test doubles.

For example:

    Service
       |
       v
    Mock Repository
       |
       v
    Mock Response

The test verifies that:

- the unit receives the expected input
- the unit interacts with its dependency correctly
- the unit produces the expected behavior from the dependency response

The mocked dependency itself can be tested independently where appropriate.

---

# 5. Backend Integration Tests

## 5.1 Tool

Backend integration tests use:

- pytest

## 5.2 Location

    app/tests/integration_test/

## 5.3 Purpose

Backend integration tests verify meaningful flows across concrete backend components.

A typical integration flow may include:

    API Route
        |
        v
    Schema
        |
        v
    Service
        |
        v
    Repository
        |
        v
    Model
        |
        v
    Database

Integration tests are organized around meaningful flows and features rather than mechanically mirroring the application directory.

## 5.4 Database

Integration tests use a real isolated test database.

The initial implementation may use an in-memory database.

The application architecture must not depend on a particular database implementation.

The integration suite should therefore be capable of being run against another supported database when deliberately validating database portability.

## 5.5 Scope

Integration tests should verify meaningful boundaries and data flows.

They should not simply duplicate every unit test.

For example, if unit tests already verify individual validation rules, integration tests should focus on whether the complete flow correctly 
moves data through:

    Route
      -> Schema
      -> Service
      -> Repository
      -> Database

---

# 6. Frontend Unit Tests

## 6.1 Tools

Frontend unit tests use:

- Vitest
- React Testing Library

## 6.2 Location

    ui/src/tests/unit_test/

## 6.3 Purpose

Frontend unit tests verify observable component, function, hook, and isolated frontend behavior.

For a user onboarding feature, appropriate unit coverage includes:

1. required fields are rendered
2. user can enter data
3. user can select a user type
4. validation state appears
5. submit behavior is triggered
6. success state is rendered when the API dependency succeeds
7. error state is rendered when the API dependency fails

Detailed validation, negative scenarios, and edge cases should primarily be covered at this level.

Tests should verify behavior rather than React implementation details.

---

# 7. Frontend Integration Tests

## 7.1 Tools

Frontend integration tests use:

- Vitest
- React Testing Library
- MSW

## 7.2 Location

    ui/src/tests/integration_test/

## 7.3 Purpose

Frontend integration tests verify meaningful interaction between frontend components and the HTTP boundary.

MSW provides realistic HTTP-level behavior without requiring the actual backend to be running.

A typical flow is:

    Component
        |
        v
    Frontend Service
        |
        v
    HTTP Request
        |
        v
    MSW
        |
        v
    HTTP Response
        |
        v
    UI State

MSW is testing infrastructure, not a separate testing category.

---

# 8. End-to-End Testing

## 8.1 Tool

E2E tests use:

- Playwright

## 8.2 Purpose

E2E tests validate the application from the user's perspective.

E2E tests do not depend on whether the application uses:

- React
- FastAPI
- Axios
- SQLAlchemy
- repositories
- services
- SQLite
- PostgreSQL

The E2E test represents the user's interaction with the complete application.

A typical flow is:

    User
      |
      v
    UI
      |
      v
    Application
      |
      v
    Expected user-visible result

E2E tests should primarily cover meaningful happy-path user journeys and selected important negative scenarios.

Extensive validation and edge-case coverage belongs at lower testing levels.

---

# 9. API Testing

LedgerLite does not maintain a separate API-testing category.

API behavior is covered through:

- backend integration tests
- E2E tests where API behavior forms part of a user workflow

This avoids creating a separate test category that duplicates integration coverage.

The API remains an important boundary, but it does not require an independent testing framework.

---

# 10. Regression Testing

## 10.1 Definition

Regression testing is a subset of E2E testing.

It is not a separate implementation or framework.

Conceptually:

    E2E
    ├── General E2E scenarios
    └── Regression subset

Regression tests protect completed user-facing functionality against future changes.

## 10.2 Location

E2E tests are maintained under:

    tests/e2e/

Regression scenarios are selected from those E2E tests.

They should be associated with completed user stories rather than duplicated into a separate test implementation.

## 10.3 Scope

The regression suite remains smaller than the complete E2E suite.

Regression coverage prioritizes:

- critical user journeys
- core business functionality
- previously problematic behavior
- functionality that must not break after future changes

Regression testing is therefore selective rather than exhaustive.

---

# 11. User Stories and Feature Completion

User stories are the primary unit of feature development.

For each user story:

1. implement the feature
2. write relevant unit tests
3. identify meaningful integration scenarios
4. implement integration tests
5. implement appropriate E2E scenarios
6. add the appropriate E2E scenarios to regression coverage where required
7. validate the feature through the required environments and CI gates

A feature is not considered complete merely because its code works locally.

---

# 12. Feature Isolation and Legacy Protection

Once a user story is complete, its behavior becomes protected functionality.

Future features should normally add new functionality without requiring changes to completed functionality.

The corresponding tests become the protection mechanism for that legacy behavior.

If a completed feature unexpectedly breaks:

    Completed Feature
          |
          v
    Regression Test Fails
          |
          v
    Production Defect / Regression

If a future requirement intentionally changes the old behavior, the affected user-story contract and tests are updated deliberately.

---

# 13. Test Data and Factories

Factories are a core part of the testing architecture.

Factories provide reusable test data and should normally generate valid domain data.

For example:

    UserFactory()

may create a complete valid user.

Tests override only the fields relevant to the scenario.

## 13.1 Valid Data

Factories should generate valid data by default.

## 13.2 Invalid Data

Invalid scenarios should be deliberate.

For example:

    UserFactory(
        mobile="123"
    )

The test should clearly communicate that the value is intentionally invalid.

Random generation must not accidentally determine whether a scenario is valid or invalid.

## 13.3 Randomized Data

Factories may use randomized data to broaden reasonable coverage over time.

Randomization is not intended to exhaustively test every possible input.

The project will test reasonable scenarios rather than attempting to enumerate every possible state.

When randomized data contributes to a useful failure, the generated values should be visible in the test output so that the specific scenario 
can be reproduced.

The exact seed-management mechanism will be decided when the factory framework is implemented.

## 13.4 Factory Responsibilities

Factories should:

- create reusable test data
- generate valid defaults
- satisfy uniqueness requirements where required
- reflect current domain constraints
- support deliberate overrides

Factories should not contain application business logic.

---

# 14. Fixtures and Test Lifecycle

Fixtures manage resources and lifecycle.

Factories create data.

These are separate responsibilities.

For example:

    Database Fixture
          |
          v
    Creates database/session
          |
          v
        Test
          |
          v
      Teardown

while:

    User Factory
          |
          v
    Creates test user data

## 14.1 Setup and Teardown

Every test must have an appropriate lifecycle.

For database tests:

    Setup
      |
      v
    Fresh State
      |
      v
    Test
      |
      v
    Teardown
      |
      v
    Clean State

A test may create and delete records during its own execution.

That does not remove the requirement for outer teardown.

The next test must still receive a fresh starting state.

## 14.2 Test Independence

Tests must be independent of execution order.

Tests should be capable of being randomized and executed in arbitrary order.

If a test depends on another test having run first, the test architecture is considered defective.

## 14.3 Randomized Test Execution

Randomized execution will be used deliberately to identify:

- hidden state dependencies
- fixture pollution
- incomplete teardown
- order-dependent behavior

---

# 15. Database Strategy

The application architecture should not depend on a specific database implementation.

Integration testing begins with an isolated in-memory database where appropriate.

Supported database implementations may be deliberately switched during development to expose hidden database coupling.

For example:

    Features 1-3
        |
        v
    Switch Database
        |
        v
    Full Integration Suite
        |
        v
    Continue Development

Database switching is a deliberate validation activity rather than something that must happen continuously.

The test suite must not depend on persistent developer-local database state.

---

# 16. Test Doubles and Mocking Standards

Mocks and test doubles are primarily used to isolate dependencies in unit tests.

They should not be used merely to make tests easier.

## Unit

    Unit
      |
      v
    Mock Dependencies

## Integration

    Real Components
          |
          v
    Real Test Database

## E2E

    Real Application
          |
          v
    Real User Workflow

The closer a test is to E2E, the less artificial the environment should be.

Tests must not simply verify the behavior of mocks themselves.

Excessive mocking can indicate that production code has too many responsibilities or is unnecessarily coupled.

If something becomes extremely difficult to test, the production design should be examined before adding increasingly complex testing infrastructure.

---

# 17. Test Organization

The test organization follows the purpose of each test level.

## Unit

Organized around testable application code.

## Integration

Organized around meaningful application flows and features.

## E2E

Organized around user workflows.

Example:

    tests/
    └── e2e/
        ├── user/
        ├── category/
        ├── financial_record/
        └── ...

## Regression

Regression scenarios are selected from E2E and associated with completed user stories.

The project does not require meaningless test-case numbering such as:

    TC001
    TC002
    TC003

User-story identifiers provide feature traceability.

---

# 18. Test Naming

Test names should describe behavior rather than implementation.

Examples:

    test_creates_user_with_valid_details()
    test_rejects_duplicate_username()
    test_shows_validation_error_for_invalid_mobile()
    test_user_can_create_account()

Avoid names such as:

    test_user_service_method()
    test_post_users_endpoint()
    test_use_state_updates_form()

unless the implementation detail itself is the behavior being tested.

A test name should make it possible to understand what behavior failed without first reading the implementation.

---

# 19. Test Code Quality

Tests are production-quality code.

A good test should be:

- readable
- isolated
- focused
- meaningful
- maintainable
- independently executable
- diagnosable when it fails

The default structure is:

    Arrange
       |
       v
     Act
       |
       v
    Assert

Test readability is preferred over excessive abstraction.

Some duplication is acceptable when it makes the test clearer.

Tests should not become a complex framework of helpers that hides the behavior being tested.

---

# 20. Assertions

Assertions should verify meaningful behavior.

Tests should not over-assert implementation details.

For example, an E2E test should verify that the user sees:

    User created successfully

rather than asserting:

- internal React state
- DOM nesting
- CSS implementation
- backend service implementation

where those details are irrelevant to the user-facing contract.

The number of assertions should be driven by the behavior being protected, not by an attempt to verify every available field.

---

# 21. Test Duplication Across Layers

The same behavior may legitimately be tested at multiple layers when each test protects a different contract.

For example:

    Unit
      -> service handles duplicate username

    Integration
      -> persistence and application flow correctly handle duplicate username

    E2E
      -> user receives the expected result

These are not considered unnecessary duplication because each validates a different boundary.

However, the exact same scenario should not be blindly repeated at every layer.

Unit tests provide deep validation.

Integration tests verify component/data flow.

E2E tests verify user behavior.

---

# 22. E2E Selector Standards

Playwright tests should prefer stable, user-oriented selectors.

Preferred order:

    Accessible Role
          |
          v
        Label
          |
          v
     Visible Text
          |
          v
    Stable Test Identifier
          |
          v
      CSS Selector

Avoid brittle selectors based on DOM structure such as:

    div:nth-child(3) > div > button

E2E tests should not depend on arbitrary DOM implementation.

---

# 23. Timing and Flakiness

Tests should not rely on arbitrary delays.

Avoid unnecessary:

    sleep(5)

Prefer waiting for:

- expected UI state
- expected element state
- application conditions
- relevant network/application completion

A flaky test is treated as a test defect until its cause is understood.

Flaky tests should be investigated and fixed rather than permanently ignored.

---

# 24. Test Failure Diagnostics

A failed test should provide enough information to answer:

1. What failed?
2. Which scenario failed?
3. Where did it fail?
4. What were the expected and actual results?
5. What test data was involved?

Randomized factory data should be visible when it contributes to a failure.

E2E failures should retain useful Playwright diagnostics such as:

- screenshots
- traces
- relevant console/network information where appropriate

CI must expose clear pass/fail results.

Test duration should also be observable so significant degradation in the test suite itself can be identified.

---

# 25. Test Coverage

Coverage is a diagnostic tool, not a guarantee of correctness.

LedgerLite does not require arbitrary 100% coverage.

Coverage should be used to:

- identify untested areas
- identify blind spots
- monitor trends
- detect unexpected coverage drops

A sudden coverage decrease after adding a feature should be investigated.

Coverage should grow naturally alongside implemented features.

---

# 26. Test Environments

LedgerLite uses exactly three environments:

    DEV
    TEST
    PROD

There is no separate staging environment.

The TEST environment serves the role normally associated with staging for this project.

## 26.1 DEV

DEV is used for:

- active development
- fast unit testing
- local integration testing
- local E2E testing where useful

Developers should run relevant tests regularly during development.

CI is not a substitute for local development discipline.

## 26.2 TEST

TEST is the main validation environment.

It is used for:

- full integration testing
- E2E testing
- regression testing
- performance testing
- load testing
- concurrency testing
- reliability testing

The TEST environment should resemble the deployed application sufficiently for these tests to provide meaningful results.

## 26.3 PROD

Production is not used as the normal automated testing environment.

Normal automated tests do not run against production data.

Heavy validation occurs before deployment.

Production testing should remain minimal and limited to safe post-deployment verification where required.

---

# 27. Performance, Load, Concurrency and Reliability

These categories are intentionally simple.

Each category has one E2E-level test executed in the TEST environment.

    Performance   -> 1 E2E test
    Load          -> 1 E2E test
    Concurrency   -> 1 E2E test
    Reliability   -> 1 E2E test

The project is not intended to build a large performance-testing infrastructure.

The objective is basic protection against significant regressions while keeping the testing strategy appropriate for a practice project.

---

# 28. Browser Coverage

Playwright browser coverage will focus on:

- Chrome
- Firefox

Supported operating-system coverage will include:

- Windows
- Linux

Other Chromium-derived browsers are not a priority.

The project will not spend disproportionate effort testing every browser variant.

---

# 29. CI/CD

GitHub Actions will be used for CI.

The project will use available free CI capabilities and will not introduce paid infrastructure for the practice project.

The development workflow is:

    Developer
       |
       v
    Implement Feature
       |
       v
    Write Tests
       |
       v
    Run Relevant Tests Locally
       |
       v
    Commit
       |
       v
    Push
       |
       v
    GitHub Actions
       |
       v
    Test Suites
       |
       v
    Deployment Gate
       |
       v
    Deploy

CI is a safety net, not a replacement for developer testing discipline.

---

# 30. Deployment Gates

Deployment gates should be deliberately strong.

The project should not avoid running tests simply because a test suite takes time.

Developers are expected to maintain tests regularly so that the CI pipeline remains reliable.

The deployment pipeline should prevent deployment when required validation fails.

The exact split between fast and heavy CI stages may be optimized during implementation, but deployment should remain protected by 
comprehensive automated validation.

---

# 31. Test Execution Categories

The test infrastructure should eventually provide simple ways to execute:

- unit tests
- integration tests
- E2E tests
- regression tests
- performance tests
- load tests
- concurrency tests
- reliability tests
- backend tests
- frontend tests
- full test suite

There should be one obvious full-suite execution path so developers do not need to remember numerous individual commands.

The exact CLI implementation will be decided when the framework is implemented.

---

# 32. Test Reporting

Test reports should answer:

1. What failed?
2. Where did it fail?
3. Which scenario was being tested?
4. What were the expected and actual results?
5. Can the failure be reproduced or investigated?

The project does not require an elaborate QA dashboard.

Clear CLI and CI output plus appropriate E2E artifacts are sufficient.

---

# 33. Skipped Tests

Skipped tests should not silently accumulate.

An intentional skip should have a clear reason, such as:

- unavailable dependency
- platform-specific behavior
- temporary known issue

Permanently skipped tests should be reviewed and either restored, replaced, or removed.

---

# 34. Lessons Learned

A lessons-learned document will record recurring testing problems and their solutions.

Examples include:

- fixture pollution
- incomplete teardown
- environment contamination
- database state leakage
- incorrect mocks
- factory problems
- CI-only failures
- browser-specific failures
- flaky test behavior

The purpose is to prevent repeatedly solving the same testing problems.

---

# 35. Performance of the Test Suite

Test correctness and isolation take priority over shaving milliseconds from individual tests.

A slightly slower but reliable and isolated test is preferable to a fast test that leaks state.

Once correctness and isolation are established, unnecessary test-suite slowdown should be investigated.

Test duration should be monitored so significant degradation becomes visible.

---

# 36. Feature Definition of Done

A user story is complete only when the following are satisfied.

## Implementation

- feature implementation is complete
- feature follows the application architecture
- feature boundaries are respected

## Backend

- relevant unit tests exist
- meaningful integration flows exist
- factories/fixtures exist where required
- setup and teardown are reliable

## Frontend

- relevant unit tests exist
- meaningful integration tests exist
- MSW is used where HTTP dependency behavior must be simulated

## User Behavior

- appropriate E2E workflow exists
- regression coverage is added where the feature is important enough to protect

## Quality

- tests are independent
- tests have meaningful names
- unnecessary duplication is avoided
- unnecessary mocking is avoided
- failures are diagnosable
- test data is isolated

## CI/CD

- relevant tests pass locally
- CI passes
- deployment gates pass

Only then is the feature considered complete.

---

# 37. Core Testing Principles

LedgerLite follows these principles:

1. Test behavior rather than implementation details wherever practical.
2. Unit tests provide deep isolated coverage.
3. Integration tests verify meaningful component and data flows.
4. E2E tests verify user workflows.
5. Regression is a subset of E2E.
6. API testing is covered through backend integration and E2E rather than a separate testing category.
7. Backend unit tests do not use a real database.
8. Backend integration tests use a real isolated database.
9. Database choice must not become a hidden application dependency.
10. Factories provide reusable and optionally randomized test data.
11. Factories generate valid data by default.
12. Invalid scenarios are deliberate.
13. Fixtures manage resources and lifecycle; factories manage data creation.
14. Every test has an appropriate setup and teardown strategy.
15. Tests are independent of execution order.
16. Randomized execution is used to expose hidden test dependencies.
17. Test state must not leak between tests.
18. Test environments are separate from production.
19. Normal automated tests do not run against production data.
20. Heavy validation occurs in TEST before production deployment.
21. E2E and regression remain user-oriented.
22. Test code is maintained to production-quality standards.
23. Coverage is a diagnostic measure rather than a correctness guarantee.
24. CI is a safety net, not a replacement for developer testing discipline.
25. Deployment gates should be strong.
26. Completed features are protected by their automated test suite.
27. Tests should fail for the reason they were written to detect.
28. Difficult-to-test production code should trigger architectural examination before adding unnecessary test complexity.
29. Test readability is preferred over excessive abstraction.
30. A small amount of duplication is acceptable when it makes tests clearer.
31. Randomized data is used to broaden reasonable coverage, not to exhaustively explore every possible input.
32. The testing strategy should remain appropriate to the scale and purpose of LedgerLite.

---

# 38. Final Testing Architecture

The complete LedgerLite testing strategy is:

                         USER STORY
                              |
                              v
                         IMPLEMENTATION
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
           BACKEND            UI             E2E
              |               |               |
         +----+----+      +---+---+           |
         |         |      |       |           |
        Unit   Integration Unit Integration    |
         |         |      |       |           |
       pytest    pytest  Vitest  Vitest        |
                          RTL     RTL          |
                                  MSW          |
              |               |               |
              +---------------+---------------+
                              |
                              v
                          REGRESSION
                         E2E SUBSET
                              |
                              v
                       TEST ENVIRONMENT
                              |
              +---------------+---------------+
              |               |               |
         Performance        Load        Concurrency
                                              |
                                          Reliability
                              |
                              v
                       DEPLOYMENT GATE
                              |
                              v
                            PROD

The three environments are:

    DEV -> TEST -> PROD

The testing philosophy is:

    Unit
      -> deep and isolated

    Integration
      -> concrete component and data flow

    E2E
      -> complete user behavior

    Regression
      -> selected E2E protection for completed features

    Performance / Load / Concurrency / Reliability
      -> one focused E2E-level check each in TEST

The framework should be implemented incrementally around completed features rather than built as a large disconnected testing system before 
features exist.


A feature is complete when its behavior is implemented, appropriately tested, integrated, validated from the user's perspective, 
and protected by the required CI/deployment gates.
