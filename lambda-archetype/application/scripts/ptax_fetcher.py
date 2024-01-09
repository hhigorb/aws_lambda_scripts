from datetime import datetime
import logging
import holidays
import pandas as pd


def rename_ptax_columns(df_ptax: pd.DataFrame) -> pd.DataFrame:
    expected_columns = {
        0: 'dt_cotacao',
        1: 'cod_moeda',
        2: 'tp_moeda',
        3: 'sg_moeda',
        4: 'vl_taxa_compra',
        5: 'vl_taxa_venda',
        6: 'vl_paridade_compra',
        7: 'vl_paridade_venda'
    }

    if set(df_ptax.columns) != set(expected_columns.keys()):
        raise ValueError(
            "DataFrame columns do not match the expected format.")

    return df_ptax.rename(columns=expected_columns)


def get_ptax_data(start_date_str: str, end_date_str: str) -> pd.DataFrame:
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    date_range = pd.date_range(
        start=start_date, end=end_date, freq='B')

    dfs = []

    for current_date in date_range:
        if current_date not in holidays.Brazil():
            date_string = current_date.strftime("%Y%m%d")
            url = (
                "https://www4.bcb.gov.br/Download/fechamento/"
                f"{date_string}.csv"
            )

            try:
                ptax_data = pd.read_csv(
                    url, sep=';', encoding='latin1', header=None)
                dfs.append(ptax_data)
            except Exception as e:
                error_message = (
                    "Error occurred for date "
                    f"{current_date.strftime('%Y-%m-%d')}: {e}"
                )

                logging.error(error_message)

    if not dfs:
        raise ValueError(
            "No valid data found between the specified dates.")

    df_ptax = pd.concat(dfs, ignore_index=True)
    df_ptax = rename_ptax_columns(df_ptax)

    df_ptax['dt_cotacao'] = pd.to_datetime(
        df_ptax['dt_cotacao'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    df_ptax['dt_cotacao'] = pd.to_datetime(
        df_ptax['dt_cotacao'], format='%Y-%m-%d')

    return df_ptax
