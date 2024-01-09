import boto3
import pandas as pd
import logging
from chalice import Chalice

app = Chalice(app_name='s3_trigger')
app.debug = True


# Set the value of APP_BUCKET_NAME in the .chalice/config.json file.
S3_BUCKET = "data-engineering-develop"


""" @app.on_s3_event(bucket=S3_BUCKET, events=['s3:ObjectCreated:*'])
def s3_handler(event):
    app.log.debug("Received event for bucket: %s, key: %s",
                  event.bucket, event.key)
"""

'''
Se necessário, utilize outro evento, como a exclusão de um objeto ou
a atualização de um objeto no parâmetro events.
'''


@app.on_s3_event(bucket=S3_BUCKET, events=['s3:ObjectCreated:*'])
def s3_json_data_to_parquet(event):
    s3_resource = boto3.resource('s3')

    json_file_key = event.key
    json_file_obj = s3_resource.Object(S3_BUCKET, json_file_key)
    json_file_content = json_file_obj.get()['Body'].read().decode('utf-8')

    df = pd.read_json(json_file_content)

    df['new_column'] = 'value'

    json_content_transformed = df.to_json(orient='records')

    json_content_bytes = json_content_transformed.encode('utf-8')

    json_file_key = json_file_key.replace(
        'raw', 'transformed')
    json_file_obj = s3_resource.Object(S3_BUCKET, json_file_key)
    json_file_obj.put(Body=json_content_bytes)

    logging.info(f"Modified JSON file saved to {S3_BUCKET}/{json_file_key}")
