# Execute the test with the command: pytest event_lambda/tests/test_app.py

from chalice.test import Client
from app import app


def test_index():
    with Client(app) as client:
        response = client.lambda_.invoke(
            'my_first_lambda', {"name": "Higor", "age": "23"})
        assert response.payload == 'Hello Higor, you are 23 years old!'
