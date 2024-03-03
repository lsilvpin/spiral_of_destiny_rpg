
from main.libraries.utils.core.settings_helper import get, set, load_environment, delete, get_all


class SettingsTool:
    """
    A tool for managing environment settings and retrieving environment variables.
    """

    __env: str = "dev"
    __isLoaded: bool = False

    def load_env(self, env: str) -> None:
        """
        Load environment variables from a .env file.

        :param env: The environment to load. Should be one of 'dev', 'hml', 'prd'.
        """
        self.__env = env
        load_environment(self.__env)
        self.__isLoaded = True

    def is_env_loaded(self) -> bool:
        """
        Check if the environment has been loaded.

        :return: True if the environment has been loaded, False otherwise.
        """
        return self.__isLoaded

    def get_current_env(self) -> str:
        """
        Get the current environment.

        :return: The current environment.
        """
        return self.__env

    def get_all(self) -> dict:
        """
        Get all environment variables.

        :return: A dictionary of all environment variables.
        """
        if not self.__isLoaded:
            self.load_env(self.__env)
        return get_all()

    def get(self, key: str) -> str:
        """
        Get the value of an environment variable.

        :param key: The name of the environment variable to get.
        :return: The value of the environment variable.
        """
        if not self.__isLoaded:
            self.load_env(self.__env)
        return get(key)

    def set(self, key: str, value: str) -> None:
        """
        Set the value of an environment variable.

        :param key: The name of the environment variable to set.
        :param value: The value to set the environment variable to.
        """
        set(key, value)

    def delete(self, key: str) -> None:
        """
        Delete an environment variable.

        :param key: The name of the environment variable to delete.
        """
        delete(key)
