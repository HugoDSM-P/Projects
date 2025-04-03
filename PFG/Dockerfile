FROM python:3.13-alpine

WORKDIR /app

COPY . /app

RUN apk update && apk upgrade
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["app.py"]