from {{ cookiecutter.project_slug }}.{{ cookiecutter.module_name }} import inc


def test_answer():
    assert inc(3) == 5

