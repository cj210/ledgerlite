# BUSINESS RULES

## Purpose

Define the business rules that govern LedgerLite behavior.

These rules describe validation, calculations, recurrence behavior, dashboard behavior, projections, and other business logic independently of implementation details.

---

# 1. User and Ownership Rules

### BR-001 — Entity Ownership

Every Category, Tag, Goal, and Financial Record belongs to exactly one User.

### BR-002 — User Data Isolation

A user must not be able to access, modify, or delete entities belonging to another user.

Ownership must be enforced by the application.

### BR-003 — Entity Name Uniqueness

Within a single user:

- Category names must be unique.
- Tag names must be unique.
- Goal names must be unique.

Different users may have entities with the same name.

### BR-004 — Starter Data

Starter Categories, Tags, and Goals may be created during user onboarding.

After onboarding, there is no distinction between starter data and user-created data.

---

# 2. Financial Record Rules

### BR-005 — Positive Amount

A Financial Record amount must be greater than zero.

Amounts support two decimal places.

### BR-006 — Optional Classification

A Financial Record may exist without:

- a Category
- a Tag
- a Goal

Incomplete classification must not prevent a valid Financial Record from being stored.

### BR-007 — Expense Inclusion

All valid Expense Financial Records contribute to spending calculations regardless of whether they are:

- categorized
- uncategorized
- tagged
- untagged
- associated with a goal
- not associated with a goal

### BR-008 — Record Type

The MVP supports only Expense Financial Records.

The transaction type concept remains part of the domain so that additional transaction types can be introduced in future versions.

---

# 3. Recurrence Rules

### BR-009 — Non-Recurring Record

A Financial Record with a NULL frequency is considered non-recurring.

### BR-010 — MVP Recurrence Frequencies

The MVP supports only:

- Monthly
- Yearly

Daily, weekly, and custom recurrence schedules are outside the MVP scope.

### BR-011 — Recurrence Information

Recurring Financial Records use:

- frequency
- due_month
- due_on
- end_date

### BR-012 — Monthly Recurrence

A monthly recurring Financial Record uses due_on to determine its scheduled day.

### BR-013 — Yearly Recurrence

A yearly recurring Financial Record uses due_month and due_on to determine its scheduled month and day.

### BR-014 — Day 31 Handling

If due_on is 31 and the current month does not contain a 31st day, the occurrence is scheduled for the last day of that month.

Examples:

- January → January 31
- February → last day of February
- April → April 30
- May → May 31

The stored due_on value remains 31.

### BR-015 — Recurrence End Date

The end_date of a recurring Financial Record is inclusive.

An occurrence may be expected on the end date.

Occurrences after the end date must not be expected.

### BR-016 — Recurrence and Transaction Date

The recurrence schedule and actual transaction date are independent.

Paying a recurring transaction earlier or later does not change its recurrence rule.

Example:

A recurring transaction may be scheduled for the 10th while the actual transaction_date is the 7th.

### BR-017 — Fixed/Variable Classification

The fixed/variable classification applies only to recurring Financial Records.

One-time Financial Records do not require fixed/variable classification.

### BR-018 — Fixed Recurring Amount

A fixed recurring transaction has a known expected amount.

### BR-019 — Variable Recurring Amount

A variable recurring transaction has a recurring schedule but its actual amount may vary.

---

# 4. Upcoming Recurring Payment Rules

### BR-020 — Current Month Occurrences

The dashboard must calculate which recurring Financial Records have an expected occurrence in the current month.

Monthly and yearly recurring records are handled consistently when determining the current month's expected payments.

### BR-021 — Expected Occurrence Date

The occurrence date is calculated from the recurring record's recurrence information.

The calculated occurrence date is the date displayed to the user.

### BR-022 — Upcoming Payment Ordering

Upcoming recurring payments are ordered by nearest expected occurrence date.

### BR-023 — Already Paid Occurrences

A recurring occurrence that has already been paid must be excluded from the upcoming recurring-payment list.

Payment status is determined from existing Financial Record data.

No separate payment-tracking table is required.

### BR-024 — Early Payment

A recurring payment may be paid before its scheduled due date.

The actual transaction_date records when it was paid.

The recurring schedule remains unchanged.

### BR-025 — Recurring Payment Matching

Existing Financial Records are used to determine whether the current recurring occurrence has already been paid.

Recurring transactions can be identified using their existing recurring information and transaction name.

### BR-026 — Paid Action

When the user selects Paid for an upcoming recurring payment:

1. A transaction-entry window is opened.
2. Known recurring information is pre-populated.
3. The user enters the remaining actual transaction information.
4. The Financial Record is saved.
5. The paid occurrence is excluded from the upcoming-payment list.

---

# 5. Dashboard Rules

### BR-027 — Dashboard Source of Truth

Dashboard information is computed from existing Financial Records.

Dashboard data must not be stored separately.

Financial Records remain the single source of truth.

### BR-028 — Current-Month Spending

Current-month spending is the sum of all Expense Financial Records whose transaction_date falls within the current month.

No classification requirement applies.

### BR-029 — Previous-Month Category Summary

The monthly category summary uses completed previous months.

The current month is represented separately through current-month transaction information.

### BR-030 — Category Spending Order

Category spending is calculated by summing Expense amounts for each Category.

Categories are displayed in decreasing order of spending.

### BR-031 — Uncategorized Spending

Uncategorized expenses must be included in the category spending summary.

Uncategorized spending must not be silently excluded.

The purpose is to make incomplete financial classification visible and encourage users to maintain cleaner data.

### BR-032 — Highest-Spending Category

