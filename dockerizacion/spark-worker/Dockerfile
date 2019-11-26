FROM bde2020/spark-worker:2.4.4-hadoop2.7

COPY ./models /models
COPY ./prediction /prediction-job

EXPOSE 8081

CMD /spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.4,org.mongodb.spark:mongo-spark-connector_2.11:2.4.1 --class es.upm.dit.ging.predictor.MakePrediction --master local /prediction-job/flight_prediction_2.11-0.1.jar
