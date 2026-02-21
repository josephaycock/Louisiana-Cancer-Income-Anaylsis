# Cleans the cancer-rates.csv to only parish and cancer rates

import pandas as pd

def clean_cancer_data(file_path):

    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Empty to store later
    header_row = None
    # Checking for header
    for i, line in enumerate(lines):
        if line.startswith("Parish,"):
            header_row = i
            break

    cancer = pd.read_csv(file_path, skiprows=header_row, engine='python')

    # Removing non-parish rows
    cancer = cancer[cancer["Parish"].str.contains("Parish", na=False)]

    return cancer