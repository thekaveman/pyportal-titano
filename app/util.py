import os


def bytes_str(buffer: bytes) -> str:
    """Decode bytes into a utf-8 string."""
    return str(buffer, "utf-8")


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


def mac_str(buffer: bytearray) -> str:
    """Converts a MAC address bytearray into the familiar string format."""
    return ":".join(reversed([hex(i).lstrip("0x") for i in buffer]))
