class LoanApprovalModel:
    def predict(self, features):
        income_annum = features[0]
        loan_amount = features[1]
        loan_term = features[2]
        cibil_score = features[3]
        residential_assets_value = features[4]
        commercial_assets_value = features[5]
        luxury_assets_value = features[6]
        bank_asset_value = features[7]

        LTI = loan_amount/income_annum
        Asset_coverage = (residential_assets_value + commercial_assets_value + luxury_assets_value + bank_asset_value)/ loan_amount
        Liquidity_ratio = bank_asset_value/loan_amount


        if LTI < 4 and cibil_score >= 530:
            return "Approved"
        if LTI > 4 and Asset_coverage > 1.5 and cibil_score >= 530:
            return "Approved"
        if LTI > 4 and Liquidity_ratio > 1.5 and cibil_score >= 530:
            return "Approved"
        return "Rejected"
        
def load_model():
    return LoanApprovalModel()