# LedgerLite — Project Specification

---

# 1. Project Overview

## Purpose

LedgerLite is a multi-user expense tracking web application built as a structured backend engineering learning project.

The project is designed to provide hands-on experience with:

- Linux environments
- relational databases
- backend API development
- frontend integration
- authentication systems
- deployment workflows

The focus of the project is learning software engineering fundamentals through incremental development phases.

---

# 2. Final Product Vision

The final application should allow users to:

- create accounts
- log in securely
- add expenses
- edit expenses
- delete expenses
- view expense history
- filter expenses by category/date
- track spending totals

The application will run as a web application hosted inside a Linux VM.

---

# 3. Final Architecture

Frontend:
- HTML
- CSS
- Vanilla JavaScript

Backend:
- FastAPI

Database:
- SQLite (initial phases)
- PostgreSQL (final deployment phase)

Environment:
- Arch Linux VM

Architecture Flow:

Frontend → FastAPI Backend → Database

---

# 4. Technology Stack

## Backend
- FastAPI

## Database
- SQLite
- PostgreSQL

## Frontend
- HTML
- CSS
- Vanilla JavaScript

## Environment
- Arch Linux VM
- Python Virtual Environment
- Git

---

# 5. Project Principles

## Principle 1 — Finish Before Expanding
The MVP must be completed before adding advanced features.

## Principle 2 — Learn Fundamentals First
Core concepts should be understood before introducing abstractions or frameworks.

Examples:
- Raw SQL before ORM
- Linux fundamentals before deployment tooling

## Principle 3 — Every Phase Must Produce a Working Deliverable
Each phase must end with a usable output.

## Principle 4 — Simplicity Over Complexity
Avoid unnecessary technologies during MVP development.

The following are intentionally excluded from MVP scope:
- React
- Docker
- Kubernetes
- Microservices
- Redis
- Complex frontend frameworks

---

# 6. Functional Requirements

The application must support:

- user registration
- user login/logout
- add expenses
- edit expenses
- delete expenses
- view expenses
- filter expenses
- multi-user data isolation

---

# 7. Non-Functional Requirements

The application should:

- run on Linux VM
- expose REST APIs
- maintain user data integrity
- be maintainable and modular
- support future database migration
- support deployment to a hosted environment

---

# 8. Project Phases

---

# PHASE 0 — Planning & Architecture

## Objectives
- define project scope
- define technology stack
- define roadmap
- define learning goals
- establish project structure

## Deliverables
- PROJECT_SPEC.md
- Git repository setup
- development roadmap

---

# PHASE 1 — Database Foundations

## Goal
Build a fully functional relational database using SQLite while mastering SQL fundamentals and Linux environment setup.

---

## Environment Setup Objectives

### Arch Linux VM
- install barebones Arch Linux VM
- configure networking
- update system packages

### User Management
- create non-root development user
- configure sudo access
- explore `/etc/skel`
- understand Linux home directory initialization

### Development Environment
- install Git
- install SQLite
- create project directory structure

---

## Database Objectives

### SQLite Fundamentals
- install sqlite3
- create database manually
- understand SQLite file-based architecture

### Schema Design
Create:
- users table
- expenses table

Understand:
- primary keys
- foreign keys
- constraints
- normalization basics

### CRUD Operations
Practice:
- INSERT
- SELECT
- UPDATE
- DELETE

### Querying
Practice:
- filtering
- sorting
- aggregations
- joins

### Relationships
Understand:
- one-to-many relationships
- referential integrity

### Transactions
Understand:
- BEGIN
- COMMIT
- ROLLBACK

---

## Database Concepts To Master

### Core SQL
- CREATE TABLE
- ALTER TABLE
- DROP TABLE
- INSERT
- SELECT
- UPDATE
- DELETE

### Query Operations
- WHERE
- ORDER BY
- LIMIT
- LIKE
- BETWEEN
- IN

### Relationships
- PRIMARY KEY
- FOREIGN KEY
- INNER JOIN
- LEFT JOIN

### Constraints
- NOT NULL
- UNIQUE
- DEFAULT
- CHECK

### Database Design
- normalization basics
- avoiding duplicate data
- relational thinking

---

## Dummy Data Objectives

Create realistic test data including:
- multiple users
- multiple expense categories
- varied dates
- varied expense amounts

The database should support realistic querying scenarios.

---

## Phase 1 Deliverables

### Linux Deliverables
- fully configured Arch Linux VM
- non-root development user
- organized project structure

### Database Deliverables
- expenses.db
- working schema
- foreign key relationships
- dummy data
- CRUD query mastery
- working joins and aggregations

### Documentation Deliverables
- SQL query notes
- schema notes
- learning notes

---

# PHASE 2 — Backend Development

## Goals
- integrate FastAPI
- connect APIs to SQLite
- expose CRUD operations through REST APIs
- run application inside Linux VM
- access APIs from host machine

## Deliverables
- working FastAPI backend
- API endpoints
- database connectivity
- API testing workflow

---

# PHASE 3 — Frontend + Authentication

## Goals
- build frontend UI
- integrate backend APIs
- implement authentication
- implement protected routes

## Deliverables
- login page
- registration page
- expense dashboard
- JWT authentication
- frontend/backend integration

---

# PHASE 4 — PostgreSQL + Deployment

## Goals
- migrate SQLite → PostgreSQL
- prepare production-style deployment
- configure Linux services
- deploy application

## Deliverables
- PostgreSQL integration
- deployed application
- production-ready environment

---

# 9. MVP Success Criteria

The project is considered successful when:

- users can register and log in
- users can manage expenses
- data is stored persistently
- the application runs successfully on Linux VM
- the application is accessible through a browser
- all major components are fully integrated

---

# 10. Long-Term Optional Enhancements

Possible future enhancements:
- charts and analytics
- recurring expenses
- CSV export
- responsive mobile UI
- Docker support
- CI/CD pipelines
- HTTPS deployment
