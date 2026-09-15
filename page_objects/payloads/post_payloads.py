"""Payload builders for JsonPlaceholder post operations."""


def create_post_payload(title: str, body: str, user_id: int = 1) -> dict[str, str | int]:
    """Create a payload for creating a new post.

    Args:
        title: Title text for the post.
        body: Body text for the post.
        user_id: ID of the user creating the post.

    Returns:
        dict: Payload suitable for JSON serialization.
    """
    return {
        "title": title,
        "body": body,
        "userId": user_id,
    }


def update_post_payload(post_id: int, title: str, body: str, user_id: int = 1) -> dict[str, str | int]:
    """Create a payload for updating an existing post.

    Args:
        post_id: Identifier for the post to update.
        title: New title text.
        body: New body text.
        user_id: Associated user ID.

    Returns:
        dict: Payload suitable for JSON serialization.
    """
    return {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": user_id,
    }
