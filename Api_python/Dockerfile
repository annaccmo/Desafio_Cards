FROM alpine


RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

WORKDIR /app   # Defining working directory

COPY /requirements.txt /app

RUN pip3 install -r requirements.txt

COPY ["api_cards.py", "/app"]
COPY ["mongo_connection.py", "/app"]

EXPOSE 5000


ENTRYPOINT [ "python3" ] # Default command

CMD ["api_cards.py"]