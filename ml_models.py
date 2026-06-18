from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    r2_score
)

from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)

import pandas as pd


def prepare_data(df):

    data = df.copy()

    encoders = {}

    for col in data.columns:

        if data[col].dtype == "object":

            le = LabelEncoder()

            data[col] = le.fit_transform(
                data[col].astype(str)
            )

            encoders[col] = le

    return data


def run_ml_model(
    df,
    target_column
):

    data = prepare_data(df)

    X = data.drop(
        columns=[target_column]
    )

    y = data[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    if y.nunique() <= 10:

        model = RandomForestClassifier()

        model.fit(
            X_train,
            y_train
        )

        preds = model.predict(
            X_test
        )

        score = accuracy_score(
            y_test,
            preds
        )

        return (
            "Classification",
            score
        )

    else:

        model = RandomForestRegressor()

        model.fit(
            X_train,
            y_train
        )

        preds = model.predict(
            X_test
        )

        score = r2_score(
            y_test,
            preds
        )

        return (
            "Regression",
            score
        )