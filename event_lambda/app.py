import boto3
import logging
from chalice import Chalice
from chalicelib.ptax import get_ptax_data
from chalicelib.parquet_converter import ParquetConverter

app = Chalice(app_name='app')


@app.lambda_function(name="ptax_data_to_s3")
def handler(event, context):
    data = get_ptax_data(event['start_date'], event['end_date'])

    data['year'] = data['dt_cotacao'].dt.year
    data['month'] = data['dt_cotacao'].dt.strftime('%m')
    data['day'] = data['dt_cotacao'].dt.strftime('%d')

    grouped = data.groupby(['year', 'month', 'day'])

    s3_client = boto3.client('s3')
    bucket_name = 'data-engineering-develop'

    for (year, month, day), group in grouped:
        group = group.drop(['year', 'month', 'day'], axis=1)
        file_name = f'{year}-{month}-{day}.parquet'

        path = (
            f'raw/financial-resources/ptax/'
            f'year={year}/month={month}/{file_name}'
        )

        parquet_bytes = ParquetConverter.convert_df_to_parquet(group)

        s3_client.put_object(
            Bucket=bucket_name,
            Key=path,
            Body=parquet_bytes,
            ContentType='application/octet-stream'
        )

        logging.info(f'Successfully sent data for {file_name} to S3')
