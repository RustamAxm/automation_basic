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

Генерация тестов в рантайме из конфига
----------------------------------------------

.. code-block::

    $ pytest  src/automation_basics/test_gen_from_config --config src/automation_basics/test_gen_from_config/config.yaml
    Test session starts (platform: linux, Python 3.12.10, pytest 8.4.2, pytest-sugar 1.1.1)
    cachedir: .pytest_cache
    rootdir: /home/rustam/python-progs/automation_basic
    configfile: pyproject.toml
    plugins: xdist-3.8.0, mock-3.15.1, sugar-1.1.1, cov-7.0.0
    collected 3 items
    2026-05-13 12:22:12.507 | INFO     | automation_basics.test_gen_from_config.conftest:tmp_:19 - demo_cmd

     src/automation_basics/test_gen_from_config/test_fct_smoke.py::TestFCTSmoke.test_action[get_demo_cmd] ✓                                                                                                      33% ███▍      2026-05-13 12:22:12.509 | INFO     | automation_basics.test_gen_from_config.conftest:tmp_:19 - demo_cmd_2

     src/automation_basics/test_gen_from_config/test_fct_smoke.py::TestFCTSmoke.test_action[get_demo_cmd_2] ✓                                                                                                    67% ██████▋   2026-05-13 12:22:12.510 | INFO     | automation_basics.test_gen_from_config.conftest:tmp_:19 - demo_cmd_3

    CLOSE
     src/automation_basics/test_gen_from_config/test_fct_smoke.py::TestFCTSmoke.test_action[get_demo_cmd_3] ✓                                                                                                   100% ██████████

    Results (0.03s):
           3 passed



Проекты с unit тестами на gtest
---------------------------------
Для c/cpp юнит тестов есть пару примеров для систем сборок

`meson <https://github.com/RustamAxm/meson-test-project>`_

`cmake <https://github.com/RustamAxm/trygtest>`_
