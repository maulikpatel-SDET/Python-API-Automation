"""Environment configuration loader for YAML-based API settings."""

import os
from pathlib import Path
from typing import Any

import yaml


class ConfigLoader:
    """Load and resolve environment settings from a YAML file."""

    def __init__(self, config_path: str | Path | None = None):
        """Initialize config loader.

        Args:
            config_path (str | Path | None): Optional path to YAML config file.
                If not provided, uses <project_root>/environments.yaml.
        """
        base_path = Path(__file__).resolve().parents[1]
        self.config_path = Path(config_path) if config_path else base_path / "environments.yaml"
        self.config = self._load_yaml()

    def _load_yaml(self) -> dict[str, Any]:
        """Load YAML config and return dictionary.

        Returns:
            dict[str, Any]: Parsed YAML content.
        """
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def get_active_environment_name(self, environment_name: str | None = None) -> str:
        """Resolve environment name.

        Priority:
        1. direct method argument
        2. APP_ENV environment variable
        3. default_environment in YAML

        Args:
            environment_name (str | None): Explicit environment name.

        Returns:
            str: Environment name in lowercase.
        """
        if environment_name:
            return str(environment_name).lower()

        env_value = os.getenv("APP_ENV")
        if env_value and env_value.strip():
            return env_value.strip().lower()

        return str(self.config.get("default_environment", "qa")).lower()

    def get_environment(self, environment_name: str | None = None) -> dict[str, Any]:
        """Return config for selected environment.

        Args:
            environment_name (str | None): Optional environment name.

        Returns:
            dict[str, Any]: Environment config.

        Raises:
            ValueError: If environment is not present in YAML.
        """
        env_name = self.get_active_environment_name(environment_name)
        envs = self.config.get("environments", {})

        if env_name not in envs:
            raise ValueError(f"Environment '{env_name}' not found")

        return envs[env_name]

    def get_base_url(self, environment_name: str | None = None) -> str:
        """Return base URL for environment.

        Args:
            environment_name (str | None): Optional environment name.

        Returns:
            str: Base URL.
        """
        env = self.get_environment(environment_name)
        return env.get("base_url", "")

    def build_url(self, endpoint: str, environment_name: str | None = None) -> str:
        """Build full URL from base URL and endpoint.

        Args:
            endpoint (str): Endpoint path like '/posts' or 'posts/1'.
            environment_name (str | None): Optional environment name.

        Returns:
            str: Final URL.
        """
        base_url = self.get_base_url(environment_name).rstrip("/")
        endpoint = endpoint.lstrip("/")
        return f"{base_url}/{endpoint}" if endpoint else base_url

