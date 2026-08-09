# PROJECT STORIES

## Purpose

Define the user-facing capabilities of LedgerLite.

Project stories describe what users should be able to accomplish with LedgerLite and why those capabilities are valuable.

Stories are grouped by functional area and marked according to MVP scope.

---

# 1. User and Onboarding

## US-001 — Create an Account

**Priority:** MVP

As a user, I want to create a LedgerLite account so that I can maintain my own financial data.

### Expected Outcome

- A user account is created.
- The user's financial data belongs exclusively to that user.

---

## US-002 — Start With Useful Default Data

**Priority:** MVP

As a new user, I want LedgerLite to provide starter categories, tags, and goals so that I can begin recording transactions without configuring everything first.

### Expected Outcome

- Starter data is available after onboarding.
- Starter data behaves exactly like user-created data after onboarding.

---

# 2. Category Management

## US-003 — Create a Category

**Priority:** MVP

As a user, I want to create categories so that I can organize my expenses by type.

### Examples

- Food
- Fuel
- Rent
- Entertainment

### Expected Outcome

- A category name must be unique within the user's categories.
- Different users may have categories with the same name.

---

## US-004 — Edit a Category

**Priority:** MVP

As a user, I want to edit a category so that I can keep my financial classification accurate.

### Expected Outcome

- The category name must remain unique within the user's categories.

---

## US-005 — View Categories

**Priority:** MVP

As a user, I want to view my categories so that I can select them when recording or editing transactions.

---

# 3. Tag and Event Management

## US-006 — Create an Event Tag

**Priority:** MVP

As a user, I want to create a named event and use it as a tag so that I can associate multiple transactions with that event.

### Examples

- Birthday Party
- Vacation 2026
- Diwali
- Wedding

### Expected Outcome

- A tag name must be unique within the user's tags.
- Different users may have tags with the same name.

---

## US-007 — Edit an Event Tag

**Priority:** MVP

As a user, I want to edit an event tag so that I can maintain accurate event information.

### Expected Outcome

- The tag name must remain unique within the user's tags.

---

## US-008 — View Event Tags

**Priority:** MVP

As a user, I want to view my event tags so that I can associate transactions with the appropriate event.

---

# 4. Goal Management

## US-009 — Create a Negative Goal

**Priority:** MVP

As a user, I want to create a goal focused on reducing a particular type of spending so that I can monitor whether my spending is moving in the desired direction.

### Examples

- Quit Smoking
- Healthy Diet
- Reduce Dining Out

### Expected Outcome

- A goal name must be unique within the user's goals.
- Different users may have goals with the same name.

---

## US-010 — Edit a Goal

**Priority:** MVP

As a user, I want to edit a goal so that I can keep my financial objectives accurate.

### Expected Outcome

- The goal name must remain unique within the user's goals.

---

## US-011 — View Goals

**Priority:** MVP

As a user, I want to view my goals so that I can associate relevant transactions with them.

---

## US-012 — Track Goal Spending

**Priority:** MVP

As a user, I want to see spending associated with a goal over time so that I can determine whether I am reducing the expense.

### Expected Outcome

For negative goals:

- Decreasing spending indicates positive progress.
- Increasing spending indicates negative progress.

---

## US-013 — Create a Positive Saving Goal

**Priority:** Future

As a user, I want to create a positive saving goal so that I can track money saved toward a financial objective.

### Examples

- Emergency Fund
- New Car
- House
- Vacation

---

# 5. Financial Record Management

## US-014 — Record an Expense

**Priority:** MVP

As a user, I want to record an expense so that LedgerLite can track my spending.

### Expense Information May Include

- Name
- Amount
- Transaction date
- Category
- Tag
- Goal
- Description
- Recurrence information

### Expected Outcome

- The expense amount must be greater than zero.
- Amounts support two decimal places.

---

## US-015 — Record an Incomplete Expense

**Priority:** MVP

As a user, I want to record an expense even when I have not yet assigned a category, tag, or goal so that I do not have to complete all classification before saving the transaction.

### Expected Outcome

Incomplete transactions remain part of LedgerLite's spending data.

---

## US-016 — Edit an Expense

**Priority:** MVP

As a user, I want to edit an expense so that I can correct or improve my financial data.

---

## US-017 — Categorize an Existing Expense

**Priority:** MVP

