FROM mongo:3.4

COPY ./resources/import_distances.sh /docker-entrypoint-initdb.d/import_distances.sh
COPY ./resources/origin_dest_distances.jsonl /resources/origin_dest_distances.jsonl
COPY ./data /data/db


EXPOSE 27017

