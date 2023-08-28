FROM python:3.7-slim

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install flask_sqlalchemy
RUN pip install psycopg2-binary

COPY scripts/extract_n_load.py  /extract_n_load.py

CMD ["python","extract_n_load.py"]