"""API automation tests for the public JsonPlaceholder service."""

import os
from utils.api_client import ApiClient
from page_objects.jsonplaceholder_page import JsonPlaceholderPage


def get_page() -> JsonPlaceholderPage:
    """Create a page object using the active environment configuration.
    
    Args:
        None
    
    Returns:
        JsonPlaceholderPage: Page object with client configured for the active environment.
        
    Notes:
        Environment selection priority:
        1. APP_ENV environment variable
        2. default_environment from environments.yaml
    """
    env_name = os.getenv("APP_ENV") or None
    client = ApiClient(environment_name=env_name)
    return JsonPlaceholderPage(client)


def test_get_all_posts_returns_200_and_list_data():
    """Verify the posts endpoint responds with a valid list."""
    response = get_page().get_all_posts()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_post_by_id_returns_expected_post():
    """Verify a specific post contains the required fields."""
    response = get_page().get_post_by_id(1)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_get_comments_for_specific_post_returns_related_comments():
    """Verify comments for a post are returned and linked to the correct post ID."""
    response = get_page().get_comments_for_post(1)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["postId"] == 1


def test_create_post_returns_201_and_created_payload():
    """Verify a new post can be created and returns the created payload."""
    page = get_page()
    response = page.create_post(title="New API Test", body="This is a test post", user_id=7)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "New API Test"
    assert data["body"] == "This is a test post"
    assert data["userId"] == 7


def test_update_post_returns_200_and_updated_values():
    """Verify an existing post can be updated successfully."""
    page = get_page()
    response = page.update_post(post_id=1, title="Updated Title", body="Updated Body", user_id=9)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Updated Title"
    assert data["body"] == "Updated Body"
    assert data["userId"] == 9


def test_delete_post_returns_200_or_404_for_jsonplaceholder():
    """Delete endpoint may respond with 200 or 404 depending on service behavior."""
    response = get_page().delete_post(1)
    assert response.status_code in (200, 404)


def test_get_all_albums_returns_200_and_album_list():
    """Verify the albums endpoint returns a non-empty list."""
    response = get_page().get_all_albums()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_album_by_id_returns_valid_album_details():
    """Verify album details contain the expected fields and identifiers."""
    response = get_page().get_album_by_id(2)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 2
    assert "title" in data
    assert data["userId"] == 1


def test_get_all_todos_returns_200_and_pending_items():
    """Verify the todos endpoint returns the expected collection."""
    response = get_page().get_all_todos()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "completed" in data[0]


def test_get_user_by_id_returns_valid_user_details():
    """Verify a user resource includes key identity-related fields."""
    response = get_page().get_user_by_id(5)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 5
    assert "name" in data
    assert "email" in data
