FROM python:3.7-buster

WORKDIR /usr/app

COPY requirements.txt .

RUN python3.7 -m pip install --upgrade pip \
  && python3.7 -m pip install -r requirements.txt \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base \
    ~/.cache/pip

COPY src src
COPY queries queries
COPY tests tests

ENTRYPOINT [ "python3.7" ]

CMD ["src/app.py"]
