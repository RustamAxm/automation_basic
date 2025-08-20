Удаленное взаимодействие
===========================
В данном отрывке рассмотрим случаи когда нужно взаимодействовать с устройством,
которое находится на другом хосте различными способами

rest api
-----------
Пример как можно завернуть класс с нормальным интерфейсом в api.

Сервер

.. code-block::

    def get_str_to_api_post(device, method):
        str_ = f"""
    @router.post("/{device}/{method}")
    async def {method}(request: Request):
        try:
            kwargs_ = await request.json()
            logger.debug(kwargs_)
            ret = {device}.{method}(**kwargs_)
            return {'{'} 'ret': ret {'}'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"{'{'}e{'}'}")
        """

        return str_

клиент

.. code-block::

    def get_client_to_api_post(device, method, args_tr, tmp_d, doc_):
        docs_q = '"""\n'
        str_ = f"""
        def {method}({args_tr}):
            {docs_q}{doc_}\n        {docs_q}
            url = f"{'{'}self.base_url{'}'}/api/v1/{device}/{method}"
            tmp_d = {tmp_d}
            try:
                response = requests.post(
                    url,
                    data=json.dumps(tmp_d),
                    headers={'{'}'content-type': 'application/json'{'}'},
                    timeout=10,
                    )
                response.raise_for_status()
                return response.json()['ret']
            except requests.exceptions.RequestException as e:
                raise Exception(f"Ошибка при получении данных: {'{'}e{'}'}")
        """

        return str_

usb to ip
-------------

Данный способ удобен когда требуется удаленно управлять устройством с физическим usb.
`Подробнее описано в репозитории <https://github.com/RustamAxm/sh_scripts/tree/main/usb_to_ip>`_

zmq
------------------
Удобная библиотека для взаимодействия по сети с различными сценариями и языками.
`ссылка на проект <https://zeromq.org/get-started/>`_

Пример для взаимодействия в сабпроекте automation_basics/zmq_demo

GRPC
--------------
Стильно модно и молодежно.
`Пример в репе на python <https://github.com/RustamAxm/grpc-test-project>`_

kafka
--------
Если мы начинаем говорить не о поделках как в zmq в широковещательном режиме,
и где не требуется немедленного ответа, стоит рассмотреть для обмена сообщениями сервис kafka

`Пример взаимодействия на разных языках в репозитории <https://github.com/RustamAxm/kafka-demo>`_

Работа с удаленным хостом
--------------------------
Самый удобный вариант рассмотреть `paramiko <https://www.paramiko.org/index.html>`_

`Неплохая дока для начала <https://pydocs.ru/python-paramiko/>`_