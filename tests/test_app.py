from app.flask_app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_prediction():
    client = app.test_client()
    response = client.post("/predict", data={"N": "90", "P": "42", "K": "43", "temperature": "20.8", "humidity": "82", "ph": "6.5", "rainfall": "202"})
    assert response.status_code == 200
    assert b"Recommended Crop:" in response.data
