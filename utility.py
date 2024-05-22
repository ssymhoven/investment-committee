import pandas as pd


def get_indices() -> pd.DataFrame:
    return pd.read_excel('data.xlsx', sheet_name='Indices', header=0, index_col=0)


def get_indices_data() -> pd.DataFrame:
    return pd.read_excel('data.xlsx', sheet_name='Data', header=0, index_col=0)


def calculate_relative_performance(first: pd.Series, second: pd.Series) -> pd.Series:
    relative_performance = (first / second)
    relative_performance = (relative_performance / relative_performance.iloc[0]) - 1
    return relative_performance * 100


def calculate_yield(first: pd.Series) -> pd.Series:
    relative_performance = (first / first.iloc[0]) - 1
    return relative_performance * 100
