from src.cancer_clean import clean_cancer_data

cancer = clean_cancer_data("data/raw/cancer-rates.csv")

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

# Saving raw csv (cancer-rates.csv) into processed csv (processed-cancer-rates.csv)
cancer.to_csv('data/processed/processed-cancer-rates.csv', index=False)