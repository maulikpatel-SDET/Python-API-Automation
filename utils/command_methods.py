"""Utility wrapper methods for common HTTP operations."""

from __future__ import annotations

from urllib.parse import urljoin

import requests


class CommandMethods:
    """Thin wrappers around requests methods for reusable API operations."""

    @staticmethod
    def build_url(base_url: str, endpoint: str) -> str:
        """Join a base URL and endpoint into one valid URL.

        Args:
            base_url: The base URL (e.g. 'https://api.example.com').
            endpoint: Endpoint path to append to the base URL.

        Returns:
            str: The combined URL.
        """
        base = base_url.rstrip("/") + "/"
        return urljoin(base, endpoint.lstrip("/"))

    @staticmethod
    def get(
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        timeout: int = 10,
    ):
        """Perform a GET request.

        Args:
            url: Full URL to call.
            headers: Optional headers to send.
            params: Optional query parameters.
            timeout: Request timeout in seconds.

        Returns:
            requests.Response: The HTTP response object.
        """
        return requests.get(url, headers=headers, params=params, timeout=timeout)

    @staticmethod
    def post(
        url: str,
        payload: dict | None = None,
        headers: dict | None = None,
        params: dict | None = None,
        timeout: int = 10,
    ):
        """Perform a POST request.

        Args:
            url: Full URL to call.
            payload: JSON-serializable body to include.
            headers: Optional headers to send.
            params: Optional query parameters.
            timeout: Request timeout in seconds.

        Returns:
            requests.Response: The HTTP response object.
        """
        return requests.post(url, json=payload, headers=headers, params=params, timeout=timeout)

    @staticmethod
    def put(
        url: str,
        payload: dict | None = None,
        headers: dict | None = None,
        params: dict | None = None,
        timeout: int = 10,
    ):
        """Perform a PUT request.

        Args:
            url: Full URL to call.
            payload: JSON-serializable body to include.
            headers: Optional headers to send.
            params: Optional query parameters.
            timeout: Request timeout in seconds.

        Returns:
            requests.Response: The HTTP response object.
        """
        return requests.put(url, json=payload, headers=headers, params=params, timeout=timeout)

    @staticmethod
    def delete(
        url: str,
        payload: dict | None = None,
        headers: dict | None = None,
        params: dict | None = None,
        timeout: int = 10,
    ):
        """Perform a DELETE request.

        Args:
            url: Full URL to call.
            payload: Optional JSON body to include.
            headers: Optional headers to send.
            params: Optional query parameters.
            timeout: Request timeout in seconds.

        Returns:
            requests.Response: The HTTP response object.
        """
        return requests.delete(url, json=payload, headers=headers, params=params, timeout=timeout)
