# airflow-project-template

Project template containing configuration files useful for local container development and testing of Airflow DAGs.

## Requirements

**Windows**
- [Windows subsystem for Linux 2](https://docs.microsoft.com/it-it/windows/wsl/install)
- [Docker Desktop](https://docs.docker.com/desktop/windows/install/) with
    - [Integration in WSL enabled](https://docs.docker.com/desktop/windows/wsl/#enabling-docker-support-in-wsl-2-distros) (checkbox enabled in Settings->Resources->WSL Integration) 
- Google Cloud Platform account with:
  - [BigQuery API enabled](https://cloud.google.com/endpoints/docs/openapi/enable-api)
  - [Service account .json file](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating) with [BigQuery access permissions](https://cloud.google.com/iam/docs/granting-changing-revoking-access)

## Installation

1. [**REQUIRED**] Clone this repository locally
    - using SSH
    ```
    git clone git@github.com:sadmozer/airflow-project-template.git
    ```
   - using HTTP
   ```
   git clone https://github.com/sadmozer/airflow-project-template.git
   ```
2. [**REQUIRED**] Copy the **service account json file** to `airflow-project-template/app/gcp` folder and rename it to `credentials.json`.
3. [**OPTIONAL**] If you want to change the version of Airflow or the version of Python you need to change the line `FROM apache/airflow:X.X.X-pythonY.Y` in the `airflow-project-template/airflow/Dockerfile`. Each time you update this file you need to restart the Airflow containers using the commands in step 5.
4. [**OPTIONAL**] If you use additional Python libraries in your DAGs insert its PyPI name and version in the `airflow-project-template/requirements.txt` file (like this `pandas==1.4.3`). Each time you add a library you need to restart the Airflow containers using the commands in step 5.
5. [**REQUIRED**] Run the following commands 
    ```
    cd app
    bash run_airflow.sh --build
    ```
    These commands will build and launch the Airflow containers. It may take a few minutes before they are ready.
 
After the installation, the Airflow containers should be up and running.
## Usage
**Airflow Web UI** 

Open in a browser the following url: `http://localhost:8080` and enter as user:password: `airflow:airflow`.

**Upload an Airflow DAG**

Put the DAG file inside the `airflow-project-template/src` folder.

**Restart Airflow**
```
cd app
bash run_airflow.sh
```

**Stop Airflow**
```
cd app
docker-compose down -v
```