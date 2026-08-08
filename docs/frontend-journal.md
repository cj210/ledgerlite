# FRONTEND ENGINEERING JOURNAL

This journal records the frontend engineering learning journey while building LedgerLite.

The purpose is not to document only what was implemented. Each entry records what was learned, why technical decisions were made, what concepts were understood, and how the work contributes toward becoming an independent full-stack engineer.

LedgerLite is the vehicle for learning. The objective is broader than learning React or completing a single application.

---

## Date

2026-08-08

## Objective

Establish the frontend development environment and understand the fundamental execution model of a React application before beginning LedgerLite UI development.

The objective was intentionally focused on understanding the technology rather than immediately building application screens.

---

## Completed

* Created the frontend application under `ui/`.
* Scaffolded a React + TypeScript application using Vite.
* Installed frontend dependencies using npm.
* Confirmed Node.js and npm availability.
* Started the Vite development server.
* Configured Vite to listen on `0.0.0.0` so the application could be accessed from the host machine's browser while development occurs inside the VM.
* Confirmed the React application loads successfully in the host browser.
* Examined the generated frontend project structure.
* Examined `package.json`.
* Examined the generated `.gitignore`.
* Examined `index.html`.
* Examined `main.tsx`.
* Examined `App.tsx`.
* Established the distinction between development tooling and the running application.
* Established the distinction between Vite and React responsibilities.
* Understood the purpose of HMR.
* Established the basic React state and re-rendering model.
* Established where the browser DOM exists and where React executes.

---

# Development Environment

The frontend is being developed inside the LedgerLite development VM.

The VM does not have a browser, so the Vite development server must listen on all interfaces:

```bash
npm run dev -- --host 0.0.0.0
```

The application can then be accessed from the host machine's browser using the VM's IP address and port `5173`.

The development flow is therefore:

```text
Host Browser
     ↓
VM Network
     ↓
Vite Development Server
     ↓
React Application
```

This establishes the basic development environment required for frontend work.

---

# Frontend Project Structure

The initial Vite project contains:

```text
ui/
├── eslint.config.js
├── .gitignore
├── index.html
├── package.json
├── package-lock.json
├── public/
├── src/
│   ├── App.css
│   ├── App.tsx
│   ├── index.css
│   └── main.tsx
├── tsconfig.app.json
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

The project can broadly be understood as:

```text
Project configuration
    │
    ├── package.json
    ├── vite.config.ts
    ├── tsconfig*.json
    └── eslint.config.js
    │
    ▼
Application code
    │
    └── src/
```

The `src/` directory will eventually contain the LedgerLite frontend application.

---

# npm Scripts

The generated `package.json` contains:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  }
}
```

The scripts provide different development and production operations.

### Development

```bash
npm run dev
```

Starts the Vite development server.

### Production Build

```bash
npm run build
```

Runs TypeScript compilation/type checking and then creates a production build using Vite.

### Linting

```bash
npm run lint
```

Runs ESLint against the project.

### Preview

```bash
npm run preview
```

Allows the generated production build to be previewed locally.

---

# Dependencies vs Development Dependencies

The project separates runtime application dependencies from development tooling.

Runtime dependencies currently include:

```text
react
react-dom
```

Development dependencies include tools such as:

```text
typescript
vite
eslint
@vitejs/plugin-react
typescript-eslint
```

The distinction established is:

```text
dependencies
    ↓
Required by the application

devDependencies
    ↓
Primarily required to develop, validate, and build the application
```

---

# package.json vs package-lock.json

`package.json` declares the project's dependencies and scripts.

`package-lock.json` records the dependency tree resolved by npm.

The distinction is:

```text
package.json
    ↓
What the project declares

package-lock.json
    ↓
What npm resolved
```

`node_modules/` is generated from these files and is not committed to Git.

---

# Linting

ESLint was identified as a code-quality tool rather than simply a formatting tool.

The distinction established is:

```text
TypeScript
    ↓
Checks type correctness

ESLint
    ↓
Checks code-quality rules and problematic patterns

Formatter
    ↓
Handles consistent formatting
```

Formatting and linting are therefore related but separate concerns.

A dedicated formatter may be considered later if required by the project.

---

# Git Ignore Rules

The generated frontend `.gitignore` currently ignores frontend-generated or machine-specific files including:

```text
node_modules
dist
dist-ssr
*.local
logs
editor-specific files
OS-specific files
```

