"""Payload builders for user-related API requests."""


def get_user_payload(user_id: int = 1) -> dict[str, int]:
    """Create a payload used for fetching a user resource.

    Args:
        user_id: Identifier of the user.

    Returns:
        dict: Query parameters for user retrieval.
    """
    return {"userId": user_id}


def create_user_payload(name: str = "Alice", job: str = "QA Engineer") -> dict[str, str]:
    """Create a payload for creating a user.

    Args:
        name: User's display name.
        job: Job or title string.

    Returns:
        dict: Payload suitable for user create calls.
    """
    return {
        "name": name,
        "job": job,
    }
