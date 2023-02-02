FROM python:3.10.0
COPY . .
RUN pip3 install -r requirements.txt
CMD python bot/main.py
