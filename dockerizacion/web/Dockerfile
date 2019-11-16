FROM python:3.6

COPY ./requirements.txt /requirements/
RUN pip3 install -r /requirements/requirements.txt
ENV PROJECT_HOME=/
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["predict_flask.py"]