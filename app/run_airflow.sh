#!/bin/bash

POSITIONAL_ARGS=()

while [[ $# -gt 0 ]]; do
  case $1 in
    -b|--build)
      BUILD=YES
      shift # past argument
      ;;
    -h|--help)
      DESCRIPTION="CIAOs"
      echo -e "usage: run_airflow.sh [-b | --build] [-h | --help]\n"
      echo -e "optional arguments:"
      printf -- '%-20s rebuild the Airflow images before restarting\n' "-b, --build "
      printf -- '%-20s show this help message and exit\n' "-h, --help "
      shift
      exit 0
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
  esac
done

set -- "${POSITIONAL_ARGS[@]}"

echo "Stopping Airflow containers.."
docker-compose down -v

echo "Setting up local folders.."
# echo -e "AIRFLOW_UID=$(id -u)" > .env
mkdir -p ../logs 
mkdir -p ../plugins  

if [[ "$BUILD" = "YES" ]]; then
    echo "Building images.."
    docker-compose build --no-cache
fi

echo "(Re)starting Airflow containers.."
docker-compose up airflow-init -d
docker-compose up -d

while [ "$(docker ps -a | grep app-airflow-webserver-1)" ] && [ "$(docker inspect -f {{.State.Health.Status}} app-airflow-webserver-1)" != "healthy" ]
do 
  echo "Waiting for Airflow to start.." && sleep 2
done

if docker exec -t app-airflow-webserver-1 airflow connections get google_cloud_default | grep -q 'Connection not found.'; then
  echo "Creating BigQuery connection.."
  docker exec -it app-airflow-webserver-1 bash -c "python /tmp/extract_project_id.py "
  docker exec -it app-airflow-webserver-1 bash -c "airflow connections import /tmp/conn.json"
fi

echo "Airflow has started correctly!"
echo "To access the Airflow UI open this url in a browser:"
echo -e "\\thttp://localhost:8080"
echo "Default credentials:"
echo -e "\\tUsername: airflow"
echo -e "\\tPassword: airflow"