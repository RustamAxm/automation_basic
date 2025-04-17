RUFF linter как добавить в проект
===================================
*  `ссылка на проект <https://docs.astral.sh/ruff/>`_

Настройка в проекте

.. code-block::

    uv add ruff --dev

Добавляем основные правила в pyproject.toml

.. code-block::

    [tool.ruff.lint]
    select = [
        # pycodestyle
        "E",
        # Pyflakes
        "F",
        # pyupgrade
        "UP",
        # flake8-bugbear
        "B",
        # flake8-simplify
        "SIM",
        # isort
        "I",
    ]


