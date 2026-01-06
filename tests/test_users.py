# test_models.py
import pytest


@pytest.mark.django_db
def test_project_duration(create_test_user) -> None:  # use the project fixture as a param
    assert create_test_user.username == "testuser"
