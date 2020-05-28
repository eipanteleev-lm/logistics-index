FROM python:3.7-buster

WORKDIR /usr/app

COPY requirements.txt .

RUN python3.7 -m pip install --upgrade pip && \
  python3.7 -m pip install -r requirements.txt

COPY src src
COPY queries queries
COPY data data

VOLUME data /usr/app/data

ENTRYPOINT [ "python3.7" ]

CMD ["src/app.py"]
