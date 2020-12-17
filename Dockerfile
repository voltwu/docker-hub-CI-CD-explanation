FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN chmod 777 /usr/local/bin/run_tests.sh \
    && ln -s /usr/local/bin/run_tests.sh /
    
CMD ["python","-m","http.server","--cgi","8000"]
