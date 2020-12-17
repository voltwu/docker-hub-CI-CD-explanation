FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN chmod +x run_tests.sh
RUN export PATH=$PATH:/usr/src/app/run_tests.sh

CMD ["python","-m","http.server","--cgi","8000"]
