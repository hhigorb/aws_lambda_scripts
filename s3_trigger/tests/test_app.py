# Execute the test with the command: pytest s3_trigger/tests/test_app.py

from chalice.test import Client
from app import app


def test_s3_handler():
    with Client(app) as client:
        event = client.events.generate_s3_event(
            bucket='data-engineering-develop', key='test.txt')
        client.lambda_.invoke('s3_handler', event)
