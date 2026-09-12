import pandas as pd


def import_food_delivery_data() -> pd.DataFrame:
    return pd.read_csv("../data/online food delivery dataset.csv")
