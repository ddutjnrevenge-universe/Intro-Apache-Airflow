FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./stock_data.py stock_data.py

CMD [ "python", "stock_data.py"]