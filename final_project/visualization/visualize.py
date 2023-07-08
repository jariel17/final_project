import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def covid_time_series(df: pd.DataFrame):
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series");

def global_context(df, palette="Set1"):
    sns.barplot(
        data=df,
        x="value",
        y="country_region",
        palette=palette
    )
    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");