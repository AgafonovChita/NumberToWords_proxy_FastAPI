<b>Способ 1. Запуск в конктейнере</b><p>
1.Установить Docker и Docker-compose<p>
2.Клонировать репозиторий <code>git clone https://github.com/AgafonovChita/proxy_project.git </code><p>
3.Перейти в рабочую директорию <code>cd proxy_project</code><p>
4.Запустить контейнер <code>make run</code><p>
5.Приложение станет доступно на <a href=http://0.0.0.0:8000>0.0.0.0:8000</a><p>
Чтобы остановить приложение <code>make stop</code><p><p>

<b>Способ 2. Локальный запуск</b><p>
1.Клонировать репозиторий <code>git clone https://github.com/AgafonovChita/proxy_project.git </code><p>
2.Перейти в рабочую директорию <code>cd proxy_project</code><p>
3.<code>python -m venv venv</code><p>
4.<code>source venv/bin/activate</code><p>
5.<code>pip install -r ./requirements.txt</code><p>
6.<code>uvicorn main:app --reload --host 0.0.0.0 --port 8000</code><p>
7.Приложение станет доступно на <a href=http://0.0.0.0:8000>0.0.0.0:8000</a><p>




<b>ДОКУМЕНТАЦИЯ</b>
1. <b>POST</b> http://0.0.0.0:8000/convert<p>
<b>body</b>: {"ubi_num": value}<p><p>

2. Автоматическое тестирование прокси-сервиса на 3х рандомных числах: <p>
<b>GET</b> http://0.0.0.0:8000/test<p>
