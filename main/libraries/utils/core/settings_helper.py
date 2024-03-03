import os
from dotenv import load_dotenv


def load_environment(env: str) -> None:
    """
    Load environment variables from a .env file.

    :param env: The environment to load. Should be one of 'dev', 'hml', 'prd'.
    """
    if env is None or env.strip() == "":
        env = "dev"
    env_file = f".env.{env}.env"
    if not os.path.exists(env_file):
        raise Exception(f"Environment file {env_file} does not exist.")
    load_dotenv(dotenv_path=env_file)

def get_all() -> dict:
    """
    Get all environment variables.

    :return: A dictionary of all environment variables.
    """
    return os.environ

def get(key: str) -> str:
    """
    Get the value of an environment variable.

    :param key: The name of the environment variable to get.
    :return: The value of the environment variable.
    """
    return os.getenv(key)

def set(key: str, value: str) -> None:
    """
    Set the value of an environment variable.

    :param key: The name of the environment variable to set.
    :param value: The value to set the environment variable to.
    """
    os.environ[key] = value

def delete(key: str) -> None:
    """
    Delete an environment variable.

    :param key: The name of the environment variable to delete.
    """
    if key in os.environ:
        del os.environ[key]
