"""
Personal Finance Transaction Analyzer

Overview
--------
This program analyzes personal finance transaction data exported in CSV format
and produces a summarized spending and income report.

The tool is intended to help answer high-level questions such as:
- How much money was earned vs spent?
- Where is money being spent (by category)?
- What are the largest individual expenses?
- How much net balance change occurred over the analyzed data?

Inputs
------
One or more CSV files provided via the command line.

Each CSV file must have the following header:

    date,description,amount,category

Where:
- date:        ISO format YYYY-MM-DD
- description: Free-text merchant or payee name
- amount:      Signed decimal value in dollars
               (negative = spending, positive = income)
- category:    Category label (may be empty)

Example input row:

    2026-01-02,Starbucks,-5.43,Food

Internal Representation
-----------------------
All monetary values are converted from dollars to integer cents at parse time.
For example:
    -5.43  ->  -543
    2500.00 -> 250000

This guarantees exact arithmetic and avoids floating-point precision errors.
All calculations are performed using integer cents and converted back to
formatted dollar strings only when rendering output.

Outputs
-------
A human-readable text report printed to standard output.

Example (simplified):

    TOTAL INCOME:     $2,529.99
    TOTAL SPENDING:   $1,419.52
    NET:              $1,110.47

    SPENDING BY CATEGORY:
    Housing        $1,200.00
    Shopping       $  100.00
    Food           $    5.43

The program may also display:
- Top N largest spending transactions
- Counts of parsed vs skipped rows
- A preview of malformed rows with row numbers

Error Handling
--------------
Malformed rows (invalid amounts, missing fields, etc.) do not terminate
execution. Such rows are recorded and reported separately to ensure
fault-tolerant processing of real-world bank export data.

Intended Final Functionality
----------------------------
By completion, the program should:
- Parse CSV transaction data safely and deterministically
- Normalize transactions into a structured internal form
- Aggregate totals and category-level statistics
- Identify and report the largest expenses
- Handle invalid input gracefully without crashing
- Produce a clear, reproducible summary report

This tool is designed as a local, dependency-light analysis utility and does
not rely on external databases or third-party finance services.
"""

import csv


def main() -> None:
    # get all the rows in a list
    rows_list = read_csv()
    print_list(rows_list)

    # turn all rows into dictionaries
    rows_dictionary = rows_to_dictionaries(rows_list)

    # remove all the invalid rows
    clean_and_dirty_rows = clean_rows(rows_dictionary)

    clean = clean_and_dirty_rows["clean"]
    dirty = clean_and_dirty_rows["dirty"]

    # print the clean rows
    print("\n clean rows")
    print_list(clean)

    # print the dirty ones
    print("\n dirty rows")
    print_list(dirty)

    # get the income and spending amounts (in dict format)
    income_and_spending = compute_income_and_spending(clean)

    # extract them
    income_cents = income_and_spending["total_income"]
    spending_cents = income_and_spending["total_spending"]

    # calculate the net
    net_income = net_cents(income_cents, spending_cents)

    print(f"total income in cents: {income_cents}")
    print(f"total spending in cents: {spending_cents}")
    print(f"net income: {net_income}")

    # print the spending by category
    category_spending = spending_by_category(clean)
    print(f"spending by category: {category_spending}")


# read the csv and output a list of all rows
def read_csv() -> list:
    rows = []
    with open("transactions.csv", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            rows.append(row)
    return rows


# get all the rows, and take out the invalid ones
def clean_rows(rows: list) -> dict:

    clean_and_dirty = {"clean": [], "dirty": []}
    for i in range(len(rows)):

        # first try to convert the dollars into pennies. if not able to, dont add to clean list.
        try:
            rows[i]["amount"] = dollar_to_penny(rows[i]["amount"])
        except ValueError:
            clean_and_dirty["dirty"].append(rows[i])
            continue

        # if every key in the dictionary has a value, then dont do anything
        if (
            rows[i]["date"]
            and rows[i]["description"]
            and rows[i]["amount"]
            and rows[i]["category"]
        ):
            # make sure amount has correct symbol, then append to clean list
            check_amount_symbol(rows[i])
            clean_and_dirty["clean"].append(rows[i])
        else:
            clean_and_dirty["dirty"].append(rows[i])

    return clean_and_dirty


# takes a dictionary, makes sure the symbol of "amount" is correct
def check_amount_symbol(row: dict) -> None:
    category = row["category"]
    amount = row["amount"]

    if category == "Income" and amount < 0:
        row["amount"] = -amount
    elif category != "Income" and amount > 0:
        row["amount"] = -amount

    return


# get the 3 top spendings


# calculate the spending according to category
def spending_by_category(rows: list) -> dict:
    category_spending = {}
    for row in rows:

        category = row["category"]
        amount = row["amount"]
        # if the category is income, then skip it
        if category == "Income":
            continue
        if category_spending.get(category):
            category_spending[category] += amount
        else:
            category_spending[category] = amount

    return category_spending


# calculate the total income and the spending amount
def compute_income_and_spending(clean_rows: list) -> dict:

    income_and_spending = {"total_income": 0, "total_spending": 0}

    for row in clean_rows:
        category = row["category"]
        amount = row["amount"]

        if category == "Income":
            income_and_spending["total_income"] += amount
        else:
            income_and_spending["total_spending"] += amount

    # convert from negative to positive cents
    income_and_spending["total_spending"] = -income_and_spending["total_spending"]

    return income_and_spending


def net_cents(income: int, spending: int) -> int:
    return income - spending


# convert dollars to pennies
def dollar_to_penny(dollars: str) -> int:
    pennies = round(float(dollars) * 100)
    return pennies


# convert pennies to dollars
def penny_to_dollar(pennies: int) -> float:
    dollars = pennies / 100
    return dollars


# turn a single row into a dictionary
def row_to_dictionary(row: list) -> dict:
    keys = ["date", "description", "amount", "category"]
    values = row

    row_dictionary = {}

    for i in range(len(keys)):
        row_dictionary[keys[i]] = values[i]

    return row_dictionary


# turn every single row into a dictionary
def rows_to_dictionaries(rows: list) -> list:
    counter = 0
    for row in rows:
        row_dict = row_to_dictionary(row)
        rows[counter] = row_dict
        counter += 1

    return rows


# print list neatly
def print_list(items):

    i = 1
    for item in items:
        print(i, ".", item)
        i += 1


# print dictionary neatly
def print_dict(d):
    for key in d:
        print(key, ":", d[key])


if __name__ == "__main__":
    main()
