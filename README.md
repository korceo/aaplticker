

# Ticker + Vis Streamlit App

Этот проект — веб-приложение на Streamlit для отображения данных о котировках и визуализации графиков на любом датасете в формате csv.

## Запуск через Docker

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/korceo/aaplticker.git
cd aaplticker
```

### 2. Соберите Docker-образ
```bash
docker build -t aaplticker .
```

### 3. Запустите контейнер
```bash
docker run -p 8501:8501 aaplticker
```

После запуска приложение будет доступно по адресу:
```
http://localhost:8501
```
