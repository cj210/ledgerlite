# DOMAIN MODEL

## Purpose

Define the core business entities, concepts, relationships, and business rules of LedgerLite.

This document describes the business domain independently of database implementation details.

---

# User

Represents a person or business that owns financial data within LedgerLite.

Each user owns:

* Categories
* Tags
* Goals
* Financial Records

A user cannot access data belonging to another user.

Every business entity belongs to exactly one user.

---

# Category

Represents the type of a financial transaction.

Examples:

* Food
* Fuel
* Rent
* Entertainment

Categories answer the question:

> "What kind of transaction is this?"

A user cannot have multiple categories with the same name.

Different users may have categories with the same name.

Starter categories may be created during user onboarding.

After onboarding, there is no distinction between starter categories and user-created categories.

---

# Tag

Represents a named event to which financial records can be associated.

The Tag itself represents the event name; a financial record is "tagged" with that event.

Examples:

* Birthday Party
* Vacation 2026
* Diwali
* Wedding
* House Warming

Multiple financial records may share the same tag.

Tags may represent past or ongoing events.

Events are considered time-bound from a business perspective, but no separate event entity is required.

A user cannot have multiple tags with the same name.

Different users may have tags with the same name.

Starter tags may be created during user onboarding.

After onboarding, there is no distinction between starter tags and user-created tags.

---

# Goal

Represents a financial objective associated with financial records.

## MVP

LedgerLite MVP supports negative goals.

A negative goal represents an objective to reduce spending associated with that goal.

Examples:

* Quit Smoking
* Healthy Diet
* Reduce Dining Out

Financial records associated with a negative goal are used to measure spending against that goal over time.

For negative goals:

* Decreasing spending represents positive progress.
* Increasing spending represents negative progress.

The UI may represent positive progress using green and negative progress using red.

## Not Included in MVP

Positive goals are outside the MVP scope.

Positive goals represent objectives such as:

* Emergency Fund
* New Car
* House
* Vacation

These would involve saving money toward a target rather than reducing expenses.

Future versions may introduce additional goal types.

A user cannot have multiple goals with the same name.

Different users may have goals with the same name.

Starter goals may be created during user onboarding.

After onboarding, there is no distinction between starter goals and user-created goals.

---

# Financial Record

Represents a historical financial transaction.

A financial record belongs to exactly one user.

A financial record may optionally belong to:

* one Category
* one Tag
* one Goal

A financial record stores:

* transaction type
* name
* amount
* transaction date
* recorded date
* recurrence information
* fixed/variable information
* descriptive information

The amount must be greater than zero and supports two decimal places.

---

# Record Type

Defines the type of financial transaction.

## MVP

LedgerLite MVP supports:

* Expense

## Not Included in MVP

Future versions may support:

* Income
* Transfer
* Savings
* Investment

The transaction type concept remains part of the domain even when only Expense is supported by the MVP.

---

# Recurring Transactions

Recurring information is stored directly on Financial Records.

A separate RecurringCommitments entity/table is not used.

LedgerLite MVP supports two recurrence schedules:

* Monthly
* Yearly

Weekly, daily, and custom recurrence schedules are outside the MVP scope.

A financial record with:

frequency = NULL

is a non-recurring financial record.

Recurring information includes:

* frequency
* due_month
* due_on
* end_date

---

## Monthly Recurrence

A monthly recurring financial record uses:

* frequency = Monthly
* due_on

due_on represents the scheduled day of the month.

If due_on is 31 and the current month does not contain a 31st day, the occurrence is scheduled for the last day of that month.

Example:

January   → January 31
February  → Last day of February
April     → April 30
May       → May 31

The stored recurrence rule remains unchanged.

---

## Yearly Recurrence

A yearly recurring financial record uses:

* frequency = Yearly
* due_month
* due_on

due_month represents the scheduled month.

due_on represents the scheduled day within that month.

---

## Recurrence End Date

end_date defines the final date on which a recurring occurrence may be expected.

The end date is inclusive.

Example:

End date: August 5

August 5      → Expected
September 5   → Not expected

---

## Recurrence and Actual Transactions

The recurrence schedule and the actual transaction date are tracked independently.

Paying a recurring transaction earlier or later does not change its recurrence rule.

Example:

Recurring schedule:
Monthly
Due on: 10th

Actual payment:
Transaction date: 7th

The recurrence remains due on the 10th.

The actual Financial Record stores the actual transaction date of the payment.

---

# Fixed and Variable Recurring Transactions

Fixed/variable classification applies to recurring financial records.

It does not apply to one-time financial records.

## Fixed Recurring Transaction

A fixed recurring transaction has a known expected amount.

Example:

Monthly Rent
₹25,000
Fixed

The remaining expected amount is based on the known recurring amount.

## Variable Recurring Transaction

A variable recurring transaction occurs on a recurring schedule but its actual amount may vary.

Example:

Electricity Bill
Monthly
Variable

For dashboard projections, the expected remaining amount is estimated using historical data.

---

# Ownership Rules

Every Category, Tag, Goal, and Financial Record belongs to exactly one User.

Users cannot access entities belonging to another user.

Ownership must be enforced by the application.

---

# Entity Name Uniqueness

Within a single user:

* Category names must be unique.
* Tag names must be unique.
* Goal names must be unique.

Different users may have entities with the same name.

---

# Financial Record Classification

Financial records may be:

* Categorized or uncategorized.
* Tagged or untagged.
* Associated with a goal or not associated with a goal.

Incomplete classification does not prevent a financial record from being stored.

All valid Expense records contribute to spending calculations regardless of whether they have a Category, Tag, or Goal.

Uncategorized and untagged records remain visible in dashboard information.

This is intentional so that incomplete data encourages users to improve their financial data quality.

---

# Dashboard

