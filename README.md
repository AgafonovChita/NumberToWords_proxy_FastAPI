<b>УСТАНОВКА</b><p>
1.Установить Docker и Docker-compose<p>
2.Клонировать репозиторий <code>git clone https://github.com/AgafonovChita/proxy_project.git </code><p>
3.Перейти в рабочую директорию <code>cd proxy_project</code><p>
4.Запустить контейнер <code>make run</code><p>
5.Приложение станет доступно на <a href=http://0.0.0.0:8000>0.0.0.0:8000</a><p>

Чтобы остановить приложение <code>make stop</code><p><p>

<b>ДОКУМЕНТАЦИЯ</b>
1. POST http://0.0.0.0:8000/convert<p>
Body: {"ubi_num": value}<p><p>
2. GET http://0.0.0.0:8000/test<p>
Тестирование сервиса на 3х рандомных числах