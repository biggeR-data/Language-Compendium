FROM registry.access.redhat.com/ubi8/python-38

USER root

WORKDIR /usr/src/app

COPY requirements ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["run.py"]
