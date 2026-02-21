from src.cancer_clean import clean_cancer_data

cancer = clean_cancer_data("data/raw/cancer-rates.csv")
print("Cancer Header\n------------------------------------------")
print(cancer.head())
print("\nTotal Parishes\n------------------------------------------")
print(len(cancer))
print("\nParish List\n------------------------------------------")
for i, parish in enumerate(cancer["Parish"], start=1):
    print(f"{i}. {parish}")