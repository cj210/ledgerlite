# Frontend Architecture

## Purpose

The LedgerLite frontend is designed as an independent application within the main repository.

Its architecture prioritizes:

- Clear separation of responsibilities
- Minimal unnecessary dependencies
- Stable boundaries between frontend and backend
- Flexibility to evolve as requirements change

---

## Application Structure

The frontend lives in the `ui/` directory.

The initial application structure is:

    ui/
    └── src/
        ├── components/
        ├── pages/
        ├── api/
        ├── utils/
        ├── App.jsx
        └── main.jsx

### Pages

Pages represent application screens or routes.

### Components

Components represent reusable UI building blocks with a clear responsibility.

Components should be extracted when there is actual reuse, shared behaviour, or a clear responsibility rather than for hypothetical future reuse.

### API

The API layer handles communication with the LedgerLite backend.

### Utils

Utilities contain UI-independent helper functions.

The structure may evolve as the application grows. New layers or folders should be introduced when actual complexity requires them.

---

## State Management

State is kept as close as practical to the components that use it.

The default approach is:

1. Keep state local to a component.
2. Lift state to the nearest common parent when multiple components require it.
3. Introduce global state management only when the application demonstrates a genuine need.

Performance optimizations will be driven by observed problems rather than introduced prematurely.

---

## Frontend–Backend Boundary

The frontend and backend share the LedgerLite domain but have separate responsibilities.

The frontend communicates with the backend through the defined API contract and does not depend on the backend's internal implementation.

The API contract is treated as a stable boundary:

    Frontend
       │
       │ API Contract
       ▼
    Backend

Internal changes in either application should, whenever possible, be resolved without changing the API contract.

Both applications are responsible for maintaining alignment with the contract.

---

## Architectural Evolution

The frontend will evolve as LedgerLite grows.

We prefer:

    Simple structure + clear boundaries + deliberate evolution

over:

    Complexity introduced for hypothetical future requirements

New libraries, abstractions, or architectural layers should be introduced when a concrete requirement justifies them.