The highest-spending category is the category with the greatest spending amount in the applicable period.

Uncategorized spending may be the highest-spending group.

---

# 6. Spending Trend Rules

### BR-033 — Trend Values

Applicable spending trends provide:

- Absolute difference
- Percentage difference

### BR-034 — Trend Difference

The absolute difference is calculated as:

difference = current_period - previous_period

### BR-035 — Trend Percentage

The percentage difference is calculated as:

percentage_difference = (difference / previous_period) × 100

### BR-036 — Monthly Comparison

The current period is compared with the previous month where applicable.

### BR-037 — Three-Month Trend

Three-month trends use the latest three months of available data.

### BR-038 — Limited History

When insufficient history exists:

- No history → explanatory state.
- One month → use the available month.
- Two months → use the available two months.
- Three or more months → use the latest three months.

### BR-039 — Trend Presentation

The backend provides numerical trend information.

The UI determines visual presentation.

For negative goals:

- decreasing spending → green
- increasing spending → red

---

# 7. Negative Goal Rules

### BR-040 — MVP Goal Type

The MVP supports only negative goals.

### BR-041 — Negative Goal Meaning

A negative goal represents an objective to reduce spending associated with that goal.

Examples:

- Quit Smoking
- Healthy Diet
- Reduce Dining Out

### BR-042 — Negative Goal Progress

For negative goals:

- decreasing spending represents positive progress
- increasing spending represents negative progress

### BR-043 — Goal Trend History

Goal trends use the same latest-three-month history philosophy:

- No history → explanatory state.
- One month → available data.
- Two months → available data.
- Three or more months → latest three months.

### BR-044 — Positive Goals

Positive goals are outside the MVP scope.

Positive goals may be introduced in a future version when additional transaction types such as savings are supported.

---

# 8. Recent Event Rules

### BR-045 — Recent Event Identification

The most recent event is identified using the Tag with the most recently updated updated_at value.

### BR-046 — Recent Event Transactions

The dashboard displays Financial Records associated with the most recent Tag.

### BR-047 — Recent Event Summary

The recent-event section includes a summary such as total spending associated with the event.

### BR-048 — Recent Event Trend

Trend calculations are not applied to the recent-event widget.

---

# 9. Recent Transaction Rules

### BR-049 — Current-Month Transactions

Recent Transactions represent Financial Records from the current month.

### BR-050 — Transaction Views

Users may switch between:

- All transactions
- Uncategorized transactions
- Untagged transactions

### BR-051 — Transaction Filters

Transactions may be filtered by:

- Category
- Tag
- Goal
- Date range

### BR-052 — Transaction Editing

Users may edit Financial Records and update their:

- Category
- Tag
- Goal
- other editable transaction information

### BR-053 — Data Cleanup

The dashboard should allow users to improve incomplete transaction classification.

Incomplete classification must remain visible rather than being hidden from dashboard information.

---

# 10. Projected Remaining Spending Rules

### BR-054 — Remaining Spending Projection

The dashboard estimates expected spending remaining in the current month.

The projection consists of:

Projected Remaining Spending =
Remaining Fixed Recurring Payments
+
Projected Variable Recurring Payments
+
Projected Other Spending

### BR-055 — Fixed Recurring Projection

Remaining fixed recurring payments use their exact expected recurring amounts.

### BR-056 — Variable Recurring Projection

Remaining variable recurring payments use historical averages.

### BR-057 — Other Spending Projection

Remaining non-recurring spending uses historical averages.

### BR-058 — No Double Counting

A Financial Record identified as part of recurring-payment calculations must not also be included in projected other spending.

A payment must therefore belong to only one projection category.

---

# 11. Historical Projection Rules

### BR-059 — Day-of-Month Comparison

Historical spending used for remaining-month projections is evaluated using the same day-of-month position.

For example, if today is August 8, historical data is evaluated from the 8th onward when estimating remaining spending.

### BR-060 — Projection History Availability

Historical projection behavior depends on available history:

- No historical months → explanatory state.
- One month → use exactly that month's available data.
- Two months → average the two available months.
- Three or more months → average the latest three months.

### BR-061 — Projection Simplicity

The remaining-spending projection is intentionally a simplified MVP estimate.

More sophisticated forecasting may be considered in future versions.

---

# 12. Business Data Integrity Rules

### BR-062 — Single Source of Truth

Financial Records are the source of truth for dashboard calculations.

Dashboard values must be calculated from Financial Records rather than stored separately.

### BR-063 — No Duplicate Spending

The same Financial Record must not contribute to multiple mutually exclusive projection categories.

### BR-064 — Complete Expense Inclusion

A valid Expense Financial Record must remain part of spending calculations even when classification information is incomplete.

---

# 13. MVP Business Scope

## Included in MVP

- User ownership and isolation
- Category management
- Tag/event management
- Negative goals
- Expense Financial Records
- Monthly recurrence
- Yearly recurrence
- Fixed recurring transactions
- Variable recurring transactions
- Recurrence end dates
- Current-month spending
- Previous-month category summaries
- Uncategorized spending
- Recent transactions
- Recent event spending
- Negative goal spending trends
- Monthly spending trends
- Three-month spending trends
- Upcoming recurring payments
- Paid recurring transactions
- Remaining-spending projection
- Historical average-based projections

## Not Included in MVP

- Income transactions
- Transfer transactions
- Savings transactions
- Investment transactions
- Positive saving goals
- Daily recurrence
- Weekly recurrence
- Custom recurrence schedules
- Advanced spending forecasting
- Separate dashboard-data storage
- Separate recurring-commitment storage
