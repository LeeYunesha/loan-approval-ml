import pandas as pd
from model2 import load_model
from preprocessing import preprocessing_row
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

algorithm = "GaussianNB"
model = load_model(algorithm)

algorithm_not_scale = ["KNeighborsClassifier" , "LogisticRegression", "SVC", "GaussianNB"]

data = pd.read_csv("loan_approval_dataset.csv")
data.columns = data.columns.str.strip()
X = []
y = []

for _, row in data.iterrows():
    X.append(preprocessing_row(row))
    if row["loan_status"].strip() == "Approved":
        y.append(1)
    elif row["loan_status"].strip() == "Rejected":
        y.append(0)
    else:
        print("Error")

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.2, train_size = 0.8, random_state = 42)

if algorithm in algorithm_not_scale:
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


model.train(X_train, Y_train)

labels = []

for features in X:
    labels.append(model.predict([features]))

for i in range(20, 100):
    propability = model.predict_proba(X_test[i])
    print(f"row: {i+1} prediction: {propability:.2%}")



accuracy = model.evaluate(X_test, Y_test)
accuracy1 = model.evaluate(X_train, Y_train)

print(accuracy, accuracy1, sep="\n" )

# model.save("Loan_Model1.pkl")
# model.load("Loan_Model.pkl")

# accuracy = model.evaluate(X_test, Y_test)
# accuracy1 = model.evaluate(X_train, Y_train)

# print(accuracy, accuracy1, sep="\n" )




    