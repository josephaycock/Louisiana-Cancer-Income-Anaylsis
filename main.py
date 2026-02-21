from src.cancer_clean import clean_cancer_data
from src.income_clean import income_clean_data

cancer = clean_cancer_data("data/raw/cancer-rates.csv")
income = income_clean_data("data/raw/parish-income.csv")

# Prints for cancer_clean.py (for testing)
print("Cancer Header\n------------------------------------------")
print(cancer.head())

print("\nCancer Header (Types)\n------------------------------------------")
print(cancer.dtypes)

print("\nTotal Parishes\n------------------------------------------")
print(len(cancer))

print("\nParish List\n------------------------------------------")
for i, parish in enumerate(cancer["Parish"], start=1):
    print(f"{i}. {parish}")

# Prints for income_clean.py (for testing)
print("\nIncome Header\n------------------------------------------")
print(income.head())

print("\nIncome Header (Types)\n------------------------------------------")
print(income.dtypes)

print("\nTotal Income\n------------------------------------------")
print(len(income))

print("\nIncome List\n------------------------------------------")
for i, row in enumerate(income.itertuples(), start=1):
    print(f"{i}. {row.Parish} - {row.median_income}")

# Saving raw csv (cancer-rates.csv) into processed csv (processed-cancer-rates.csv)
cancer.to_csv('data/processed/processed-cancer-rates.csv', index=False)

# Saving raw csv (parish-income.csv) into processed csv (processed-parish-income.csv)
income.to_csv('data/processed/processed-parish-income.csv', index=False)