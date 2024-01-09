# Execute the test with the command: pytest scheduled_lambda/tests/test_app.py

from chalice.test import Client
from app import app


def test_index():
    with Client(app) as client:
        response = client.lambda_.invoke(
            'scheduled',
            client.events.generate_cw_event(
                source="",
                detail_type="",
                detail="",
                resources=""
            )
        )
        assert response.payload == 'Hello from Lambda!'
