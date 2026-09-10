import pandas as pd
from model import load_model
from preprocessing import preprocessing_row

model = load_model()

def predict(data):
    data_preprocessed = []
    for _, row in data.iterrows():
        data_preprocessed.append(preprocessing_row(row))

    labels = []
    for row in data_preprocessed:
        labels.append(model.predict(row))
    return labels
    
data = pd.read_csv("loan_approval_dataset.csv")

labels = predict(data)

if " loan_status" in data.columns:
    accuracy = sum(                                          #sum() can count True as a value (it counts it like 1) and Fales counts as 0
        labels[i] == data.iloc[i][" loan_status"].strip() for i in range(len(labels))                                                   #generator, generates numbers
    )/len(labels)
    print(f"accuracy is {round(accuracy * 100, 2)}%")
else:
    print("Error")
