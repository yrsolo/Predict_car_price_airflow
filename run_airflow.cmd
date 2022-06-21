mkdir logs
mkdir plugins
mkdir data\models
mkdir data\predictions
mkdir data\test
mkdir data\train

docker-compose up airflow-init
docker-compose up
