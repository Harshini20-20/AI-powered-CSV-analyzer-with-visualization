import streamlit as st
import plotly.express as px


def show_histogram(df):
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found.")
        return

    column = st.selectbox(
        "Select Numeric Column",
        numeric_cols,
        key="histogram"
    )

    fig = px.histogram(
        df,
        x=column,
        title=f"Histogram of {column}"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_scatter(df):
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) < 2:
        st.warning("Need at least 2 numeric columns.")
        return

    x_col = st.selectbox(
        "X Axis",
        numeric_cols,
        key="scatter_x"
    )

    y_col = st.selectbox(
        "Y Axis",
        numeric_cols,
        key="scatter_y"
    )

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{x_col} vs {y_col}"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_boxplot(df):
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found.")
        return

    column = st.selectbox(
        "Select Column",
        numeric_cols,
        key="boxplot"
    )

    fig = px.box(
        df,
        y=column,
        title=f"Box Plot of {column}"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_piechart(df):
    cat_cols = df.select_dtypes(include="object").columns

    if len(cat_cols) == 0:
        st.warning("No categorical columns found.")
        return

    column = st.selectbox(
        "Select Column",
        cat_cols,
        key="piechart"
    )

    values = df[column].value_counts().reset_index()
    values.columns = [column, "Count"]

    fig = px.pie(
        values,
        names=column,
        values="Count",
        title=f"Pie Chart of {column}"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_heatmap(df):
    numeric_df = df.select_dtypes(include="number")

    if len(numeric_df.columns) < 2:
        st.warning("Need at least 2 numeric columns.")
        return

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="Correlation Heatmap"
    )

    st.plotly_chart(fig, use_container_width=True)