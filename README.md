# Простой Web Scraper

Небольшой скрипт на Python для парсинга веб-страниц. Он извлекает заголовки статей, ссылки и краткое описание (если доступно) со страницы и сохраняет результат в CSV файл.

Скрипт пытается автоматически определить статьи, анализируя распространённую HTML-структуру (`article`, `h1`, `h2`, `h3`).

---

## Возможности

- извлечение заголовков статей
- сбор ссылок на страницы
- попытка извлечения краткого описания (summary)
- фильтрация невалидных ссылок (`login`, `mailto`, `javascript` и др.)
- сохранение результатов в CSV
- работа с большинством сайтов с блогами или новостями

---

## Пример результата

title,url,summary
Local AI Assistant: Installing OpenClaw with Ollama in 2 Steps,https://example.com/article1,N/A
How Modern Databases Work,https://example.com/article2,This article explains how modern databases handle data...
Building a CLI Tool in Python,https://example.com/article3,N/A

## Установка

Установите необходимые зависимости:

pip install requests beautifulsoup4


## Использование

Запустите скрипт и передайте URL страницы:

python webscraper.py https://вашсайт.com

После выполнения появится файл вашеимя.csv с результатами.

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл LICENSE для подробностей.
