## 2.1

latex-файл сразу и с таблицей, и с картинкой: *artifacts/table_with_picture.tex*

## 2.2

pdf-файл сразу и с таблицей, и с картинкой: *artifacts/table_with_picture.pdf*

ссылка на репозиторий: https://test.pypi.org/project/latexgen/0.0.3/

## 2.3

Dockerfile собирающий образ со всем необходимым окружением также лежит в корне директории. 

Собираем образ: *docker build .*

Инициируем образ: *docker run -it <image_id> //bin/bash*

Запускаем скрипт в образе: *cd src && python3 main.py*
