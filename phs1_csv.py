#“In Phase 1, we first loaded the Kaggle credit card dataset using pandas. We verified the dataset structure, number of rows and columns, and checked the class distribution to confirm the fraud imbalance.”

import pandas as pd
import numpy as np
#--phase 2--
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
#--phase 3---
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#load data
df = pd.read_csv('creditcard.csv') #df is dataframe

print("Data loaded successfully!")
print("shape of data:", df.shape) #return no of row and cols
print("\nFirst 5 rows of data:\n", df.head())
print("\nColumn names:\n", df.columns)
print("\n Class distribution:") #class distribution
print(df["Class"].value_counts()) #counting how many times each class label (unique element in the "Class" column) appears in your dataset.

#---------PHASE 1 ENDS HERE----------------
X= df.drop("Class", axis=1) #drop class column and assign to X
y= df["Class"] #assign class column to y



X_train,X_test, y_train, y_test = train_test_split(
              X, y,
              test_size =0.2,
              random_state = 42,
              stratify = y
)
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)
print("BEFORE SMOTE:", y_train.value_counts())
print("AFTER SMOTE:", y_train_smote.value_counts())

"""Train New Model on SMOTE Data"""
#model_smote = LogisticRegression(class_weight= 'balanced', max_iter = 1000)
model_smote = LogisticRegression(max_iter = 2000, solver='liblinear')
model_smote.fit(X_train_smote, y_train_smote)
print("\nModel trained on SMOTE data completed successfully")

"""We removed class_weight='balanced'
Because data is already balanced."""

print("\nTraining set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

print("\nTraining set class distribution:")
print(y_train.value_counts())

print("\nTesting set class distribution:")
print(y_test.value_counts())


scaler= StandardScaler()

#scale only the amount column
X_train['Amount']= scaler.fit_transform(X_train[['Amount']])
X_test['Amount'] = scaler.transform(X_test[['Amount']])

print("\nScaling applied to Amount column.")

print("\nFeatures (X) shape:", X.shape)
print("Target (y) shape:", y.shape) 

#-----PHASE 2 COMPLETED HERE----------------
#-----PHASE3----- teaching the computer to learn the difference between  fraud and legit data

#create model
model= LogisticRegression(class_weight= 'balanced', max_iter = 1000)  #class_wgt="balanced", means that the algorithm will automatically adjust the weights inversely proportional to class frequencies in the input data, which can help improve performance on imbalanced datasets. max_iter=1000 means that the algorithm will run for a maximum of 1000 iterations to find the optimal solution. This is often necessary when dealing with complex datasets or when the default number of iterations is not sufficient for convergence.
# class_weight='balanced' Because fraud cases are rare. This gives more importance to fraud class.
#train model
model.fit(X_train, y_train)

print("\n Model training completed successfully")


#Step1: predict on test data 
y_pred = model.predict(X_test)

#Step2: Accuracy
print("\nAccuracy:", accuracy_score(y_test, y_pred))

#Step3: Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

#Step4: Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


#----PHASE 4---- 
#STEP 1- MODEL SAVE USING joblib
import joblib
#save the SMOTE training model
joblib.dump(model_smote, "fraud_detection_model_smote.pkl")
print("Model saved successfully!")






#Evaluate the SMOTE model
y_pred_smote = model_smote.predict(X_test)
print("\nSMOTE Model Accuracy:", accuracy_score(y_test, y_pred_smote))
print("\nSMOTE Model Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_smote))
print("\nSMOTE Model Classification Report:")
print(classification_report(y_test, y_pred_smote))  