As a user, I want to assign a category to an existing expense so that my spending analysis becomes more accurate.

---

## US-018 — Tag an Existing Expense

**Priority:** MVP

As a user, I want to assign an event tag to an existing expense so that I can analyze spending associated with that event.

---

## US-019 — Associate an Expense With a Goal

**Priority:** MVP

As a user, I want to associate an expense with a goal so that the expense contributes to that goal's spending analysis.

---

## US-020 — Filter Transactions

**Priority:** MVP

As a user, I want to filter transactions by category, tag, goal, and date range so that I can investigate specific parts of my financial history.

---

## US-021 — View Uncategorized Transactions

**Priority:** MVP

As a user, I want to view my uncategorized expenses so that I can identify and classify incomplete financial data.

---

## US-022 — View Untagged Transactions

**Priority:** MVP

As a user, I want to view my untagged expenses so that I can identify transactions that are not associated with an event.

---

# 6. Recurring Transactions

## US-023 — Create a Recurring Transaction

**Priority:** MVP

As a user, I want to mark a transaction as recurring so that LedgerLite can identify future expected payments.

### MVP Frequencies

- Monthly
- Yearly

### Expected Outcome

LedgerLite calculates the expected occurrence date according to the recurrence rules.

If a recurring transaction is scheduled for the 31st and the current month does not contain a 31st, the occurrence is scheduled for the last day of that month.

---

## US-024 — Define a Fixed Recurring Transaction

**Priority:** MVP

As a user, I want to mark a recurring transaction as fixed so that LedgerLite knows its expected amount.

### Example

Monthly Rent — ₹25,000

---

## US-025 — Define a Variable Recurring Transaction

**Priority:** MVP

As a user, I want to mark a recurring transaction as variable so that LedgerLite can estimate its future amount using historical spending.

### Example

Electricity Bill

---

## US-026 — Define a Recurring Transaction End Date

**Priority:** MVP

As a user, I want to specify when a recurring transaction ends so that LedgerLite stops expecting it after that date.

### Expected Outcome

The end date is inclusive.

A recurring occurrence may be expected on the end date but not after it.

---

## US-027 — Pay an Expected Recurring Transaction

**Priority:** MVP

As a user, I want to mark an expected recurring payment as Paid so that I can record the actual transaction.

### Expected Outcome

- A transaction-entry window opens.
- Known recurring information is pre-populated.
- I enter the remaining transaction information.
- The actual transaction is saved.
- The payment disappears from the upcoming recurring-payment list.

---

## US-028 — Pay a Recurring Transaction Early

**Priority:** MVP

As a user, I want to record a recurring payment before its scheduled date so that LedgerLite reflects when I actually paid it.

### Expected Outcome

- The actual transaction date records when the payment was made.
- The recurring schedule remains unchanged.
- The recurring payment is no longer shown as unpaid for that occurrence.

---

# 7. Dashboard

## US-029 — View a Financial Dashboard

**Priority:** MVP

As a user, I want a dashboard that summarizes my financial activity so that I can understand my spending without manually analyzing every transaction.

---

## US-030 — View Current-Month Spending

**Priority:** MVP

As a user, I want to see how much I have spent during the current month so that I can understand my current spending level.

---

## US-031 — Identify the Highest-Spending Category

**Priority:** MVP

As a user, I want the dashboard to highlight my highest-spending category so that I can quickly identify where most of my money is going.

---

## US-032 — View Monthly Category Spending

**Priority:** MVP

As a user, I want to see my monthly spending grouped by category so that I can understand where my money is being spent.

### Expected Outcome

- Categories are ordered from highest spending to lowest spending.
- Uncategorized spending is included.

---

## US-033 — View Spending Trends

**Priority:** MVP

As a user, I want to see how my spending is changing compared with previous periods so that I can identify whether my spending is increasing or decreasing.

### Expected Information

- Difference
- Percentage difference

### Trend History

- When three or more months of history are available, the latest three months are used.
- When less than three months of history are available, the available history is used.
- A new user with no relevant history receives an explanatory state rather than a misleading trend.

---

## US-034 — View Goal Progress on the Dashboard

**Priority:** MVP

As a user, I want to see the progress of my negative goals on the dashboard so that I can quickly understand whether I am reducing the targeted spending.

### Expected Outcome

- The goal trend follows the same available-history and latest-three-month approach used by spending trends.
- Decreasing spending represents positive progress.
- Increasing spending represents negative progress.

