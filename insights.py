import pandas as pd
import numpy as np

def generate_ai_insights(df):
    insights = []

    # Dataset Size
    rows, cols = df.shape
    insights.append(f"📊 Dataset contains {rows} rows and {cols} columns.")

    # Missing Values
    missing = df.isnull().sum()
    missing_cols = missing[missing > 0]

    if len(missing_cols) > 0:
        insights.append(
            f"⚠️ {len(missing_cols)} columns contain missing values."
        )

        top_missing = missing_cols.sort_values(
            ascending=False
        ).head(3)

        for col, count in top_missing.items():
            insights.append(
                f"'{col}' has {count} missing values."
            )
    else:
        insights.append(
            "✅ No missing values detected."
        )

    # Duplicates
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        insights.append(
            f"⚠️ Dataset contains {duplicates} duplicate rows."
        )
    else:
        insights.append(
            "✅ No duplicate rows found."
        )

    # Numeric Analysis
    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns

    if len(numeric_cols) > 0:

        for col in numeric_cols:

            mean_val = df[col].mean()
            max_val = df[col].max()
            min_val = df[col].min()

            insights.append(
                f"📈 '{col}' ranges from {min_val:.2f} to {max_val:.2f} "
                f"with an average of {mean_val:.2f}."
            )

    # Correlation Analysis
    if len(numeric_cols) > 1:

        corr_matrix = df[numeric_cols].corr()

        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):

                col1 = corr_matrix.columns[i]
                col2 = corr_matrix.columns[j]

                corr = corr_matrix.iloc[i, j]

                if corr > 0.7:
                    insights.append(
                        f"🔥 Strong positive correlation between "
                        f"'{col1}' and '{col2}' ({corr:.2f})."
                    )

                elif corr < -0.7:
                    insights.append(
                        f"❄️ Strong negative correlation between "
                        f"'{col1}' and '{col2}' ({corr:.2f})."
                    )

    # Categorical Columns
    cat_cols = df.select_dtypes(
        include=["object"]
    ).columns

    for col in cat_cols[:3]:

        top_value = (
            df[col]
            .value_counts()
            .idxmax()
        )

        count = (
            df[col]
            .value_counts()
            .max()
        )

        insights.append(
            f"🏆 Most frequent value in '{col}' "
            f"is '{top_value}' ({count} occurrences)."
        )

    return insights