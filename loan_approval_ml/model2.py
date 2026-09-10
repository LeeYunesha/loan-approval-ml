from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from model import load_model
import joblib

class LoanApprovalModel:
    def __init__(self, algorithm):
        self.algorithm = algorithm
        if algorithm == "RandomForestClassifier":
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        
        if algorithm == "DecisionTreeClassifier":
            self.model = DecisionTreeClassifier(random_state=42)
        
        if algorithm == "ExtraTreesClassifier":
            self.model = ExtraTreesClassifier(n_estimators=100, random_state=42)

        if algorithm == "GradientBoostingClassifier":
            self.model = GradientBoostingClassifier(random_state=42)

        if algorithm == "AdaBoostClassifier":
            self.model = AdaBoostClassifier(random_state=42)

        if algorithm == "LogisticRegression":
            self.model = LogisticRegression(max_iter= 1000)

        if algorithm == "KNeighborsClassifier":
            self.model = KNeighborsClassifier(n_neighbors = 5)

        if algorithm == "SVC":  
            self.model = SVC(probability= True, random_state=42)

        if algorithm == "GaussianNB":
            self.model = GaussianNB()



    
    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, features):
        prediction = self.model.predict(features)
        return int(prediction[0])
    
    def predict_proba(self, features):
        propability = self.model.predict_proba([features])
        return propability[0][1]
    
    def evaluate(self, X, y):
        return self.model.score(X, y)
    
    def save(self, file_name):
        joblib.dump(self.model, file_name)

    def load(self, file_name):
        self.model = joblib.load(file_name)
        
        
def load_model(algorithm):
    return LoanApprovalModel(algorithm)





    






