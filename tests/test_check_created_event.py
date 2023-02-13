from src.check_created_event import CheckCreatedEvent


def test_return_is_not_none():
    assert CheckCreatedEvent is not None


def test_return_is_false_when_nothing_is_sent():
    assert CheckCreatedEvent().check_created_event() is False


def test_return_is_false_when_empty_string_is_sent():
    assert CheckCreatedEvent.check_created_event("") is False


def test_return_is_true_when_string_is_sent():
    assert CheckCreatedEvent.check_created_event("hello") is True
