"""Example user API tests for the automation framework."""

import os

from utils.api_client import ApiClient
from page_objects.user_api_page import UserApiPage


def test_user_api_page_can_fetch_user():
    """Verify the user retrieval page object returns a successful response."""
    env_name = os.getenv("APP_ENV") or None
    client = ApiClient(environment_name=env_name)
    user_page = UserApiPage(client)
    response = user_page.get_user(user_id=1)
    assert response.status_code == 200


def test_user_api_page_can_create_user():
    """Verify the user creation page object returns a success response."""
    env_name = os.getenv("APP_ENV") or None
    client = ApiClient(environment_name=env_name)
    user_page = UserApiPage(client)
    response = user_page.create_user(name="Alice", job="QA Engineer")
    assert response.status_code == 201
