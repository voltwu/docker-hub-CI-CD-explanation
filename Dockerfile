FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN chmod +x /usr/src/app/run_tests.sh

ENV PATH="/usr/src/app/run_tests.sh:${PATH}"

CMD ["python","-m","http.server","--cgi","8000"]
