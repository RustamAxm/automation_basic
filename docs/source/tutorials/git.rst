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


