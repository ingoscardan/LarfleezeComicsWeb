import io
import os

import environ
from google.cloud import secretmanager

def setup_environment(base_dir):
    env = environ.Env(DEBUG=(bool, False))
    env_file = os.path.join(base_dir, '.env')

    if os.path.isfile(env_file):
        #Use local .env file
        env.read_env(env_file)
    elif os.environ.get("GOOGLE_CLOUD_PROJECT", None):
        # Pull secrets from Secret Manager
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")

        client = secretmanager.SecretManagerServiceClient()
        settings_name = os.environ.get("SETTINGS_NAME", "django_settings")
        name = f"projects/{project_id}/secrets/{settings_name}/versions/latest"
        payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

        env.read_env(io.StringIO(payload))
    else:
        raise Exception("No local .env or GOOGLE_CLOUD_PROJECT detected. No secrets found.")

    return env
