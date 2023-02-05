from app import app

def test_index_heading():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Events" in response.data
    assert b"<h1>" in response.data
    
def test_index_text_field():
    response = app.test_client().get('/')
    assert b"<input" in response.data
    assert b'placeholder="Event name"' in response.data
    assert b"Event name</label>" in response.data

def test_index_submit_button():
    response = app.test_client().get('/')
    assert b"<button" in response.data
    assert b"Add" in response.data

def test_index_footer():
    response = app.test_client().get('/')
    assert b"Copyright" in response.data
    assert b"2022 - 2023" in response.data
    assert b"Sabrina Samuel" in response.data