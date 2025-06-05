UV крутой менеджер пакетов
============================
*  `ссылка на проект <https://docs.astral.sh>`_

Основная часть
----------------
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

зависимости из git репозиториев

.. code-block::

    dependencies = [
        "package-name>=0.0.0",
    ]

    [tool.uv.sources]
    package-name = { git = "link to package" }

Шаблоны проектов
------------------

    * `Репозиторий с прикольной тулой  <https://github.com/jlevy/uvinit>`_
    * `Сам шаблон <https://github.com/jlevy/simple-modern-uv>`_

Для того чтобы утилита подхватила самописный шаблон, нужно закоммитить и поставить тег. Только в этом случае изменения подхватятся.

.. code-block::

   uvx uvinit --template ./simple-modern-uv-rustam/

Далее откроется интерактивное окно.

Дополнительно
---------------

    * `pytest <https://docs.pytest.org/en/stable/index.html>`_
    * `poethepoet <https://poethepoet.natn.io/>`_
    * `dynamic version for package <https://pydevtools.com/handbook/how-to/how-to-add-dynamic-versioning-to-uv-projects/>`_
    * `pretty progress bar <https://www.geeksforgeeks.org/progress-bars-in-python/>`_
