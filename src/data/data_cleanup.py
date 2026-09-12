import pandas as pd


def cleanup_food_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=["Unnamed: 13"])
    return df
