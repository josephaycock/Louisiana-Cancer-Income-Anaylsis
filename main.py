from src.cancer_clean import clean_cancer_data

cancer = clean_cancer_data("data/raw/cancer-rates.csv")
print(cancer.head())