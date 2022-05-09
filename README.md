# dataflow-cheatsheet

Dataflow Python Scripts Cheatsheets

## Prerequisites

1. Your GCP Project with Dataflow API enabled.
2. A service account with privileged access to Dataflow. (`roles/dataflow.admin`)
3. A GCP Credential file of the service account mentioned above.
4. Google Cloud Cli (`gcloud`)

```
$ brew install google-cloud-sdk
```

5. An activated `gcloud config configuration` corresponding with your GCP Project. You need this to submit dataflow tasks to your as intended GCP Project by `gcloud` within sample scripts in the repo.

```
gcloud config configurations create ${your_config_name}
gcloud config set project ${your_gcp_project_id}

# Or activate your configuration to your project if it already exists
gcloud config configurations activate ${your_config_name}
```

## Setup

1. Create `env.sh` by copying from `env.sh.sample` and Configure the file.
2. Run `source env.sh` once `env.sh` is configured completely.
3. Run `make setup` to install python virtual enviroments.
