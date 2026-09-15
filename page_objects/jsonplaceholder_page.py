"""Page object for JsonPlaceholder REST API actions."""

from __future__ import annotations

from utils.api_client import ApiClient
from page_objects.payloads.post_payloads import create_post_payload, update_post_payload


class JsonPlaceholderPage:
    """Encapsulate API operations for posts, albums, todos, and users."""

    def __init__(self, client: ApiClient):
        """Store the configured API client for this page object."""
        self.client = client

    def get_all_posts(self):
        """Fetch all posts.

        Args:
            None

        Returns:
            requests.Response: HTTP response containing a list of posts.
        """
        return self.client.get("/posts")

    def get_post_by_id(self, post_id: int):
        """Fetch a specific post by ID.

        Args:
            post_id: Identifier of the post to retrieve.

        Returns:
            requests.Response: HTTP response containing the post object.
        """
        return self.client.get(f"/posts/{post_id}")

    def get_comments_for_post(self, post_id: int):
        """Fetch comments for a specific post.

        Args:
            post_id: Identifier of the post whose comments will be fetched.

        Returns:
            requests.Response: HTTP response containing a list of comments.
        """
        return self.client.get("/comments", params={"postId": post_id})

    def create_post(self, title: str, body: str, user_id: int = 1):
        """Create a new post.

        Args:
            title: Title text for the post.
            body: Body text for the post.
            user_id: ID of the user creating the post.

        Returns:
            requests.Response: HTTP response for the create operation.
        """
        payload = create_post_payload(title=title, body=body, user_id=user_id)
        return self.client.post("/posts", payload=payload)

    def update_post(self, post_id: int, title: str, body: str, user_id: int = 1):
        """Update an existing post.

        Args:
            post_id: Identifier of the post to update.
            title: New title text.
            body: New body text.
            user_id: User ID associated with the post.

        Returns:
            requests.Response: HTTP response for the update operation.
        """
        payload = update_post_payload(post_id=post_id, title=title, body=body, user_id=user_id)
        return self.client.put(f"/posts/{post_id}", payload=payload)

    def delete_post(self, post_id: int):
        """Delete a post.

        Args:
            post_id: Identifier of the post to delete.

        Returns:
            requests.Response: HTTP response for the delete operation.
        """
        return self.client.delete(f"/posts/{post_id}")

    def get_all_albums(self):
        """Fetch all albums.

        Args:
            None

        Returns:
            requests.Response: HTTP response containing a list of albums.
        """
        return self.client.get("/albums")

    def get_album_by_id(self, album_id: int):
        """Fetch a specific album by ID.

        Args:
            album_id: Identifier of the album to retrieve.

        Returns:
            requests.Response: HTTP response containing the album object.
        """
        return self.client.get(f"/albums/{album_id}")

    def get_all_todos(self):
        """Fetch all todos.

        Args:
            None

        Returns:
            requests.Response: HTTP response containing a list of todos.
        """
        return self.client.get("/todos")

    def get_todo_by_id(self, todo_id: int):
        """Fetch a specific todo by ID.

        Args:
            todo_id: Identifier of the todo to retrieve.

        Returns:
            requests.Response: HTTP response containing the todo object.
        """
        return self.client.get(f"/todos/{todo_id}")

    def get_all_users(self):
        """Fetch all users.

        Args:
            None

        Returns:
            requests.Response: HTTP response containing a list of users.
        """
        return self.client.get("/users")

    def get_user_by_id(self, user_id: int):
        """Fetch a specific user by ID.

        Args:
            user_id: Identifier of the user to retrieve.

        Returns:
            requests.Response: HTTP response containing the user object.
        """
        return self.client.get(f"/users/{user_id}")