The most important frontend rules are:

```text
node_modules
dist
dist-ssr
*.local
```

`node_modules` is reproducible from the package manifests and therefore should not be committed.

`dist` and `dist-ssr` are build artifacts that can be regenerated using the production build.

The frontend `.gitignore` applies to the frontend project scope and does not replace repository-level ignore rules.

---

# HTML and the React Application

The generated `index.html` was examined.

Its important structure is:

```html
<body>
  <div id="root"></div>
  <script type="module" src="/src/main.tsx"></script>
</body>
```

`index.html` is the HTML shell of the application.

It provides the initial document and the root element into which React mounts the application.

HTML is therefore not replaced by React.

Instead:

```text
HTML
    ↓
Provides the document/container

React + JSX/TSX
    ↓
Describes the application UI

CSS
    ↓
Styles the UI

JavaScript/TypeScript
    ↓
Provides application behavior
```

The application will continue to depend on HTML even though most application UI markup will eventually be written as JSX/TSX inside React components.

---

# React Application Execution Flow

The most important execution model established today is:

```text
Browser requests index.html
            ↓
index.html creates <div id="root">
            ↓
index.html loads main.tsx
            ↓
Vite transforms/serves the development module
            ↓
main.tsx starts React
            ↓
React connects to #root
            ↓
React renders <App />
            ↓
App.tsx describes the UI
            ↓
React updates the browser DOM
            ↓
Browser displays the UI
```

The important relationship between the files is:

```text
index.html
    ↓
main.tsx
    ↓
App.tsx
```

`main.tsx` is effectively the entry point connecting React to the browser document.

`App.tsx` is the initial React component.

---

# Browser DOM

An important distinction was established:

**React does not have a separate browser DOM.**

The browser maintains the actual DOM in memory.

The browser's DOM is therefore part of the browser process running on the host machine.

In the current development environment:

```text
VM
 └── Linux
      └── Vite
           │
           │ serves/transforms application
           ▼
Host Machine
 └── Browser
      ├── React JavaScript
      ├── React state
      └── Browser DOM
```

React executes inside the browser once the application has been loaded.

The VM's Vite server does not maintain the browser's DOM.

---

# React Rendering Model

The generated application introduced React state through:

```tsx
const [count, setCount] = useState(0)
```

The following mental model was established:

```text
count
    ↓
Current state value

setCount
    ↓
Function used to update the state

0
    ↓
Initial state value
```

When the user clicks the generated counter:

```tsx
setCount((count) => count + 1)
```

React updates the state and renders the component again.

The resulting flow is:

```text
User clicks
    ↓
React event handler runs
    ↓
setCount()
    ↓
React state changes
    ↓
React renders the component again
    ↓
{count} receives the new value
    ↓
React updates the required DOM
    ↓
Browser displays the updated UI
```

A critical distinction was established:

```text
React re-render
    ≠
Browser refresh
```

A React re-render means React evaluates the component's UI representation again.

It does not mean the browser reloads the entire page.

---

# Declarative UI

The difference between traditional imperative DOM manipulation and React's model was introduced.

Traditional DOM manipulation might explicitly instruct the browser:

```text
Find this element.
Change its text.
Add this class.
Hide that element.
```

React instead allows the developer to describe the desired UI in terms of state:

```text
State
  ↓
What should the UI look like?
  ↓
React determines the required DOM changes
```

This is the beginning of the declarative UI mental model.

The developer generally changes application state rather than manually manipulating individual DOM elements.

---

# Vite vs React

The distinction between Vite and React was established.

### Vite

Vite is primarily the development/build tool.

During development it provides:

```text
Development server
Module transformation/serving
HMR
```

During production preparation it creates optimized browser-ready assets.

### React

React is the UI library/framework layer responsible for:

```text
Components
State
Rendering
UI updates
Event handling
```

The distinction can be summarized as:

```text
Code change
    ↓
Vite / HMR

User interaction
    ↓
React
```

Vite does not update application state when the user clicks a button.

React does.

---

# HMR

HMR means:

**Hot Module Replacement**

It is a development feature provided by the development toolchain.

When a source module changes:

```text
Edit App.tsx
    ↓
Save
    ↓
Vite detects the change
    ↓
HMR
    ↓
Updated module reaches the browser
    ↓
Running application updates
```

