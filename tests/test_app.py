from app import app

def test_hello():
    response = app.test_client().get('/')
    # assertEqual(response.status_code, 200)
    assert response.status_code == 200
    # assert response.body == "Hello, World!"
    assert response.data.decode('utf-8') == "Hello, World!"