"""Page object for user-related API operations."""

from __future__ import annotations

from utils.api_client import ApiClient
from page_objects.payloads.user_payloads import create_user_payload, get_user_payload


class UserApiPage:
    """Encapsulate user API actions in a reusable page object."""

    def __init__(self, client: ApiClient):
        """Store the API client used by this page object."""
        self.client = client

    def get_user(self, user_id: int = 1):
        """Fetch a user by ID.

        Args:
            user_id: Identifier of the user to retrieve.

        Returns:
            requests.Response: HTTP response containing the user object.
        """
        params = get_user_payload(user_id)
        return self.client.get(f"/users/{user_id}", params=params)

    def create_user(self, name: str = "Alice", job: str = "QA Engineer"):
        """Create a new user with the provided values.

        Args:
            name: User's name.
            job: User's job title.

        Returns:
            requests.Response: HTTP response for the create operation.
        """
        payload = create_user_payload(name=name, job=job)
        return self.client.post("/users", payload=payload)

    def update_user(self, user_id: int = 1, name: str = "Alice", job: str = "QA Lead"):
        """Update an existing user.

        Args:
            user_id: Identifier of the user to update.
            name: New name for the user.
            job: New job title for the user.

        Returns:
            requests.Response: HTTP response for the update operation.
        """
        payload = create_user_payload(name=name, job=job)
        return self.client.put(f"/users/{user_id}", payload=payload)
