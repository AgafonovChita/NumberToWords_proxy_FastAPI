<b>Proxy на FastAPI</b> для <a href="https://www.dataaccess.com/webservicesserver/NumberConversion.wso?op=NumberToWords">SOAP API - NumberToWords</a>


<ol>
  <li>принимает запрос в json
  <li>конвертирует в xml
  <li>отправляет запрос на оригинальное API
  <li>принимает ответ
  <li>возвращает конвертированный в json ответ
</ol>

________________________________________________________________


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


________________________________________________________________

<b>ДОКУМЕНТАЦИЯ</b><br>
1.Proxy-endpoint:<br>
<b>POST</b> /proxy_number_to_words<br>
<b>Host</b>: http://0.0.0.0:8000 <br>
<b>ubi_num</b> = "your value"<br>

2.Тестирование прокси на 3х рандомных числах:<br>
<b>GET</b> /test <br>
<b>Host</b>: http://0.0.0.0:8000 <br>

