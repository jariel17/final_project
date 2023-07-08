import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def top_countries(df, countries, amount=20):
        countries_df = (
            df
            .select_columns(["country_region", "value"])
            .groupby(["country_region"])
            .aggregate("sum")
            .sort_values("value", ascending=False)
            .reset_index()
            .head(amount)
            .transform_column(
                column_name="country_region",
                function=lambda x: "red" if x in countries else "lightblue",
                dest_column_name="color"
                )
            )   
        return countries_df;


