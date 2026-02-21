# Cleans parish-income.csv to household, estimates, and median income
import pandas as pd

def income_clean_data(file_path):

    label_column = "Label (Grouping)"
    value_column = "Median income (dollars)"

    income = pd.read_csv(file_path, engine='python')

    current_parish = None
    results = []
    in_households = False

    #
    for i, row in income.iterrows():
        label = str(row[label_column]).strip()


        if "Parish" in label and ", Louisiana" in label:
            current_parish = (
                label.replace("Parish", "")
                .replace(", Louisiana", "")
                .strip()
            )
            in_households = False
            continue

        if label == "Households":
            in_households = True
            continue

        if in_households and label == "Estimate" and current_parish:
            results.append(((current_parish), row[value_column]))
            in_households = False

    income_clean = pd.DataFrame(results, columns=["Parish", "median income (dollars)"])

    # Removes commas in income
    income_clean["median income (dollars)"] = (
        income_clean["median income (dollars)"]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    # Changes string to numeric value
    income_clean["median income (dollars)"] = pd.to_numeric(
        income_clean["median income (dollars)"],
        errors="coerce",
    )

    # Renaming 'median income (dollars)' to 'median_income'
    income_clean = income_clean.rename(
        columns={
            'median income (dollars)': 'median_income'
        }
    )

    # Check if there empty rows and removes it
    income_clean = income_clean.dropna(
        subset=["Parish", "median_income"]
    )

    return income_clean