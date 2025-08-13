

# Ticker + Vis Streamlit App

Веб-приложение на Streamlit для отображения данных о котировках и визуализации графиков на любом датасете в формате csv.

## Запуск через Docker

1. Убедитесь, что у вас установлен Docker.
2. Выполните:
```bash
docker build -t aaplticker https://github.com/korceo/aaplticker.git
docker run -p 8501:8501 aaplticker
```
3. После запуска приложение будет доступно по адресу:
```
http://localhost:8501
```
