FROM python:3

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN  pip install Flask

EXPOSE 5000

CMD ["python", "hello_world.py"]