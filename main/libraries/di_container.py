from dependency_injector import providers, containers
from main.libraries.tools.core.log_tool import LogTool
from main.libraries.adapters.integrators.core.role_interpreter import RoleInterpreter
from main.libraries.tools.core.settings_tool import SettingsTool


class Container(containers.DeclarativeContainer):
    """
    Container class for dependency injection.

    This class extends the `containers.DeclarativeContainer` class from the `dependency_injector` module.
    It provides instances for each services of the system.
    """

    # Tools
    settings_tool = providers.Factory(SettingsTool)
    log_tool = providers.Factory(LogTool, settings_tool=settings_tool)

    # Adapters
    role_interpreter = providers.Factory(RoleInterpreter, settings_tool=settings_tool, logger=log_tool)

    # Wiring
    wiring_config = containers.WiringConfiguration(
        modules=[
            "main.apps.microservice.controllers.character_controller",
        ]
    )
