# En Google Cloud Kubernetes.
Para ejecutar el proyecto en Google Cloud Kubernetes se necesita lo siguiente:
- Tener kubectl instalado y apuntando a un cluster de Google Cloud. [+Info](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl?hl=es-419)

- Situarse en la carpeta dockerizacion/kompose-kubernetes y lanzar el script situado en esa carpeta:
`python3 kubepredict.py`       

La aplicación se lanzara en el puerto 80.

# En Local
Para ejecutar el comando en local basta con situarse en la carpeta dockerizacion y lanzar:

`docker-compose up
