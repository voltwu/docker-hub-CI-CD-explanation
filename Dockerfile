FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD ["python","-m","http.server","--cgi","8000"]
