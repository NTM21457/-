import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

def plot_income_distribution(df, grid=True):
    fig = px.histogram(df, x='доход', nbins=20)
    fig.update_layout(
        xaxis=dict(showgrid=grid),
        yaxis=dict(showgrid=grid)
    )
    st.plotly_chart(fig)



def plot_top_clients(df):
    top_clients = df.nlargest(5, 'баланс')
    fig, ax = plt.subplots()
    ax.barh(top_clients['клиент'], top_clients['баланс'])
    ax.set_xlabel('Баланс')
    ax.set_ylabel('Клиент')
    st.pyplot(fig)