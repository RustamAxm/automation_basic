# automation tutorial 
## intro 
Данный проект создан для ознакомления с базовыми практиками. По моему субъективному мнению полезными для AQA, физикам экспериментаторам и в целом кто хочет автоматизировать работу с устройствами будь то разработка или же исследовательский интерес. 

## Генерация документации

Для генерации rst файлов из исходников питонячих скриптов 

```bash 
uv run poe api-rst
```
Для того чтобы из этой заготовки получить html страницы 
```bash 
uv run poe html
```

## Тестирование
```bash 
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
(automation-basic) rustam@rustam-zenbook:~/Documents/automation_basic$ ll test-results/
total 12
drwxrwxr-x  2 rustam rustam 4096 Apr 17 18:28 ./
drwxrwxr-x 11 rustam rustam 4096 Apr 17 18:28 ../
-rw-rw-r--  1 rustam rustam  424 Apr 17 18:28 2025-04-17_s1744903701.xml

```