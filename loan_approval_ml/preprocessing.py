def preprocessing_row(row):
    income_annum = row["income_annum"]
    loan_amount = row["loan_amount"]
    loan_term = row["loan_term"]
    cibil_score = row["cibil_score"]
    residential_assets_value = row["residential_assets_value"]
    commercial_assets_value = row["commercial_assets_value"]
    luxury_assets_value = row["luxury_assets_value"]
    bank_asset_value = row["bank_asset_value"]
    return[income_annum, loan_amount,
           loan_term, cibil_score, 
           residential_assets_value, commercial_assets_value, 
           luxury_assets_value, bank_asset_value]
