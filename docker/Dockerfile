FROM python:3.12.5-alpine3.20

WORKDIR simple_elasticsearch_cleaner

COPY simple_elasticsearch_cleaner.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "simple_elasticsearch_cleaner.py"]
