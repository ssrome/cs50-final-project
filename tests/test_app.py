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
    assert "Add" in response.text


def test_index_footer():
    response = app.test_client().get('/')
    assert "Copyright" in response.text
    assert "2022 - 2023" in response.text
    assert "Sabrina Samuel" in response.text


def test_index_delete_all_button():
    response = app.test_client().get('/')
    assert "Delete all" in response.text


def test_add_event():
    app.test_client().post('/', data={"add-event": "Add", "new-event": "monster"})
    response = app.test_client().get('/')
    assert "monster" in response.text


def test_delete_all():
    app.test_client().post('/', data={"delete-all": "Delete All"})
    response = app.test_client().get('/')
    assert "monster" not in response.text


def test_delete_item():
    app.test_client().post('/', data={"add-event": "Add", "new-event": "monster"})
    app.test_client().post('/', data={"add-event": "Add", "new-event": "butterflies"})
    app.test_client().post('/', data={"delete-event": "1"})
    response = app.test_client().get('/')
    assert "butterflies" not in response.text
    app.test_client().post('/', data={"delete-all": "Delete All"})


def test_delete_first_item_in_event_list():
    app.test_client().post('/', data={"add-event": "Add", "new-event": "pose"})
    app.test_client().post('/', data={"add-event": "Add", "new-event": "monster"})
    app.test_client().post('/', data={"add-event": "Add", "new-event": "butterflies"})
    app.test_client().post('/', data={"delete-event": "0"})
    response = app.test_client().get('/')
    assert "pose" not in response.text
    app.test_client().post('/', data={"delete-all": "Delete All"})
