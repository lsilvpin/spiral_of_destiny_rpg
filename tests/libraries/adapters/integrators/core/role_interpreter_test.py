import pytest

from main.libraries.di_container import Container


@pytest.fixture
def role_interpreter():
    container = Container()
    return container.role_interpreter()


def test_should_load_settings(role_interpreter):
    role = "admin"
    role_interpreter.load(role)
    assert role_interpreter.get_role() == role

@pytest.mark.skip(reason="This test integrates with OpenAI API and has costs.")
def test_should_prompt_user(role_interpreter):
    role = "Rick, da série Rick and Morty"
    role_interpreter.load(role)
    msg = "Fala Rick, como você faria para resolver o problema da fome no mundo?"
    response = role_interpreter.prompt(msg)
    assert response is not None
    print(response)
