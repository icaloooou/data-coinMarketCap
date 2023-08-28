FROM python:3.7-slim

RUN python -m pip install --upgrade pip

RUN pip install flask_sqlalchemy

COPY scripts/extract_n_load.py  /scripts/extract_n_load.py

CMD ["python","extract_n_load.py"]