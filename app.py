import streamlit as st
import pandas as pd

from insights import generate_ai_insights
from charts import (
    show_histogram,
    show_scatter,
    show_boxplot,
    show_piechart,
    show_heatmap
)

st.set_page_config(
    page_title="AI CSVision",
    layout="wide"
)

st.title("📊 AI CSVision")
st.caption("Smart CSV Analytics Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success(
        f"Loaded {df.shape[0]} rows and {df.shape[1]} columns"
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Overview",
            "Visualizations",
            "Insights",
            "Data Cleaning"
        ]
    )

    # OVERVIEW
    with tab1:

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Rows",
            df.shape[0]
        )

        c2.metric(
            "Columns",
            df.shape[1]
        )

        c3.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

        st.subheader("Column Information")
        st.dataframe(df.dtypes.astype(str))

    # VISUALIZATION
    with tab2:

        st.subheader("Interactive Charts")

        chart_type = st.selectbox(
            "Choose Chart",
            [
                "Histogram",
                "Scatter",
                "Box Plot",
                "Pie Chart",
                "Heatmap"
            ]
        )

        if chart_type == "Histogram":
            show_histogram(df)

        elif chart_type == "Scatter":
            show_scatter(df)

        elif chart_type == "Box Plot":
            show_boxplot(df)

        elif chart_type == "Pie Chart":
            show_piechart(df)

        elif chart_type == "Heatmap":
            show_heatmap(df)

    # INSIGHTS
    with tab3:

        st.subheader("🤖 AI Insights")

        insights = generate_ai_insights(df)

        for insight in insights:
            st.info(insight)

    # DATA CLEANING
    with tab4:

        st.subheader("Data Cleaning")

        if st.button("Remove Duplicates"):

            before = len(df)

            df = df.drop_duplicates()

            after = len(df)

            st.success(
                f"Removed {before-after} duplicate rows"
            )

        if st.button("Drop Missing Rows"):

            before = len(df)

            df = df.dropna()

            after = len(df)

            st.success(
                f"Removed {before-after} rows"
            )

        st.download_button(
            "Download Cleaned CSV",
            df.to_csv(index=False),
            "cleaned_data.csv",
            "text/csv"
        )

else:

    st.info(
        "Upload a CSV file to begin analysis."
    )

from reports import (
    create_excel_report,
    create_ppt_report
)