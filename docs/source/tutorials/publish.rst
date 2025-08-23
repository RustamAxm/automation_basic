Публикация документации
=========================

Генеарция rst из докстрингов
------------------------------

.. code-block::

    uv run poe api-rst


Генерация HTML
-------------------

.. code-block::

    uv run poe html

Публикация PDF
-------------------

На основе плагина `simplepdf <https://sphinx-simplepdf.readthedocs.io/en/latest/>`_  документация публикуется в pdf.

В нашем проекте достаточно прописать

.. code-block::

    uv run poe pdf

Публикация markdown
------------------------

На основе пакета и фичей `sphinx-markdown-builder <https://pypi.org/project/sphinx-markdown-builder/>`_

На основе проекта

.. code-block::

    uv run poe md

Публикация в CI
------------------
Для публикации нужно поместить генеренные файлы в общее хранилище как stage в CI

* `Minio <https://min.io/>`_

Есть вариант с github, но требуется поместить в индекс генеренные HTML