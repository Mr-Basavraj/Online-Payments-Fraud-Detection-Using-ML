import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("PS_20174392719_1491204439457_log.csv")

data["type"] = data["type"].map({"CASH_OUT": 1, "PAYMENT": 2, "CASH_IN": 3, "TRANSFER": 4, "DEBIT": 5})

data["balanceError"] = data["oldbalanceOrg"] - data["amount"] - data["newbalanceOrig"]

x = np.array(data[["type", "amount", "oldbalanceOrg", "newbalanceOrig", "balanceError"]])
y = np.array(data["isFraud"])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.20, random_state=42)

# THIS IS THE FIX ↓
model = DecisionTreeClassifier(class_weight='balanced')
model.fit(xtrain, ytrain)

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Success! 'model.pkl' has been created in your folder.")