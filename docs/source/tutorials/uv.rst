UV крутой менеджер пакетов
============================
*  `ссылка на проект <https://docs.astral.sh>`_

Установка в ubuntu 24.04

.. code-block::

    sudo snap install uv

создание проекта

.. code-block::

    uv init --lib my-module

добавить пакет

.. code-block::

    uv add numpy
    uv add pytest --dev
    uv add poethepoet

удобный скриптинг через poethepoet, далее добавляем в toml

.. code-block::

    [tool.poe.tasks]
    html.shell = "rm -fr docs/build && uv run sphinx-build -M html docs/source docs/build"
    api-rst.shell = "rm -fr docs/source/api && uv run sphinx-apidoc -o docs/source/api automation_basics/"
    test-demo.shell = "pytest -vs --junitxml=test-results/$(date '+%F_s%s').xml automation_basics/test_demo/ "


Additional
--------------

    * `pytest <https://docs.pytest.org/en/stable/index.html>`_
    * `poethepoet <https://poethepoet.natn.io/>`_