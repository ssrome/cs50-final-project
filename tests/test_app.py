from app import app


def test_index_heading():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert "Events" in response.text
    assert "<h1>" in response.text


def test_index_text_field():
    response = app.test_client().get('/')
    assert "<input" in response.text
    assert 'placeholder="Event name"' in response.text
    assert "Event name</label>" in response.text


def test_index_submit_button():
    response = app.test_client().get('/')
    assert "<button" in response.text
    assert "Add" in response.text


def test_index_footer():
    response = app.test_client().get('/')
    assert "Copyright" in response.text
    assert "2022 - 2023" in response.text
    assert "Sabrina Samuel" in response.text


def test_index_delete_all_button():
    response = app.test_client().get('/')
    assert "Delete all" in response.text
