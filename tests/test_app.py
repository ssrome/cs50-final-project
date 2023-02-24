from app import app


def test_index_heading():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert "Upcoming" in response.text
    assert "<h1>" in response.text


def test_index_text_field():
    response = app.test_client().get('/')
    assert "<input" in response.text
    assert 'placeholder="Name"' in response.text
    assert "Name</label>" in response.text


def test_index_submit_button():
    response = app.test_client().get('/')
    assert "Add" in response.text


def test_index_footer():
    response = app.test_client().get('/')
    assert "Copyright" in response.text
    assert "2022 - 20" in response.text
    assert "Sabrina Samuel" in response.text


def test_index_delete_all_button():
    app.test_client().post('/', data={"new-item": "monster", "add-event": "Add"})
    response = app.test_client().get('/')
    assert "Delete all" in response.text


def test_add_event():
    app.test_client().post('/', data={"new-item": "pose", "add-event": "Add"})
    response = app.test_client().get('/')
    assert "pose" in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_delete_all():
    app.test_client().post('/', data={"new-item": "butterflies", "add-event": "Add"})
    app.test_client().post('/', data={"delete-all-event": "Delete all"})
    response = app.test_client().get('/')
    assert "butterflies" not in response.text


def test_delete_item():
    app.test_client().post('/', data={"new-item": "monster", "add-event": "Add"})
    app.test_client().post('/', data={"new-item": "butterflies", "add-event": "Add"})
    app.test_client().post('/', data={"delete-event": "1"})
    response = app.test_client().get('/')
    assert "butterflies" not in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_delete_first_item_in_event_list():
    app.test_client().post('/', data={"new-item": "pose", "add-event": "Add"})
    app.test_client().post('/', data={"new-item": "monster", "add-event": "Add"})
    app.test_client().post('/', data={"new-item": "butterflies", "add-event": "Add"})
    app.test_client().post('/', data={"delete-event": "0"})
    response = app.test_client().get('/')
    assert "pose" not in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_shows_complete_button():
    app.test_client().post('/', data={"new-item": "pose", "add-event": "Add"})
    response = app.test_client().get('/')
    assert "complete" in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_can_mark_an_item_complete():
    app.test_client().post('/', data={"new-item": "pose", "add-event": "Add"})
    app.test_client().post('/', data={"new-item": "monster", "add-event": "Add"})
    app.test_client().post('/', data={"complete-event": "0"})
    response = app.test_client().get('/')
    assert 'Incomplete' in response.text
    assert 'aria-label="readonly input" readonly' in response.text
    assert 'text-decoration-line-through' in response.text
    assert 'plaintext' in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_can_mark_a_complete_item_incomplete():
    app.test_client().post('/', data={"new-item": "celebrate", "add-event": "Add"})
    app.test_client().post('/', data={"complete-event": "0"})
    app.test_client().get('/')
    app.test_client().post('/', data={"incomplete-event": "0"})
    response = app.test_client().get('/')
    assert 'Incomplete' not in response.text
    assert 'aria-label="readonly input" readonly' in response.text
    assert 'Complete' in response.text
    assert 'text-decoration-line-through' not in response.text
    assert 'plaintext' not in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_it_doesnt_create_item_if_input_is_empty():
    app.test_client().post('/', data={"new-item": "", "add-event": "Add"})
    response = app.test_client().get('/')
    assert '<value="0">' not in response.text


def test_it_shows_an_error_message_if_input_is_empty_on_add():
    response = app.test_client().post('/', data={"new-item": "", "add-event": "Add"})
    assert "Please enter text in name." in response.text


def test_it_shows_completed_page():
    response = app.test_client().get('/completed')
    assert "Completed" in response.text


def test_it_shows_page_with_only_completed_items():
    app.test_client().post('/', data={"new-item": "celebrate", "add-event": "Add"})
    app.test_client().post('/', data={"new-item": "monster", "add-event": "Add"})
    app.test_client().post('/', data={"new-item": "pose", "add-event": "Add"})
    app.test_client().post('/', data={"complete-event": "0"})
    app.test_client().post('/', data={"complete-event": "1"})
    response = app.test_client().get('/completed')
    assert "celebrate" in response.text
    assert "monster" in response.text
    assert "pose" not in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_shows_edit_button():
    app.test_client().post('/', data={"new-item": "celebrate", "add-event": "Add"})
    response = app.test_client().get('/')
    assert 'Edit' in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_save_button_not_shown_on_completed_item():
    app.test_client().post('/', data={"new-item": "celebrate", "add-event": "Add"})
    app.test_client().post('/', data={"complete-event": "0"})
    response = app.test_client().post('/', data={"edit-event": "0"})
    assert 'Edit' in response.text
    assert 'Save' not in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_input_is_editable_after_pressing_edit_button():
    app.test_client().post('/', data={"new-item": "celebrate", "add-event": "Add"})
    app.test_client().post('/', data={"edit-event": "0"})
    response = app.test_client().get('/')
    assert 'aria-label="readonly input"' not in response.text
    assert 'readonly' not in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})


def test_edited_item_can_be_saved():
    app.test_client().post('/', data={"new-item": "celebrate", "add-event": "Add"})
    app.test_client().post('/', data={"edit-event": "0"})
    response = app.test_client().post('/', data={"edit-item": "monster", "save-event": "0"})
    assert 'monster' in response.text
    assert 'celebrate' not in response.text
    app.test_client().post('/', data={"delete-all-event": "Delete all"})
