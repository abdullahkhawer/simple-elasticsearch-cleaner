FROM python:3.13.1-alpine3.21

WORKDIR simple_elasticsearch_cleaner

COPY simple_elasticsearch_cleaner.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "simple_elasticsearch_cleaner.py"]
