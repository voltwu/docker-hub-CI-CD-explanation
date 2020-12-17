FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN chmod 777 /usr/src/app/run_tests.sh \
    && ln -s /usr/src/app/run_tests.sh /

CMD ["python","-m","http.server","--cgi","8000"]
