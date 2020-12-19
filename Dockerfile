FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN chmod +x /usr/src/app/run_tests.sh

ENV PATH="/usr/src/app"

CMD ["python","-m","http.server","--cgi","8000"]