HMR avoids the need for a full browser refresh during development.

HMR is a development convenience and is not part of the deployed production application.

---

# Development vs Production

A major distinction was established between development and production.

## Development

```text
.tsx / .ts / CSS
       ↓
Vite development server
       ↓
Browser
       ↓
React runs
```

Vite remains actively involved during development.

## Production

The production build is created using:

```bash
npm run build
```

The process is approximately:

```text
Source code
    ↓
TypeScript checking/compilation
    ↓
Vite production build
    ↓
dist/
    ↓
Deploy generated assets
    ↓
Browser
```

The browser receives browser-ready JavaScript, CSS, HTML, and other assets.

The production browser does not require the Vite development server or TypeScript compiler to be running.

React's production JavaScript remains part of the application.

---

# Key Mental Models Established

The following concepts were understood during this session:

### Frontend execution

```text
index.html
    ↓
main.tsx
    ↓
React
    ↓
App.tsx
    ↓
Browser DOM
    ↓
Screen
```

### Development feedback loop

```text
Edit source
    ↓
Vite
    ↓
HMR
    ↓
Browser
```

### React interaction loop

```text
User interaction
    ↓
Event handler
    ↓
State update
    ↓
React re-render
    ↓
DOM update
    ↓
Screen update
```

### Production flow

```text
Source
    ↓
Build
    ↓
dist/
    ↓
Deploy
    ↓
Browser
```

---

# Lessons Learned

* Vite development server and Vite production build are different parts of the development lifecycle.
* The browser does not execute TypeScript directly.
* Vite transforms/serves source modules during development and produces browser-ready assets during a production build.
* `npm run build` is not the same thing as `npm run dev`.
* ESLint is primarily a code-quality tool rather than simply a formatting tool.
* React is not TypeScript; `useState` is a React API.
* React does not maintain a separate browser DOM.
* The browser maintains the actual DOM in memory.
* React executes inside the browser once the application is loaded.
* The VM runs Vite, while the host browser runs the frontend application.
* `index.html` is still part of a React application.
* `index.html` provides the root element into which React mounts.
* `main.tsx` connects React to the browser document.
* `App.tsx` is a React component that describes UI.
* React re-rendering is different from a browser refresh.
* A React state update can cause the existing DOM to be updated without reloading the page.
* HMR means Hot Module Replacement.
* HMR is a development feature and is not required by the deployed production application.
* `node_modules` is generated and should not be committed.
* `dist` is a generated production artifact and should not be committed.
* Application state currently exists in browser memory and therefore resets when the application is refreshed.
* Persistent LedgerLite data will eventually live in the backend/database rather than temporary React state.

---

# Reflection

Today's session deliberately focused on understanding the frontend execution model rather than immediately building LedgerLite screens.

This was important because the objective of the frontend journey is not simply to learn React syntax.

The broader objective is to become capable of reasoning about a full-stack application.

The first important distinction was between the development environment and the application itself.

Vite is responsible for the development/build workflow, while React is responsible for the application's UI model.

The second important distinction was between React re-rendering and browser refreshing.

A browser page remains alive after its initial load. JavaScript can change the existing DOM while the page is running. React uses this capability to update the UI when application state changes.

The VM-based development environment also clarified where different parts of the system execute.

Vite currently runs inside the development VM, while the React application executes inside the host browser.

This mental model will become important when the frontend is eventually connected to the FastAPI backend.

The frontend therefore now has a working development foundation and an initial conceptual foundation.

---

# Next Session

Continue with the React fundamentals required before beginning LedgerLite UI implementation.

Focus on:

* JSX
* React components
* How JSX relates to HTML
* Component composition
* Props
* State
* Event handling
* Rendering
* Basic component structure

The next conceptual boundary is:

```text
React Component
    ↓
JSX
    ↓
React rendering
    ↓
Browser DOM
```

After the fundamental React model is understood, begin applying it to the LedgerLite frontend architecture.

---

# Frontend Journey Principle

The frontend should be learned as an engineering discipline rather than as a collection of React syntax or tutorials.

LedgerLite is the practical vehicle.

The target is not:

```text
Learn React
    ↓
Finish LedgerLite
```

The target is:

```text
Learn frontend engineering
        +
Build real applications
        +
Understand architectural decisions
        +
Integrate with backend systems
        +
Test and maintain the frontend
        ↓
Become an independent full-stack engineer
```

