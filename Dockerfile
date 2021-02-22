FROM python:3

COPY requirements.txt /requirements.txt

RUN pip install -r  requirements.txt

COPY project /project

WORKDIR /project

CMD ["python", "main.py"]
