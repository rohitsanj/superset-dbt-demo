"""
Helper script to generate Superset access/refresh token
and push descriptions from dbt models into Superset 
using dbt-superset-lineage (https://github.com/slidoapp/dbt-superset-lineage)
"""
import requests
from dbt_superset_lineage import push_descriptions_main


if __name__ == "__main__":
    superset_db_id = 1
    create_dataset_if_not_exists = True

    protocol = "http"
    superset_host = "localhost"
    superset_port = 8088
    superset_url = f"{protocol}://{superset_host}:{superset_port}"
    res = requests.post(f"{superset_url}/api/v1/security/login", json={
        "username": "admin",
        "password": "admin",
        "provider": "db",
        "refresh": True,
    })
    assert res.status_code == 200, f"Failed to fetch access; {res.status_code=}"

    js = res.json()
    access_token = js["access_token"]
    refresh_token = js["refresh_token"]

    push_descriptions_main(
        dbt_project_dir=".",
        dbt_db_name=None,
        superset_url=superset_url,
        superset_db_id=superset_db_id,
        superset_refresh_columns=True,
        superset_pause_after_update=None,
        superset_access_token=access_token,
        superset_refresh_token=refresh_token,
        create_dataset_if_not_exists=create_dataset_if_not_exists,
    )
