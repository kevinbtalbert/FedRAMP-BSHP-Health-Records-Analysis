# %% [markdown]
# # Create a Dashboard Application using CML

# %% [markdown]
# ## Setup the CML API Client

# %%
import os
import cmlapi
import random
import string
import json
import random
import string

client = cmlapi.default_client(url=os.getenv("CDSW_API_URL").replace("/api/v1", ""), cml_api_key=os.getenv("CDSW_APIV2_KEY"))
available_runtimes = client.list_runtimes(search_filter=json.dumps({
    "kernel": "Python 3.9",
    "edition": "GovCloud",
    "editor": "PBJ Workbench"
}))
print(available_runtimes)

## Set available runtimes to the latest runtime in the environment (iterator is the number that begins with 0 and advances sequentially)
## The JOB_IMAGE_ML_RUNTIME variable stores the ML Runtime which will be used to launch the job
print(available_runtimes.runtimes[0])
print(len(available_runtimes.runtimes))
print(available_runtimes.runtimes[len(available_runtimes.runtimes)-1].image_identifier)
APP_IMAGE_ML_RUNTIME = available_runtimes.runtimes[len(available_runtimes.runtimes)-1].image_identifier

## Store the ML Runtime for any future jobs in an environment variable so we don't have to do this step again
os.environ['APP_IMAGE_ML_RUNTIME'] = APP_IMAGE_ML_RUNTIME
project = client.get_project(project_id=os.getenv("CDSW_PROJECT_ID"))


# %% [markdown]
# ## Deploy the Dashboard Application using CML API Client

# %%
def get_random_string(length):
    # this function prevents dupe app names
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

application_request = cmlapi.CreateApplicationRequest(
     name = "BSHP Prediabetes Outcomes Dashboard",
     description = "Dashboard interface for the Prediabetes Outcomes",
     project_id = project.id,
     subdomain = "bshp-" + get_random_string(4),
     script = "dashboard_app.py",
     cpu = 2,
     memory = 8,
     runtime_identifier = os.getenv('APP_IMAGE_ML_RUNTIME')
)

app = client.create_application(
     project_id = project.id,
     body = application_request
)


