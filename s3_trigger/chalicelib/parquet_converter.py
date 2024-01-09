import pandas as pd
from io import BytesIO


class ParquetConverter:
    @staticmethod
    def convert_df_to_parquet(df: pd.DataFrame) -> BytesIO:
        try:
            data = pd.DataFrame(df)
            parquet_bytes = BytesIO()
            data.to_parquet(parquet_bytes, index=False)
            parquet_bytes.seek(0)
            return parquet_bytes
        except Exception as e:
            raise Exception(
                f"An error occurred while converting data to Parquet: {e}")
