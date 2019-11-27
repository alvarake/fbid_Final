FROM python:3.6
COPY ./requirements.txt /requirements/
RUN pip3 install -r /requirements/requirements.txt
ENV PROJECT_HOME=/
COPY ./app /app 
EXPOSE 80
CMD ["python3", "/app/predict_flask.py"]
