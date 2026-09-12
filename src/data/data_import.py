import pandas as pd

from data import data_cleanup


def csv_to_dataframe(filename: str, cleaner=None) -> pd.DataFrame:
    df = pd.read_csv(filename)
    if cleaner:
        df = cleaner(df)
    return df


def import_food_orders() -> pd.DataFrame:
    return csv_to_dataframe(
        filename="../data/online food delivery dataset.csv",
        cleaner=data_cleanup.cleanup_food_orders,
    )


def import_sleep_data() -> pd.DataFrame:
    return csv_to_dataframe(
        filename="../data/Sleep_Efficiency.csv",
    )
