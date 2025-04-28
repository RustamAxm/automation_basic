Pytest
========

Консольный пример
-----------------------------------------

.. code-block::

    (automation-basic) rustam@rustam-zenbook:~/Documents/automation_basic$ uv run poe test-demo
    Built automation-basic @ file:///home/rustam/Documents/automation_basic
    Uninstalled 1 package in 1ms
    Installed 1 package in 3ms
    Poe => uv run pytest -vs automation_basics/test_demo/
    =================================================================================================== test session starts ===================================================================================================
    platform linux -- Python 3.12.3, pytest-8.3.5, pluggy-1.5.0 -- /home/rustam/Documents/automation_basic/.venv/bin/python3
    cachedir: .pytest_cache
    rootdir: /home/rustam/Documents/automation_basic
    configfile: pyproject.toml
    collected 2 items

    automation_basics/test_demo/test_demo.py::test_randon val=0.5140455188138412
    PASSED
    automation_basics/test_demo/test_demo.py::test_randon_false val=0.33228701646396275
    PASSED

Тут есть момент с тем что фикстура будет вызываться каждый раз, для того чтобы это отключить нужно пробросить параметр

.. code-block::

    @fixture(scope="session")
    def get_testing_data():

Результаты в xml удобно сохранить и отправить в какой нибудь `allure <https://allurereport.org/>`_

.. code-block::

    (automation-basic) rustam@rustam-zenbook:~/Documents/automation_basic$ ll test-results/
    total 12
    drwxrwxr-x  2 rustam rustam 4096 Apr 17 18:28 ./
    drwxrwxr-x 11 rustam rustam 4096 Apr 17 18:28 ../
    -rw-rw-r--  1 rustam rustam  424 Apr 17 18:28 2025-04-17_s1744903701.xml

Опции для работы и конфигурации
----------------------------------

Для дополнительных опций `можно добавлять в томл <https://docs.pytest.org/en/stable/reference/customize.html>`_

.. code-block::

    [tool.pytest.ini_options]
    minversion = "6.0"
    addopts = "-vvs"
    testpaths = [
        "automation_basics/test_demo",
    ]

`Контроль ошибок и предупреждений <https://docs.pytest.org/en/stable/how-to/capture-warnings.html>`_
