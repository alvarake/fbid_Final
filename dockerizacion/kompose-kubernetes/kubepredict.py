import os


#Aparentemente el SPARK_MASTER no hace falta; Por lo menos con un nodo

def deploy(array, time):
    for f in array:
	    os.system("kubectl apply -f " + f)
	    os.system("sleep "+ time)

zkkf = [
    'zookeeper-deployment.yaml,zookeeper-service.yaml',
    'kafka-deployment.yaml',
    'kafka-service.yaml'
]
deploy(zkkf, "20")

webmongo = [
    'mongo-deployment.yaml', 
    'mongo-service.yaml',
    'mongo-claim0-persistentvolumeclaim.yaml',
	'web-deployment.yaml',
	'web-service.yaml'    
    ]
deploy(webmongo, "0")


spark = [
    'spark-worker-1-deployment.yaml,spark-worker-1-service.yaml'
]

# spark = [
#     'spark-master-deployment.yaml,spark-master-service.yaml',
#     'spark-worker-1-deployment.yaml,spark-worker-1-service.yaml'
# ]
deploy(spark, "12")


