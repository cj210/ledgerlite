# LedgerLite

## Overview

Individuals and small organizations often record financial trasactions across different mediums such as notebooks, spreadsheets, or disconnected applications. The mediums are not effective when it comes to analyzing the data. They need more manual efforts in order to analyze the data and use it for decision making. 

Over time, this creates challenges in:

- Tracking financial trasactions consistently
- Organizing data into categories
- Understanding spending  and saving patterns
- Generating useful financial insights

LedgerLite provides a centralized platform to record, organize, analyze, report and forecast expenses, enabling users to make informed financial and strategic decisions.


## Features

The core features are:
1. Tracking finacial transactions like expenses, savings, transfers etc.
2. Organizing transactions into different categories and types like fixed, recurring etc.
3. Tracking due dates and payments left on recurring payments like loans and EMIs.
4. Filtering transactions as per different events in life and specific user targets.
5. Periodic reports on summary of transactions.
6. Reminders and notifications on future recurring transactions.
7. Dashboard that consolidated recent transactions and near future expected transactions.


## Architecture

LedgerLite follows a three-layer application architecture:

### Design Principle: Each layer has a single responsibility and communicates only with the adjacent layer.

User (Individual / Small scale business)
        |
        |
Frontend Layer
(HTML + CSS + JavaScript)
        |
        |
Backend Layer
(FastAPI REST API)
        |
        |
Data Layer
(SQLite - Initially, PostgreSQL Database - Planned)


### Component Responsibilities

#### Frontend Responsibilities:
- Capture user input
- Display financial information
- Present reports and dashboards
- Communicate with backend APIs

#### Backend Responsibilities:
- Business logic
- API endpoints
- Input validation
- Expense processing
- Authentication and authorization
- Data acess
- Report generation

#### Database Responsibilities:
- Store application data
- Maintain relationships
- Preserve date integrity
- Support reports and analysis



## Getting Started
- Clone the repo
- Check docs/03-development-environment.md to check for machine and project level software requirements.
- Run scripts/bootstrap.sh for environment setup.
You can start contributing.

## Project Structure
Please refer to docs/04-project-structure.md

## Development Setup
Please refer to docs/03-develpment-environment.md

## Documentation
This project is well documented. All related files are located in docs directory.

## Roadmap
Please refer to docs/00-roadmap.md

## Contributing
Contributors list:
1. Kalicharan


License 
Free to clone, download and publish.
