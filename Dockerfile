FROM python:3.7-buster

WORKDIR /usr/app

COPY src src
COPY requirements.txt .
COPY week_dataset.pkl .

RUN python3.7 -m pip install --upgrade pip && \
  python3.7 -m pip install -r requirements.txt

ENTRYPOINT [ "python3.7" ]

CMD ["src/app.py"]
