<b>Способ 1. Запуск в конктейнере</b><p>
<ol>
<li>Установить Docker и Docker-compose
<li>Клонировать репозиторий <code>git clone https://github.com/AgafonovChita/proxy_project.git </code>
<li>Перейти в рабочую директорию <code>cd proxy_project</code>
<li>Запустить контейнер <code>make run</code>
<li>Приложение станет доступно на <a href=http://0.0.0.0:8000>0.0.0.0:8000</a>
</ol>
Чтобы остановить приложение <code>make stop</code><p><p>

<b>Способ 2. Локальный запуск</b><p>
<ol>
<li>Клонировать репозиторий <code>git clone https://github.com/AgafonovChita/proxy_project.git </code>
<li>Перейти в рабочую директорию <code>cd proxy_project</code>
<li><code>python -m venv venv</code>
<li><code>source venv/bin/activate</code>
<li><code>pip install -r ./requirements.txt</code>
<li><code>uvicorn main:app --reload --host 0.0.0.0 --port 8000</code>
<li>Приложение станет доступно на <a href=http://0.0.0.0:8000>0.0.0.0:8000</a>
  </ol>




<b>ДОКУМЕНТАЦИЯ</b>
1. <b>POST</b> http://0.0.0.0:8000/proxy_number_to_words<p>
<b>body</b>: {"ubi_num": value}<p><p>

2. Автоматическое тестирование прокси-сервиса на 3х рандомных числах: <p>
<b>GET</b> http://0.0.0.0:8000/test<p>
