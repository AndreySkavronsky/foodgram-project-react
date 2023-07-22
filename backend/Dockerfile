# Используем образ Python в качестве базового
FROM python:3.11.4-slim

# Обновляем и устанавливаем зависимости, включая утилиту make
RUN apt-get update &&\
    apt-get upgrade -y &&\
    apt-get install -y --no-install-recommends make &&\
    apt-get clean &&\
    apt-get autoremove -y &&\
    rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt ./
RUN pip install -U pip &&\
    pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы проекта
COPY . /app

# Выполняем все необходимые действия и запускаем Gunicorn через Makefile
CMD ["make", "run"]