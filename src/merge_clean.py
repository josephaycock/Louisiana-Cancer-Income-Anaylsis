# Merges two csv (income and cancer)

def datasets_merge(cancer_df, income_df):
    # Checks and remove whitespaces and lowercase for merge
    cancer_df["merge_key"] = (
        cancer_df["Parish"]
        .str.lower()
        .str.replace(" ", "")
    )

    income_df["merge_key"] = (
        income_df["Parish"]
        .str.lower()
        .str.replace(" ", "")
    )

    # Merge both csv
    merge_csv = cancer_df.merge(income_df, on="merge_key", how="inner")

    # Drops the merge_key column
    final_merge_csv = merge_csv.drop(columns=["merge_key", "Parish_y"]).rename(columns={"Parish_x": "Parish"})

    return final_merge_csv