import pandas as pd

df = pd.read_csv("loan_approval_dataset.csv")

df.columns = df.columns.str.strip()


df["residential_assets_value"] + df["commercial_assets_value"] + df["luxury_assets_value"] + df["bank_asset_value"]

df["loan_amount_to_term"] = df["loan_amount"]* df["loan_term"]
df["loan_amount_to_term_1"] = df["loan_amount"]/ df["loan_term"]

df["income_to_loan_term"] = df["income_annum"]* df["loan_term"]
df["loan_amount_to_income"] = df["loan_amount"]/ df["income_annum"]

df["cibil_loan_term"] = df["cibil_score"]* df["loan_term"]
df["assets_to_income"] = (df["residential_assets_value"] + df["commercial_assets_value"] + df["luxury_assets_value"] + df["bank_asset_value"])/ df["income_annum"]

df["assets_to_cibil"] = df["income_annum"]* df["loan_term"]
df["income_to_loan_term_1"] = df["income_annum"]/ df["loan_term"]

print(df["loan_amount_to_term"], 
      df["loan_amount_to_term_1"],df["income_to_loan_term"],
      df["loan_amount_to_income"],
      df["cibil_loan_term"],
      df["assets_to_income"],
      df["assets_to_cibil"],
      df["income_to_loan_term_1"])
print(df["loan_status"])


