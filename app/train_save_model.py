# -*- coding: utf-8 -*-
"""train_save_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/191oGq3ck7M_dn6ev3PYw1bm2dinb4j4-
"""

import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

train_df = pd.read_csv("train.csv")

def preprocess(df):
    df = df.copy()
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

train_cleaned = preprocess(train_df)

X = train_cleaned.drop(columns=['id', 'Calories'])
y = train_cleaned['Calories']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
numeric_features = X.select_dtypes(include=np.number).columns.tolist()

X_train_scaled = X_train.copy()
X_train_scaled[numeric_features] = scaler.fit_transform(X_train[numeric_features])

model = CatBoostRegressor(random_state=42, verbose=0)
model.fit(X_train_scaled, y_train)

joblib.dump(model, "model_catboost.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(numeric_features, "features.pkl")

print("Model, scaler, and feature list saved successfully.")