Dashboard information is computed from Financial Records and is not stored separately.

Financial Records remain the single source of truth.

The dashboard may provide:

* Current-month spending
* Previous-month category summaries
* Highest-spending category
* Spending trends
* Goal progress
* Recent event spending
* Recent transactions
* Upcoming recurring payments
* Projected remaining spending

---

# Current-Month Spending

Current-month spending includes all Expense financial records whose transaction date falls within the current month.

Classification is not required.

Therefore:

* Categorized expenses are included.
* Uncategorized expenses are included.
* Tagged expenses are included.
* Untagged expenses are included.
* Goal-associated expenses are included.
* Expenses without goals are included.

---

# Monthly Category Summary

The monthly category summary uses completed previous months.

The current month is represented separately through recent/current-month transaction information.

Expenses are grouped by Category and ordered by total spending in decreasing order.

Uncategorized expenses are included in the summary.

This allows incomplete financial classification to remain visible to the user.

---

# Spending Trends

Applicable dashboard spending trends provide:

* Absolute difference.
* Percentage difference.

The comparison is between the current period and the previous period.

difference = current_period - previous_period

percentage_difference = (difference / previous_period) × 100

Three-month trends use the latest three months.

For users with limited history:

* No history → explanatory state.
* One month → use the available month.
* Two months → use the available two months.
* Three or more months → use the latest three months.

The backend provides the numerical trend information.

The UI determines visual presentation such as green or red.

---

# Negative Goal Progress

For MVP negative goals, spending associated with the goal is analyzed over time.

The goal trend uses the same latest-three-month philosophy:

* No history → explanatory state.
* One month → available data.
* Two months → available data.
* Three or more months → latest three months.

For negative goals:

Spending decreases → Positive progress

Spending increases → Negative progress

---

# Recent Event

The most recent event is determined by the most recently updated Tag.

The dashboard displays the financial records associated with that Tag.

The recent-event section may include a summary such as total spending associated with the event.

Trend calculations are not applied to the recent-event widget.

---

# Recent Transactions

The dashboard displays recent transactions from the current month.

Users may view and manage transaction classification from this area.

Supported views include:

* All transactions
* Uncategorized transactions
* Untagged transactions

Transactions may be filtered by:

* Category
* Tag
* Goal
* Date range

Users may edit financial records and update their Category, Tag, Goal, and other editable information.

The purpose is both transaction visibility and maintaining clean financial data.

---

# Upcoming Recurring Payments

The dashboard displays expected recurring payments for the current month.

Monthly and yearly recurrence types are treated consistently by the dashboard.

The dashboard presents the calculated occurrence date for the current month.

Payments are ordered by nearest due date.

Already-paid occurrences are excluded.

When a recurring payment is identified as already paid, it is determined from existing Financial Record data rather than a separate payment-tracking table.

---

# Paying a Recurring Transaction

Each upcoming recurring payment may provide a Paid action.

When the user selects Paid:

1. The transaction-entry window opens.
2. Known recurring information is pre-populated.
3. The user enters the remaining actual transaction information.
4. The actual Financial Record is saved.
5. The occurrence is then excluded from the upcoming recurring-payment list.

Paying a recurring transaction earlier than its scheduled date changes the actual transaction date but does not change the recurring schedule.

---

# Projected Remaining Spending

The dashboard estimates expected spending remaining in the current month.

The projection consists of:

Projected Remaining Spending =
Remaining Fixed Recurring Payments
+
Projected Variable Recurring Payments
+
Projected Other Spending

## Fixed Recurring Payments

Remaining fixed recurring payments use their exact expected recurring amounts.

## Variable Recurring Payments

Remaining variable recurring payments use historical averages.

## Other Spending

Other expected spending uses historical averages from non-recurring spending.

A payment already classified as a recurring payment is excluded from other spending so that it is not counted twice.

---

# Historical Projection Rules

Historical averages use the same day-of-month position when estimating the remaining portion of the current month.

Example:

If today is the 8th, historical data is evaluated from the 8th onward when estimating remaining spending.

History availability:

* No historical months → explanatory state.
* One month → use exactly that month's available data.
* Two months → average the two available months.
* Three or more months → average the latest three months.

The projection is intentionally a simplified MVP estimate.

More sophisticated forecasting may be considered in future versions.

---

# Dashboard Data Integrity

Dashboard calculations must not duplicate spending.

A financial record identified as a recurring payment belongs to the recurring calculation and must not also be included in projected other spending.

All dashboard calculations derive from the existing Financial Record data.

No dashboard-specific data is persisted.

---

# Business Relationship Summary

User
├── Category
├── Tag
├── Goal
└── Financial Record

Financial Record
├── Category (optional)
├── Tag (optional)
└── Goal (optional)

Financial Record
├── Record Type
├── Recurrence information (optional)
├── Fixed/Variable information (for recurring records)
└── Transaction information

Dashboard
└── Computed from Financial Records

---

# MVP Scope Summary

## Included in MVP

* User ownership and isolation
* Categories
* Tags/events
* Negative goals
* Expense financial records
* Monthly recurring transactions
* Yearly recurring transactions
* Fixed recurring transactions
* Variable recurring transactions
* Recurrence end dates
* Current-month spending
* Previous-month category summaries
* Uncategorized spending
* Recent transactions
* Recent event spending
* Goal spending trends
* Monthly and three-month spending trends
* Upcoming recurring payments
* Paid recurring transactions
* Remaining-spending projection
* Historical average-based projections

## Not Included in MVP

* Income transactions
* Transfer transactions
* Savings transactions
* Investment transactions
* Positive saving goals
* Daily recurrence
* Weekly recurrence
* Custom recurrence schedules
* Advanced spending forecasting
* Separate dashboard-data storage
* Separate recurring-commitment storage

