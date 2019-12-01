FROM bde2020/spark-worker:2.4.4-hadoop2.7

COPY ./models /models
COPY ./prediction /prediction-job

EXPOSE 8081

CMD sh -c "sleep 12 && /prediction-job/startpredicition.sh"
