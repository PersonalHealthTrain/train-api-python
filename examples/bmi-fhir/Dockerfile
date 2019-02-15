FROM personalhealthtrain/train-api-python:1.0rc5-pandas
COPY entrypoint.py /opt/entrypoint.py
COPY query.cql /opt/query.cql
ENTRYPOINT [ "python", "/opt/entrypoint.py" ]
