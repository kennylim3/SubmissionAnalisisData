import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


def create_yearly_rental_df(df):
    yearly_day_df = day_df.groupby("yr").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    }).reset_index()

    yearly_day_df.rename(columns={
        "yr": "year",
        "cnt": "total_rental"
    }, inplace=True)

    return yearly_day_df

def create_season_rental_df(df):
    season_day_df = day_df.groupby("season").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    }).cnt.sort_values(ascending=False).reset_index()

    season_day_df.rename(columns={
        "cnt": "total_rental"
    }, inplace=True)

    return season_day_df

def create_weekday_rental_df(df):
    weekday_day_df = day_df.groupby("weekday").agg({
        "casual": "sum",
        "registered": "sum",
        "cnt": "sum"
    }).cnt.sort_values(ascending=False).reset_index()

    weekday_day_df.rename(columns={
        "cnt": "total_rental"
    }, inplace=True)

    return weekday_day_df

day_df = pd.read_csv("day_data.csv")

st.header(':bike: Bike Sharing :sparkles:')
st.subheader('Yearly Rental')
fig = plt.figure(figsize=(10, 5))
plt.plot(create_yearly_rental_df(day_df)["year"], create_yearly_rental_df(day_df)["total_rental"], marker='o', linewidth=2, color="#72BCD4")
plt.title("Bike Sharing Performance in 2011 and 2012", loc="center", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()

st.pyplot(fig)

st.subheader("Best Performing Season")
fig, ax = plt.subplots(figsize=(20, 10))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="total_rental", y="season", data=create_season_rental_df(day_df), palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Best Performing Season", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)


st.subheader("Best Performing Day")
fig, ax = plt.subplots(figsize=(20, 10))

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

sns.barplot(x="total_rental", y="weekday", data=create_weekday_rental_df(day_df), palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Best Performing Day", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)