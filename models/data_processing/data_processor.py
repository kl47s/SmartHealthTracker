import pandas as pd

class DataProcessor:
    @staticmethod
    def clean_data(df):
        # Пример очистки данных: удаление NaN
        return df.dropna()

    @staticmethod
    def normalize_data(df):
        return (df - df.mean()) / df.std()