---

## US-035 — View the Most Recent Event

**Priority:** MVP

As a user, I want to see spending associated with my most recently updated event so that I can quickly review my latest event-related expenses.

### Expected Outcome

- The most recently updated event is identified using the event tag's latest update.
- Transactions associated with that event are displayed.
- A summary of the event's spending may be displayed.

---

## US-036 — View Recent Transactions

**Priority:** MVP

As a user, I want to see my recent transactions so that I can quickly review my latest spending activity.

### Expected Outcome

Recent transactions represent transactions from the current month.

---

## US-037 — Clean Financial Data From the Dashboard

**Priority:** MVP

As a user, I want to edit and classify transactions directly from the dashboard so that I can improve the quality of my financial data while reviewing my analytics.

---

# 8. Upcoming Payments

## US-038 — View Expected Payments

**Priority:** MVP

As a user, I want to see recurring payments expected during the current month so that I know what expenses are coming up.

### Expected Outcome

- Monthly and yearly recurring transactions are shown together.
- Payments are ordered by nearest expected date.
- Already-paid occurrences are excluded.
- Expected dates are calculated according to the recurring transaction rules.

---

## US-039 — View Remaining Spending Projection

**Priority:** MVP

As a user, I want to see how much I am expected to spend for the remainder of the month so that I can understand my likely total spending.

### Projection Includes

- Exact remaining fixed recurring payments.
- Estimated remaining variable recurring payments.
- Estimated remaining non-recurring spending.

### Expected Outcome

Recurring payments must not be counted again as other projected spending.

---

## US-040 — Understand Projection History

**Priority:** MVP

As a user, I want the remaining-spending projection to improve as LedgerLite collects more historical data so that the estimate becomes more useful over time.

### Expected Behavior

- Historical spending is evaluated from the corresponding day-of-month onward.
- No historical months → explanatory state.
- One month → use exactly that month's available data.
- Two months → average the available months.
- Three or more months → average the latest three months.

---

# 9. Financial Analysis

## US-041 — Review Spending by Goal

**Priority:** MVP

As a user, I want to review expenses associated with a goal so that I can understand how much I am spending toward the behavior I want to change.

---

## US-042 — Review Spending by Event

**Priority:** MVP

As a user, I want to review all transactions associated with an event so that I can understand the total cost of that event.

---

## US-043 — Review Spending by Date Range

**Priority:** MVP

As a user, I want to review spending within a specific date range so that I can analyze a particular period.

---

## US-044 — Review Spending by Category

**Priority:** MVP

As a user, I want to review spending for a specific category so that I can understand how much I spend on that type of expense.

---

# 10. Future Transaction Types

## US-045 — Record Income

**Priority:** Future

As a user, I want to record income so that LedgerLite can provide a broader view of my financial activity.

---

## US-046 — Record Transfers

**Priority:** Future

As a user, I want to record transfers so that movement of money between accounts can be represented accurately.

---

## US-047 — Record Savings

**Priority:** Future

As a user, I want to record savings transactions so that I can track money saved toward positive goals.

---

## US-048 — Record Investments

**Priority:** Future

As a user, I want to record investment transactions so that I can track investment-related financial activity.

---

# 11. Future Recurrence

## US-049 — Support Additional Recurrence Patterns

**Priority:** Future

As a user, I want to configure additional recurrence patterns so that LedgerLite can represent financial commitments beyond monthly and yearly schedules.

### Possible Future Patterns

- Daily
- Weekly
- Custom intervals

---

# MVP Summary

The MVP should allow a user to:

1. Create and manage categories.
2. Create and manage event tags.
3. Create and manage negative spending-reduction goals.
4. Record expenses.
5. Record incomplete expenses.
6. Edit and classify existing expenses.
7. Filter transactions.
8. Create monthly and yearly recurring transactions.
9. Mark recurring transactions as fixed or variable.
10. Record recurring payments when they are paid.
11. View current-month spending.
12. View category spending.
13. Identify the highest-spending category.
14. View spending trends.
15. View negative-goal progress.
16. View recent event spending.
17. View recent transactions.
18. Clean financial data from the dashboard.
19. View upcoming recurring payments.
20. View projected remaining spending.
21. Analyze spending by category, tag, goal, and date range.

The MVP does not include positive saving goals or non-expense transaction types.
