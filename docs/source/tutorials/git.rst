git заметки
==============
заметки по гит

База
-------
ребейз в интерактивном режиме осносительно себя позволяет перечень коммитов отредактировать

.. code-block::

    git rebase -i HEAD~3

установка нескольких репозиториев для одного проекта

.. code-block::

    git remote -v
    git remote add <name_for_remote> <link>

Красивый вывод истории
------------------------

Для истории коммитов отредактировать ~/.gitconfig

.. code-block::

    [alias]
    lg1 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(auto)%d%C(reset)' --all
    lg2 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(white)%s%C(reset) %C(dim white)- %an%C(reset)'
    lg = lg1

Пример вывода

.. code-block::

    git lg

Конфликты
------------

Не совпадение коммитов с remote

Создаем временную ветку

.. code-block::

    git checkout -b tmp
    git switch <prev branch>

Далее ресет на нужное количество коммитов, забираем разницу из удаленного репозитория, далее забираем коммиты которые отличались.

.. code-block::

    git reset --hard HEAD~3
    git pull
    git cherry-pick tmp

tags
-------

Создание тега 

.. code-block::

   git tag v0.1.0

Отправка всех тегов в remote

.. code-block::

   git push --tags 


Отправка одного тега 

.. code-block::

   git push <remote-name> tag <tag>

Pre-commit
------------

Удобно при каждом коммите проверять состояние репозитория. Заполняем .pre-commit-config.yaml

.. code-block::

    repos:
    - repo: local
      hooks:
        - id: check-json
          name: json check
          entry: "uv run check-json"
          language: system
          files: .json

        - id: check-yaml
          name: yaml check
          entry: "uv run check-yaml"
          language: system
          files: .yaml

        - id: check-toml
          name: toml check
          entry: "uv run check-toml"
          language: system
          files: .toml

        - id: check-xml
          name: xml check
          entry: "uv run check-xml"
          language: system
          files: .xml

        - id: linter
          name: Linter check
          entry: "uv run poe linter"
          language: system
          types: [ python ]
          pass_filenames: false

Настраиваем в проекте

.. code-block::

    uv run pre-commit install

Далее при коммите вызываются проверки

.. code-block::

    $ git commit -m 'fix rst '
    json check...........................................(no files to check)Skipped
    yaml check...........................................(no files to check)Skipped
    toml check...............................................................Passed
    xml check............................................(no files to check)Skipped
    Linter check.............................................................Passed

Редактироавние коммитов
------------------------------

Отключаем прекоммит хук

.. code-block::

    uv run pre-commit uninstall

Пример изменения автора коммита

.. code-block::

    git rebase --onto HEAD~29 --exec "git commit --amend --reset-author --no-edit" HEAD~29

