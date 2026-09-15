"""Reusable API client for environment-aware REST calls."""

from __future__ import annotations

from typing import Any

import requests

from utils.config_loader import ConfigLoader


class ApiClient:
    """Send HTTP requests using the active environment configuration."""

    def __init__(self, environment_name: str | None = None, config_path: str | None = None):
        """Initialize the client with the selected environment.

        Args:
            environment_name: Optional environment key to use (overrides APP_ENV).
            config_path: Optional path to the environments YAML file.

        Returns:
            None
        """
        self.config_loader = ConfigLoader(config_path)
        self.environment_name = self.config_loader.get_active_environment_name(environment_name)
        self.environment = self.config_loader.get_environment(self.environment_name)

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> requests.Response:
        """Send a GET request.

        Args:
            endpoint: API endpoint path (e.g. '/posts').
            params: Optional query parameters to include in the request.
            headers: Optional headers to merge with environment headers.

        Returns:
            requests.Response: The HTTP response object.
        """
        return self.request("GET", endpoint, params=params, headers=headers, **kwargs)

    def post(
        self,
        endpoint: str,
        payload: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> requests.Response:
        """Send a POST request.

        Args:
            endpoint: API endpoint path (e.g. '/posts').
            payload: JSON-serializable body to send as the request body.
            params: Optional query parameters.
            headers: Optional headers to merge with environment headers.

        Returns:
            requests.Response: The HTTP response object.
        """
        return self.request("POST", endpoint, payload=payload, params=params, headers=headers, **kwargs)

    def put(
        self,
        endpoint: str,
        payload: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> requests.Response:
        """Send a PUT request.

        Args:
            endpoint: API endpoint path.
            payload: JSON payload for the PUT request.
            params: Optional query parameters.
            headers: Optional headers to merge with environment headers.

        Returns:
            requests.Response: The HTTP response object.
        """
        return self.request("PUT", endpoint, payload=payload, params=params, headers=headers, **kwargs)

    def delete(
        self,
        endpoint: str,
        payload: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> requests.Response:
        """Send a DELETE request.

        Args:
            endpoint: API endpoint path.
            payload: Optional JSON payload to include with the request.
            params: Optional query parameters.
            headers: Optional headers to merge with environment headers.

        Returns:
            requests.Response: The HTTP response object.
        """
        return self.request("DELETE", endpoint, payload=payload, params=params, headers=headers, **kwargs)

    def request(
        self,
        method: str,
        endpoint: str,
        payload: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> requests.Response:
        """Build the URL, merge headers, and execute the HTTP call.

        Args:
            method: HTTP method name (GET, POST, PUT, DELETE, etc.).
            endpoint: Endpoint path to call (may be absolute path part).
            payload: Optional JSON body to send.
            params: Optional query parameters.
            headers: Optional headers to merge with environment headers.

        Returns:
            requests.Response: The HTTP response from `requests`.
        """
        url = self.config_loader.build_url(endpoint, self.environment_name)
        final_headers = self.environment.get("headers", {}).copy()
        if headers:
            final_headers.update(headers)

        timeout = kwargs.pop("timeout", self.environment.get("timeout", 10))
        return requests.request(
            method=method.upper(),
            url=url,
            json=payload,
            params=params,
            headers=final_headers,
            timeout=timeout,
            **kwargs,
        )
