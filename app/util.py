import os


def get_env(key: str, default=None, cast=None) -> str | int:
    """Gets an environment variable.

    Args:
        key: The name of the environment variable to get.

        default: A default value if the environment variable is not found, defaults to None.

        cast: A return type for the value, defaults to the settings.toml type (str or int).

    Returns:
        The environment variable value,
    """
    value = os.getenv(key, default)
    if cast is bool:
        return value.lower() == "true"
    else:
        return cast(value) if cast else value
