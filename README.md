Proxy для <a href="https://www.dataaccess.com/webservicesserver/NumberConversion.wso?op=NumberToWords">API</a>

<i>Принимает запрос в json, конвертирует в xml, отправляет запрос на API, принимает ответ, возвращает конвертированный в json ответ</i>

<b>Способ 1. Запуск в конктейнере</b>
  <ol>
    <li>Установить Docker и Docker-compose
    <li>Клонировать репозиторий <code>git clone https://github.com/AgafonovChita/proxy_project.git </code>
    <li>Перейти в рабочую директорию <code>cd proxy_project</code>
    <li>Запустить контейнер <code>make run</code>
    <li>Приложение станет доступно на <a href=http://0.0.0.0:8000>0.0.0.0:8000</a>
  </ol>
Чтобы остановить приложение <code>make stop</code><p>


<b>Способ 2. Локальный запуск</b>
  <ol>
    <li>Клонировать репозиторий <code>git clone https://github.com/AgafonovChita/proxy_project.git </code>
    <li>Перейти в рабочую директорию <code>cd proxy_project</code>
    <li><code>python -m venv venv</code>
    <li><code>source venv/bin/activate</code>
    <li><code>pip install -r ./requirements.txt</code>
    <li><code>uvicorn main:app --reload --host 0.0.0.0 --port 8000</code>
    <li>Приложение станет доступно на <a href=http://0.0.0.0:8000>0.0.0.0:8000</a>
  </ol>




<b>ДОКУМЕНТАЦИЯ</b><br>
1.Proxy-endpoint:<br>
<b>POST</b> /proxy_number_to_words<br>
<b>Host</b>: http://0.0.0.0:8000 <br>
<b>ubi_num</b> = "your value"<br>

2.Тестирование прокси на 3х рандомных числах:<br>
<b>GET</b> /test <br>
<b>Host</b>: http://0.0.0.0:8000 <br>

