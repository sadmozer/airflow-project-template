import requests
session = requests.Session()
session.trust_env = False
health = session.get(url="http://airflow:8080/health").json()
if (health["metadatabase"]["status"] == "healthy" and health["scheduler"]["status"] == "healthy"):
    print("Airflow ready and healthy!")