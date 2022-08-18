import json
with open("/tmp/credentials.json", "r") as f:
    project_id = json.load(f)["project_id"]

with open("/tmp/conn.json", "r") as fin:
    connections = json.load(fin)

connections["google_cloud_default"]["extra"]["extra__google_cloud_platform__project"] = project_id

with open("/tmp/conn.json", "w") as fout:
    json.dump(connections, fout, indent=4, sort_keys=True)

