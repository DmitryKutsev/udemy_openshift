FROM python:3.7


RUN pip install requirements.txt
RUN python app/app.py

