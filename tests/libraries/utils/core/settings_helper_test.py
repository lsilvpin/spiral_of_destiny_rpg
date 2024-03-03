import sys, os, pytest

sys.path.insert(0, os.path.abspath("."))
from main.libraries.utils.core.settings_helper import load_environment, get, set, get_all, delete


def setup_function(function):
    # Create .env files for testing
    os.environ.clear()
    with open(".env.test1.env", "w") as f:
        f.write("TEST_VARIABLE=test1\n")
    with open(".env.test2.env", "w") as f:
        f.write("TEST_VARIABLE=test2\n")


def teardown_function(function):
    # Remove .env files after testing
    os.remove(".env.test1.env")
    os.remove(".env.test2.env")


def test_should_load_test1_environment_variables_from_file():
    # Test loading .env.test1.env
    load_environment("test1")
    assert get("TEST_VARIABLE") == "test1"
    # First variables should not be overwritena
    load_environment("test2")
    assert get("TEST_VARIABLE") == "test1"


def test_should_load_test2_environment_variables_from_file():
    # Test loading .env.test2.env
    load_environment("test2")
    assert get("TEST_VARIABLE") == "test2"
    # First variables should not be overwriten
    load_environment("test1")
    assert get("TEST_VARIABLE") == "test2"


def test_should_raise_exception_when_env_file_does_not_exist():
    with pytest.raises(Exception):
        load_environment("nonexistent")


def test_should_get_all_environment_variables():
    os.environ["KEY1"] = "VALUE1"
    os.environ["KEY2"] = "VALUE2"
    result = get_all()
    assert result["KEY1"] == "VALUE1"
    assert result["KEY2"] == "VALUE2"


def test_should_get_environment_variable_value():
    os.environ["KEY"] = "VALUE"
    result = get("KEY")
    assert result == "VALUE"


def test_should_set_environment_variable_value():
    set("KEY", "VALUE")
    value = get("KEY")
    assert value == "VALUE"

def test_should_delete_environment_variable():
    set("KEY", "VALUE")
    assert get("KEY") == "VALUE"
    delete("KEY")
    assert get("KEY") is None
    assert "KEY" not in os.environ
