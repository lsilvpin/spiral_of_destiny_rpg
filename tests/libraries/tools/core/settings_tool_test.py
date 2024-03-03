import pytest
from main.libraries.di_container import Container
from main.libraries.tools.core.settings_tool import SettingsTool

@pytest.fixture
def settings_tool():
    container = Container()
    return container.settings_tool()

def test_should_load_environment(settings_tool):
    env = "dev"
    settings_tool.load_env(env)
    assert settings_tool.get_current_env() == env
    assert settings_tool.is_env_loaded() is True

def test_should_get_some_environment_variable(settings_tool):
    key = "SOME_KEY"
    value = "some_value"
    settings_tool.set(key, value)
    assert settings_tool.get(key) == value
    settings_tool.delete(key)

def test_should_load_env_then_check_is_loaded(settings_tool):
    env = "dev"
    settings_tool.load_env(env)
    assert settings_tool.is_env_loaded() is True

def test_should_load_env_then_get_env_and_compare(settings_tool):
    env = "dev"
    settings_tool.load_env(env)
    assert settings_tool.get_current_env() == env

def test_should_do_entire_crud_of_a_environment_variable(settings_tool):
    key = "SOME_KEY"
    value = "some_value"
    updated_value = "updated_value"
    assert settings_tool.get(key) is None
    settings_tool.set(key, value)
    assert settings_tool.get(key) == value
    settings_tool.set(key, updated_value)
    assert settings_tool.get(key) == updated_value
    settings_tool.delete(key)
    assert settings_tool.get(key) is None

def test_should_create_three_env_vars_read_all_and_delete_all(settings_tool):
    key1 = "KEY1"
    value1 = "VALUE1"
    key2 = "KEY2"
    value2 = "VALUE2"
    key3 = "KEY3"
    value3 = "VALUE3"
    settings_tool.set(key1, value1)
    settings_tool.set(key2, value2)
    settings_tool.set(key3, value3)
    assert settings_tool.get(key1) == value1
    assert settings_tool.get(key2) == value2
    assert settings_tool.get(key3) == value3
    all_vars = settings_tool.get_all()
    assert all_vars[key1] == value1
    assert all_vars[key2] == value2
    assert all_vars[key3] == value3
    settings_tool.delete(key1)
    settings_tool.delete(key2)
    settings_tool.delete(key3)
    assert settings_tool.get(key1) is None
    assert settings_tool.get(key2) is None
    assert settings_tool.get(key3) is None
    all_vars = settings_tool.get_all()
    with pytest.raises(KeyError):
        all_vars[key1]
    with pytest.raises(KeyError):
        all_vars[key2]
    with pytest.raises(KeyError):
        all_vars[key3]

def test_should_get_openai_api_key(settings_tool):
    key = "OPENAI_API_KEY"
    value = settings_tool.get(key)
    assert value is not None

def test_should_get_openai_org_id(settings_tool):
    key = "OPENAI_ORG_ID"
    value = settings_tool.get(key)
    assert value is not None
