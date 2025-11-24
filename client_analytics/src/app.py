import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from data_processing import load_data, get_insights
from visualization import plot_income_distribution, plot_top_clients
load_dotenv()
@st.cache_data
def get_data():
    return load_data('fixtures/sample_clients.csv')
def main():
    st.title("Аналитика по клиентским данным")

    df = get_data()

    min_age = df['возраст'].min(skipna=True)
    max_age = df['возраст'].max(skipna=True)

    if pd.isnull(min_age):
        min_age = 18
    if pd.isnull(max_age):
        max_age = 100

    age_min = int(min_age)
    age_max = int(max_age)

    min_income = df['доход'].min(skipna=True)
    max_income = df['доход'].max(skipna=True)

    if pd.isnull(min_income):
        min_income = 0
    if pd.isnull(max_income):
        max_income = 1000000

    income_min = int(min_income)
    income_max = int(max_income)

    st.sidebar.header("Фильтры")
    age_filter = st.sidebar.slider(
        "Возраст",
        min_value=age_min,
        max_value=age_max,
        value=(18, 100)
    )
    income_filter = st.sidebar.slider(
        "Доход",
        min_value=income_min,
        max_value=income_max,
        value=(income_min, income_max)
    )
    region_filter = st.sidebar.multiselect(
        "Регион",
        options=df['регион'].dropna().unique(),
        default=df['регион'].dropna().unique()
    )

    filtered_df = df[
        (df['возраст'] >= age_filter[0]) & (df['возраст'] <= age_filter[1]) &
        (df['доход'] >= income_filter[0]) & (df['доход'] <= income_filter[1]) &
        (df['регион'].isin(region_filter))
    ]

    st.header("Общая статистика ")
    st.write(get_insights(filtered_df))

    st.header("Распределение доходов")
    plot_income_distribution(filtered_df, grid=True)

    st.header("Топ-5 клиентов по балансу")
    plot_top_clients(filtered_df)


if __name__ == "__main__":
    main()