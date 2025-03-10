# Databricks API Documentation

## Table of Contents

1. [API Endpoints](#api-endpoints)
2. [General Documentation](#general-documentation)

# API Endpoints

## GET /2.1/jobs/get

Retrieves the details for a single job.

### Query parameters

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#job_id) requiredint64

Example`job_id=11223344`

The canonical identifier of the job to retrieve information about. This field is required.

### Responses

**200** Request completed successfully.

Request completed successfully.

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#job_id) int64

Example`11223344`

The canonical identifier for this job.

[`creator_user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#creator_user_name) string

Example`"user.name@databricks.com"`

The creator user name. This field won’t be included in the response if the user has already been deleted.

[`run_as_user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#run_as_user_name) string

Example`"user.name@databricks.com"`

The email of an active workspace user or the application ID of a service principal that the job runs as. This value can be changed by setting the `run_as` field when creating or updating a job.

By default, `run_as_user_name` is based on the current job settings and is set to the creator of the job if job access control is disabled or to the user with the `is_owner` permission if job access control is enabled.

[`settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings) object

Settings for this job and all of its runs. These settings can be updated using the `resetJob` method.

[`name`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-name) string

<= 4096 characters

Default`"Untitled"`

Example`"A multitask job"`

An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding.

[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-description) string

<= 27700 characters

Example`"This job contain multiple tasks that are required to produce the weekly shark sightings report."`

An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding.

[`email_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-email_notifications) object

Default`{}`

An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.

[`webhook_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-webhook_notifications) object

Default`{}`

A collection of system notification IDs to notify when runs of this job begin or complete.

[`notification_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-notification_settings) object

Default`{}`

Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this job.

[`timeout_seconds`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-timeout_seconds) int32

Default`0`

Example`86400`

An optional timeout applied to each run of this job. A value of `0` means no timeout.

[`health`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-health) object

An optional set of health rules that can be defined for this job.

[`schedule`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-schedule) object

An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.

[`trigger`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-trigger) object

A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.

[`continuous`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-continuous) object

An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of `schedule` and `continuous` can be used.

[`max_concurrent_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-max_concurrent_runs) int32

Default`1`

Example`10`

An optional maximum allowed number of concurrent runs of the job.
Set this value if you want to be able to execute multiple runs of the same job concurrently.
This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters.
This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs.
However, from then on, new runs are skipped unless there are fewer than 3 active runs.
This value cannot exceed 1000. Setting this value to `0` causes all new runs to be skipped.

[`tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-tasks) Array of object

<= 100 items

Example

A list of task specifications to be executed by this job.
If more than 100 tasks are available, you can paginate through them using [jobs/get](https://docs.databricks.com/api/azure/workspace/jobs/get). Use the `next_page_token` field at the object root to determine if more results are available.

[`job_clusters`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-job_clusters) Array of object

<= 100 items

Example

A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
If more than 100 job clusters are available, you can paginate through them using [jobs/get](https://docs.databricks.com/api/azure/workspace/jobs/get).

[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-git_source) object

Example

An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.

If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.

Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.

[`tags`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-tags) object

Default`{}`

Example

A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.

[`format`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-format) string

Deprecated

Enum: `SINGLE_TASK | MULTI_TASK`

Example`"MULTI_TASK"`

Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`.

[`queue`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-queue) object

The queue settings of the job.

[`parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-parameters) Array of object

Job-level parameter definitions

[`edit_mode`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-edit_mode) string

Enum: `UI_LOCKED | EDITABLE`

Edit mode of the job.

- `UI_LOCKED`: The job is in a locked UI state and cannot be modified.
- `EDITABLE`: The job is in an editable state and can be modified.

[`deployment`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-deployment) object

Deployment information for jobs managed by external sources.

[`environments`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#settings-environments) Array of object

<= 10 items

A list of task execution environment specifications that can be referenced by serverless tasks of this job.
An environment is required to be present for serverless tasks.
For serverless notebook tasks, the environment is accessible in the notebook environment panel.
For other serverless tasks, the task environment is required to be specified using environment\_key in the task settings.

[`created_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/get#created_time) int64

Example`1601370337343`

The time at which this job was created in epoch milliseconds (milliseconds since 1/1/1970 UTC).

This method might return the following HTTP codes: 400, 401, 403, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Response samples

200

```
{
  "job_id": 11223344,
  "creator_user_name": "user.name@databricks.com",
  "run_as_user_name": "user.name@databricks.com",
  "settings": {
    "name": "A multitask job",
    "description": "This job contain multiple tasks that are required to produce the weekly shark sightings report.",
    "email_notifications": {
      "on_start": [\
        "user.name@databricks.com"\
      ],
      "on_success": [\
        "user.name@databricks.com"\
      ],
      "on_failure": [\
        "user.name@databricks.com"\
      ],
      "on_duration_warning_threshold_exceeded": [\
        "user.name@databricks.com"\
      ],
      "on_streaming_backlog_exceeded": [\
        "user.name@databricks.com"\
      ],
      "no_alert_for_skipped_runs": false
    },
    "webhook_notifications": {
      "on_start": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_success": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_failure": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_duration_warning_threshold_exceeded": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_streaming_backlog_exceeded": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ]
    },
    "notification_settings": {
      "no_alert_for_skipped_runs": false,
      "no_alert_for_canceled_runs": false,
      "alert_on_last_attempt": false
    },
    "timeout_seconds": 86400,
    "health": {
      "rules": [\
        {\
          "metric": "RUN_DURATION_SECONDS",\
          "op": "GREATER_THAN",\
          "value": 10\
        }\
      ]
    },
    "schedule": {
      "quartz_cron_expression": "20 30 * * * ?",
      "timezone_id": "Europe/London",
      "pause_status": "UNPAUSED"
    },
    "trigger": {
      "pause_status": "UNPAUSED",
      "file_arrival": {
        "url": "string",
        "min_time_between_triggers_seconds": 0,
        "wait_after_last_change_seconds": 0
      },
      "periodic": {
        "interval": 0,
        "unit": "HOURS"
      }
    },
    "continuous": {
      "pause_status": "UNPAUSED"
    },
    "max_concurrent_runs": 10,
    "tasks": [\
      {\
        "max_retries": 3,\
        "task_key": "Sessionize",\
        "description": "Extracts session data from events",\
        "min_retry_interval_millis": 2000,\
        "depends_on": [],\
        "timeout_seconds": 86400,\
        "spark_jar_task": {\
          "main_class_name": "com.databricks.Sessionize",\
          "parameters": [\
            "--data",\
            "dbfs:/path/to/data.json"\
          ]\
        },\
        "libraries": [\
          {\
            "jar": "dbfs:/mnt/databricks/Sessionize.jar"\
          }\
        ],\
        "retry_on_timeout": false,\
        "existing_cluster_id": "0923-164208-meows279"\
      },\
      {\
        "max_retries": 3,\
        "task_key": "Orders_Ingest",\
        "description": "Ingests order data",\
        "job_cluster_key": "auto_scaling_cluster",\
        "min_retry_interval_millis": 2000,\
        "depends_on": [],\
        "timeout_seconds": 86400,\
        "spark_jar_task": {\
          "main_class_name": "com.databricks.OrdersIngest",\
          "parameters": [\
            "--data",\
            "dbfs:/path/to/order-data.json"\
          ]\
        },\
        "libraries": [\
          {\
            "jar": "dbfs:/mnt/databricks/OrderIngest.jar"\
          }\
        ],\
        "retry_on_timeout": false\
      },\
      {\
        "max_retries": 3,\
        "task_key": "Match",\
        "description": "Matches orders with user sessions",\
        "notebook_task": {\
          "base_parameters": {\
            "age": "35",\
            "name": "John Doe"\
          },\
          "notebook_path": "/Users/user.name@databricks.com/Match"\
        },\
        "min_retry_interval_millis": 2000,\
        "depends_on": [\
          {\
            "task_key": "Orders_Ingest"\
          },\
          {\
            "task_key": "Sessionize"\
          }\
        ],\
        "new_cluster": {\
          "autoscale": {\
            "max_workers": 16,\
            "min_workers": 2\
          },\
          "node_type_id": null,\
          "spark_conf": {\
            "spark.speculation": true\
          },\
          "spark_version": "7.3.x-scala2.12"\
        },\
        "timeout_seconds": 86400,\
        "retry_on_timeout": false,\
        "run_if": "ALL_SUCCESS"\
      }\
    ],
    "job_clusters": [\
      {\
        "job_cluster_key": "auto_scaling_cluster",\
        "new_cluster": {\
          "autoscale": {\
            "max_workers": 16,\
            "min_workers": 2\
          },\
          "node_type_id": null,\
          "spark_conf": {\
            "spark.speculation": true\
          },\
          "spark_version": "7.3.x-scala2.12"\
        }\
      }\
    ],
    "git_source": {
      "git_branch": "main",
      "git_provider": "gitHub",
      "git_url": "https://github.com/databricks/databricks-cli"
    },
    "tags": {
      "cost-center": "engineering",
      "team": "jobs"
    },
    "format": "SINGLE_TASK",
    "queue": {
      "enabled": true
    },
    "parameters": [\
      {\
        "default": "users",\
        "name": "table"\
      }\
    ],
    "run_as": {
      "user_name": "user@databricks.com",
      "service_principal_name": "692bc6d0-ffa3-11ed-be56-0242ac120002"
    },
    "edit_mode": "UI_LOCKED",
    "deployment": {
      "kind": "BUNDLE",
      "metadata_file_path": "string"
    },
    "environments": [\
      {\
        "environment_key": "string",\
        "spec": {\
          "client": "1",\
          "dependencies": [\
            "string"\
          ]\
        }\
      }\
    ]
  },
  "created_time": 1601370337343
}
```

## GET /2.1/jobs/list

Retrieves a list of jobs.

### Query parameters

[`offset`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#offset) int32

<= 1000

Deprecated

Default`0`

The offset of the first job to return, relative to the most recently created job.
Deprecated since June 2023. Use `page_token` to iterate through the pages instead.

[`limit`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#limit) int32

\[ 1 .. 100 \]

Default`20`

Example`limit=25`

The number of jobs to return. This value must be greater than 0 and less or equal to 100. The default value is 20.

[`expand_tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#expand_tasks) boolean

Default`false`

Whether to include task and cluster details in the response.

[`name`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#name) string

Example`name=A%20multitask%20job`

A filter on the list based on the exact (case insensitive) job name.

[`page_token`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#page_token) string

Example`page_token=CAEomPSriYcxMPWM_IiIxvEB`

Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or previous page of jobs respectively.

### Responses

**200** Request completed successfully.

Request completed successfully.

[`jobs`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#jobs) Array of object

The list of jobs. Only included in the response if there are jobs to list.

Array \[\
\
[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#jobs-job_id) int64\
\
Example`11223344`\
\
The canonical identifier for this job.\
\
[`creator_user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#jobs-creator_user_name) string\
\
Example`"user.name@databricks.com"`\
\
The creator user name. This field won’t be included in the response if the user has already been deleted.\
\
[`settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#jobs-settings) object\
\
Settings for this job and all of its runs. These settings can be updated using the `resetJob` method.\
\
[`created_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#jobs-created_time) int64\
\
Example`1601370337343`\
\
The time at which this job was created in epoch milliseconds (milliseconds since 1/1/1970 UTC).\
\
\]

[`has_more`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#has_more) boolean

Example`false`

If true, additional jobs matching the provided filter are available for listing.

[`next_page_token`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#next_page_token) string

Example`"CAEomPuciYcxMKbM9JvMlwU="`

A token that can be used to list the next page of jobs (if applicable).

[`prev_page_token`](https://docs.databricks.com/api/azure/workspace/jobs_21/list#prev_page_token) string

Example`"CAAos-uriYcxMN7_rt_v7B4="`

A token that can be used to list the previous page of jobs (if applicable).

This method might return the following HTTP codes: 400, 401, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

QUOTA\_EXCEEDED

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Response samples

200

```
{
  "jobs": [\
    {\
      "job_id": 11223344,\
      "creator_user_name": "user.name@databricks.com",\
      "settings": {\
        "name": "A multitask job",\
        "description": "This job contain multiple tasks that are required to produce the weekly shark sightings report.",\
        "email_notifications": {\
          "on_start": [\
            "user.name@databricks.com"\
          ],\
          "on_success": [\
            "user.name@databricks.com"\
          ],\
          "on_failure": [\
            "user.name@databricks.com"\
          ],\
          "on_duration_warning_threshold_exceeded": [\
            "user.name@databricks.com"\
          ],\
          "on_streaming_backlog_exceeded": [\
            "user.name@databricks.com"\
          ],\
          "no_alert_for_skipped_runs": false\
        },\
        "webhook_notifications": {\
          "on_start": [\
            [\
              {\
                "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
              }\
            ]\
          ],\
          "on_success": [\
            [\
              {\
                "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
              }\
            ]\
          ],\
          "on_failure": [\
            [\
              {\
                "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
              }\
            ]\
          ],\
          "on_duration_warning_threshold_exceeded": [\
            [\
              {\
                "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
              }\
            ]\
          ],\
          "on_streaming_backlog_exceeded": [\
            [\
              {\
                "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
              }\
            ]\
          ]\
        },\
        "notification_settings": {\
          "no_alert_for_skipped_runs": false,\
          "no_alert_for_canceled_runs": false,\
          "alert_on_last_attempt": false\
        },\
        "timeout_seconds": 86400,\
        "health": {\
          "rules": [\
            {\
              "metric": "RUN_DURATION_SECONDS",\
              "op": "GREATER_THAN",\
              "value": 10\
            }\
          ]\
        },\
        "schedule": {\
          "quartz_cron_expression": "20 30 * * * ?",\
          "timezone_id": "Europe/London",\
          "pause_status": "UNPAUSED"\
        },\
        "trigger": {\
          "pause_status": "UNPAUSED",\
          "file_arrival": {\
            "url": "string",\
            "min_time_between_triggers_seconds": 0,\
            "wait_after_last_change_seconds": 0\
          },\
          "periodic": {\
            "interval": 0,\
            "unit": "HOURS"\
          }\
        },\
        "continuous": {\
          "pause_status": "UNPAUSED"\
        },\
        "max_concurrent_runs": 10,\
        "tasks": [\
          {\
            "max_retries": 3,\
            "task_key": "Sessionize",\
            "description": "Extracts session data from events",\
            "min_retry_interval_millis": 2000,\
            "depends_on": [],\
            "timeout_seconds": 86400,\
            "spark_jar_task": {\
              "main_class_name": "com.databricks.Sessionize",\
              "parameters": [\
                "--data",\
                "dbfs:/path/to/data.json"\
              ]\
            },\
            "libraries": [\
              {\
                "jar": "dbfs:/mnt/databricks/Sessionize.jar"\
              }\
            ],\
            "retry_on_timeout": false,\
            "existing_cluster_id": "0923-164208-meows279"\
          },\
          {\
            "max_retries": 3,\
            "task_key": "Orders_Ingest",\
            "description": "Ingests order data",\
            "job_cluster_key": "auto_scaling_cluster",\
            "min_retry_interval_millis": 2000,\
            "depends_on": [],\
            "timeout_seconds": 86400,\
            "spark_jar_task": {\
              "main_class_name": "com.databricks.OrdersIngest",\
              "parameters": [\
                "--data",\
                "dbfs:/path/to/order-data.json"\
              ]\
            },\
            "libraries": [\
              {\
                "jar": "dbfs:/mnt/databricks/OrderIngest.jar"\
              }\
            ],\
            "retry_on_timeout": false\
          },\
          {\
            "max_retries": 3,\
            "task_key": "Match",\
            "description": "Matches orders with user sessions",\
            "notebook_task": {\
              "base_parameters": {\
                "age": "35",\
                "name": "John Doe"\
              },\
              "notebook_path": "/Users/user.name@databricks.com/Match"\
            },\
            "min_retry_interval_millis": 2000,\
            "depends_on": [\
              {\
                "task_key": "Orders_Ingest"\
              },\
              {\
                "task_key": "Sessionize"\
              }\
            ],\
            "new_cluster": {\
              "autoscale": {\
                "max_workers": 16,\
                "min_workers": 2\
              },\
              "node_type_id": null,\
              "spark_conf": {\
                "spark.speculation": true\
              },\
              "spark_version": "7.3.x-scala2.12"\
            },\
            "timeout_seconds": 86400,\
            "retry_on_timeout": false,\
            "run_if": "ALL_SUCCESS"\
          }\
        ],\
        "job_clusters": [\
          {\
            "job_cluster_key": "auto_scaling_cluster",\
            "new_cluster": {\
              "autoscale": {\
                "max_workers": 16,\
                "min_workers": 2\
              },\
              "node_type_id": null,\
              "spark_conf": {\
                "spark.speculation": true\
              },\
              "spark_version": "7.3.x-scala2.12"\
            }\
          }\
        ],\
        "git_source": {\
          "git_branch": "main",\
          "git_provider": "gitHub",\
          "git_url": "https://github.com/databricks/databricks-cli"\
        },\
        "tags": {\
          "cost-center": "engineering",\
          "team": "jobs"\
        },\
        "format": "SINGLE_TASK",\
        "queue": {\
          "enabled": true\
        },\
        "parameters": [\
          {\
            "default": "users",\
            "name": "table"\
          }\
        ],\
        "run_as": {\
          "user_name": "user@databricks.com",\
          "service_principal_name": "692bc6d0-ffa3-11ed-be56-0242ac120002"\
        },\
        "edit_mode": "UI_LOCKED",\
        "deployment": {\
          "kind": "BUNDLE",\
          "metadata_file_path": "string"\
        },\
        "environments": [\
          {\
            "environment_key": "string",\
            "spec": {\
              "client": "1",\
              "dependencies": [\
                "string"\
              ]\
            }\
          }\
        ]\
      },\
      "created_time": 1601370337343\
    }\
  ],
  "has_more": false,
  "next_page_token": "CAEomPuciYcxMKbM9JvMlwU=",
  "prev_page_token": "CAAos-uriYcxMN7_rt_v7B4="
}
```

## GET /2.1/jobs/runs/export

Export and retrieve the job run task.

### Query parameters

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/exportrun#run_id) requiredint64

Example`run_id=455644833`

The canonical identifier for the run. This field is required.

[`views_to_export`](https://docs.databricks.com/api/azure/workspace/jobs_21/exportrun#views_to_export) string

Enum: `CODE | DASHBOARDS | ALL`

Default`"CODE"`

Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.

### Responses

**200** Request completed successfully.

Request completed successfully.

[`views`](https://docs.databricks.com/api/azure/workspace/jobs_21/exportrun#views) Array of object

The exported content in HTML format (one for every view item). To extract the HTML notebook from the JSON response, download and run this [Python script](https://docs.databricks.com/en/_static/examples/extract.py).

Array \[\
\
[`content`](https://docs.databricks.com/api/azure/workspace/jobs_21/exportrun#views-content) string\
\
Content of the view.\
\
[`name`](https://docs.databricks.com/api/azure/workspace/jobs_21/exportrun#views-name) string\
\
Name of the view item. In the case of code view, it would be the notebook’s name. In the case of dashboard view, it would be the dashboard’s name.\
\
[`type`](https://docs.databricks.com/api/azure/workspace/jobs_21/exportrun#views-type) string\
\
Enum: `NOTEBOOK | DASHBOARD`\
\
Type of the view item.\
\
\]

This method might return the following HTTP codes: 400, 401, 403, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Response samples

200

```
{
  "views": [\
    {\
      "content": "string",\
      "name": "string",\
      "type": "NOTEBOOK"\
    }\
  ]
}
```

## GET /2.1/jobs/runs/get

Retrieve the metadata of a run.

### Query parameters

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#run_id) requiredint64

Example`run_id=455644833`

The canonical identifier of the run for which to retrieve the metadata.
This field is required.

[`include_history`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#include_history) boolean

Default`false`

Example`include_history=true`

Whether to include the repair history in the response.

[`include_resolved_values`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#include_resolved_values) boolean

Default`false`

Whether to include resolved parameter values in the response.

### Responses

**200** Request completed successfully.

Request completed successfully.

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_id) int64

Example`11223344`

The canonical identifier of the job that contains this run.

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#run_id) int64

Example`455644833`

The canonical identifier of the run. This ID is unique across all runs of all jobs.

[`creator_user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#creator_user_name) string

Example`"user.name@databricks.com"`

The creator user name. This field won’t be included in the response if the user has already been deleted.

[`number_in_job`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#number_in_job) int64

Deprecated

Example`455644833`

A unique identifier for this job run. This is set to the same value as `run_id`.

[`original_attempt_run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#original_attempt_run_id) int64

Example`455644833`

If this run is a retry of a prior run attempt, this field contains the run\_id of the original attempt; otherwise, it is the same as the run\_id.

[`state`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#state) object

Deprecated

Deprecated. Please use the `status` field instead.

[`life_cycle_state`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#state-life_cycle_state) string

Enum: `PENDING | RUNNING | TERMINATING | TERMINATED | SKIPPED | INTERNAL_ERROR | BLOCKED | WAITING_FOR_RETRY | QUEUED`

A value indicating the run's current lifecycle state. This field is always available in the response.

[`result_state`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#state-result_state) string

Enum: `SUCCESS | FAILED | TIMEDOUT | CANCELED | MAXIMUM_CONCURRENT_RUNS_REACHED | UPSTREAM_CANCELED | UPSTREAM_FAILED | EXCLUDED | SUCCESS_WITH_FAILURES | DISABLED`

A value indicating the run's result. This field is only available for terminal lifecycle states.

[`state_message`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#state-state_message) string

A descriptive message for the current state. This field is unstructured, and its exact format is subject to change.

[`user_cancelled_or_timedout`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#state-user_cancelled_or_timedout) boolean

Default`false`

A value indicating whether a run was canceled manually by a user or by the scheduler because the run timed out.

[`queue_reason`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#state-queue_reason) string

Example`"Queued due to reaching maximum concurrent runs of 1."`

The reason indicating why the run was queued.

[`schedule`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#schedule) object

The cron schedule that triggered this run if it was triggered by the periodic scheduler.

[`quartz_cron_expression`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#schedule-quartz_cron_expression) requiredstring

Example`"20 30 * * * ?"`

A Cron expression using Quartz syntax that describes the schedule for a job. See [Cron Trigger](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) for details. This field is required.

[`timezone_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#schedule-timezone_id) requiredstring

Example`"Europe/London"`

A Java timezone ID. The schedule for a job is resolved with respect to this timezone. See [Java TimeZone](https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html) for details. This field is required.

[`pause_status`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#schedule-pause_status) string

Enum: `UNPAUSED | PAUSED`

Default`"UNPAUSED"`

Indicate whether this schedule is paused or not.

[`cluster_spec`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cluster_spec) object

A snapshot of the job’s cluster specification when this run was created.

[`existing_cluster_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cluster_spec-existing_cluster_id) string

Example`"0923-164208-meows279"`

If existing\_cluster\_id, the ID of an existing cluster that is used for all runs.
When running jobs or tasks on an existing cluster, you may need to manually restart
the cluster if it stops responding. We suggest running jobs and tasks on new clusters for
greater reliability

[`new_cluster`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cluster_spec-new_cluster) object

If new\_cluster, a description of a new cluster that is created for each run.

[`job_cluster_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cluster_spec-job_cluster_key) string

\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$

If job\_cluster\_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`.

[`libraries`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cluster_spec-libraries) Array of object

An optional list of libraries to be installed on the cluster.
The default value is an empty list.

[`cluster_instance`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cluster_instance) object

The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.

[`cluster_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cluster_instance-cluster_id) string

Example`"0923-164208-meows279"`

The canonical identifier for the cluster used by a run. This field is always available for runs on existing clusters. For runs on new clusters, it becomes available once the cluster is created. This value can be used to view logs by browsing to `/#setting/sparkui/$cluster_id/driver-logs`. The logs continue to be available after the run completes.

The response won’t include this field if the identifier is not available yet.

[`spark_context_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cluster_instance-spark_context_id) string

The canonical identifier for the Spark context used by a run. This field is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues to be available after the run has completed.

The response won’t include this field if the identifier is not available yet.

[`job_parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_parameters) Array of object

Job-level parameters used in the run

Array \[\
\
[`name`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_parameters-name) string\
\
Example`"table"`\
\
The name of the parameter\
\
[`default`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_parameters-default) string\
\
Example`"users"`\
\
The optional default value of the parameter\
\
[`value`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_parameters-value) string\
\
Example`"customers"`\
\
The value used in the run\
\
\]

[`overriding_parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters) object

The parameters used for this run.

[`pipeline_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters-pipeline_params) object

Controls whether the pipeline should perform a full refresh

[`jar_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters-jar_params) Array of string

Deprecated

Example

A list of parameters for jobs with Spark JAR tasks, for example `"jar_params": ["john doe", "35"]`.
The parameters are used to invoke the main function of the main class specified in the Spark JAR task.
If not specified upon `run-now`, it defaults to an empty list.
jar\_params cannot be specified in conjunction with notebook\_params.
The JSON representation of this field (for example `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.

Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.

[`notebook_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters-notebook_params) object

Deprecated

Example

A map from keys to values for jobs with notebook task, for example `"notebook_params": {"name": "john doe", "age": "35"}`.
The map is passed to the notebook and is accessible through the [dbutils.widgets.get](https://docs.databricks.com/dev-tools/databricks-utils.html) function.

If not specified upon `run-now`, the triggered run uses the job’s base parameters.

notebook\_params cannot be specified in conjunction with jar\_params.

Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.

The JSON representation of this field (for example `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot exceed 10,000 bytes.

[`python_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters-python_params) Array of string

Deprecated

Example

A list of parameters for jobs with Python tasks, for example `"python_params": ["john doe", "35"]`.
The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite
the parameters specified in job setting. The JSON representation of this field (for example `{"python_params":["john doe","35"]}`)
cannot exceed 10,000 bytes.

Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.

Important

These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error.
Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis.

[`spark_submit_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters-spark_submit_params) Array of string

Deprecated

Example

A list of parameters for jobs with spark submit task, for example `"spark_submit_params": ["--class", "org.apache.spark.examples.SparkPi"]`.
The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the
parameters specified in job setting. The JSON representation of this field (for example `{"python_params":["john doe","35"]}`)
cannot exceed 10,000 bytes.

Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs

Important

These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error.
Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis.

[`python_named_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters-python_named_params) object

Deprecated

Example

[`sql_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters-sql_params) object

Deprecated

Example

A map from keys to values for jobs with SQL task, for example `"sql_params": {"name": "john doe", "age": "35"}`. The SQL alert task does not support custom parameters.

[`dbt_commands`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#overriding_parameters-dbt_commands) Array of string

Deprecated

Example

An array of commands to execute for jobs with the dbt task, for example `"dbt_commands": ["dbt deps", "dbt seed", "dbt deps", "dbt seed", "dbt run"]`

[`start_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#start_time) int64

Example`1625060460483`

The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued.

[`setup_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#setup_duration) int64

Example`0`

The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.

[`execution_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#execution_duration) int64

Example`0`

The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.

[`cleanup_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#cleanup_duration) int64

Example`0`

The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.

[`end_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#end_time) int64

Example`1625060863413`

The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running.

[`run_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#run_duration) int64

Example`110183`

The time in milliseconds it took the job run and all of its repairs to finish.

[`queue_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#queue_duration) int64

Example`1625060863413`

The time in milliseconds that the run has spent in the queue.

[`trigger`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#trigger) string

Enum: `PERIODIC | ONE_TIME | RETRY | RUN_JOB_TASK | FILE_ARRIVAL | TABLE`

The type of trigger that fired this run.

- `PERIODIC`: Schedules that periodically trigger runs, such as a cron scheduler.
- `ONE_TIME`: One time triggers that fire a single run. This occurs you triggered a single run on demand through the UI or the API.
- `RETRY`: Indicates a run that is triggered as a retry of a previously failed run. This occurs when you request to re-run the job in case of failures.
- `RUN_JOB_TASK`: Indicates a run that is triggered using a Run Job task.
- `FILE_ARRIVAL`: Indicates a run that is triggered by a file arrival.
- `TABLE`: Indicates a run that is triggered by a table update.
- `CONTINUOUS_RESTART`: Indicates a run created by user to manually restart a continuous job run.

[`trigger_info`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#trigger_info) object

Additional details about what triggered the run

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#trigger_info-run_id) int64

The run id of the Run Job task run

[`run_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#run_name) string

<= 4096 characters

Default`"Untitled"`

Example`"A multitask job run"`

An optional name for the run. The maximum length is 4096 bytes in UTF-8 encoding.

[`run_page_url`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#run_page_url) string

Example`"https://my-workspace.cloud.databricks.com/#job/11223344/run/123"`

The URL to the detail page of the run.

[`run_type`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#run_type) string

Enum: `JOB_RUN | WORKFLOW_RUN | SUBMIT_RUN`

The type of a run.

- `JOB_RUN`: Normal job run. A run created with [jobs/runnow](https://docs.databricks.com/api/azure/workspace/jobs/runnow).
- `WORKFLOW_RUN`: Workflow run. A run created with [dbutils.notebook.run](https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow).
- `SUBMIT_RUN`: Submit run. A run created with [jobs/submit](https://docs.databricks.com/api/azure/workspace/jobs/submit).

[`tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks) Array of object

<= 100 items

Example

The list of tasks performed by the run. Each task has its own `run_id` which you can use to call `JobsGetOutput` to retrieve the run resutls.
If more than 100 tasks are available, you can paginate through them using [jobs/getrun](https://docs.databricks.com/api/azure/workspace/jobs/getrun). Use the `next_page_token` field at the object root to determine if more results are available.

Array \[\
\
[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-run_id) int64\
\
Example`99887766`\
\
The ID of the task run.\
\
[`task_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-task_key) requiredstring\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
Example`"Task_Key"`\
\
A unique name for the task. This field is used to refer to this task from other tasks.\
This field is required and must be unique within its parent job.\
On Update or Reset, this field is used to reference the tasks to be updated or reset.\
\
[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-description) string\
\
<= 1000 characters\
\
Example`"This is the description for this task."`\
\
An optional description for this task.\
\
[`depends_on`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-depends_on) Array of object\
\
An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task.\
The key is `task_key`, and the value is the name assigned to the dependent task.\
\
[`run_if`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-run_if) string\
\
Enum: `ALL_SUCCESS | ALL_DONE | NONE_FAILED | AT_LEAST_ONE_SUCCESS | ALL_FAILED | AT_LEAST_ONE_FAILED`\
\
Example`"ALL_SUCCESS"`\
\
An optional value indicating the condition that determines whether the task should be run once its dependencies have been completed. When omitted, defaults to `ALL_SUCCESS`. See [jobs/create](https://docs.databricks.com/api/azure/workspace/jobs/create) for a list of possible values.\
\
[`notebook_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-notebook_task) object\
\
The task runs a notebook when the `notebook_task` field is present.\
\
[`spark_jar_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-spark_jar_task) object\
\
The task runs a JAR when the `spark_jar_task` field is present.\
\
[`spark_python_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-spark_python_task) object\
\
The task runs a Python file when the `spark_python_task` field is present.\
\
[`spark_submit_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-spark_submit_task) object\
\
(Legacy) The task runs the spark-submit script when the `spark_submit_task` field is present. This task can run only on new clusters and is not compatible with serverless compute.\
\
In the `new_cluster` specification, `libraries` and `spark_conf` are not supported. Instead, use `--jars` and `--py-files` to add Java and Python libraries and `--conf` to set the Spark configurations.\
\
`master`, `deploy-mode`, and `executor-cores` are automatically configured by Azure Databricks; you _cannot_ specify them in parameters.\
\
By default, the Spark submit job uses all available memory (excluding reserved memory for Azure Databricks services). You can set `--driver-memory`, and `--executor-memory` to a smaller value to leave some room for off-heap usage.\
\
The `--jars`, `--py-files`, `--files` arguments support DBFS and S3 paths.\
\
[`pipeline_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-pipeline_task) object\
\
The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported.\
\
[`python_wheel_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-python_wheel_task) object\
\
The task runs a Python wheel when the `python_wheel_task` field is present.\
\
[`dbt_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-dbt_task) object\
\
The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse.\
\
[`sql_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-sql_task) object\
\
The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present.\
\
[`run_job_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-run_job_task) object\
\
The task triggers another job when the `run_job_task` field is present.\
\
[`condition_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-condition_task) object\
\
The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present.\
The condition task does not require a cluster to execute and does not support retries or notifications.\
\
[`for_each_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-for_each_task) object\
\
The task executes a nested task for every input provided when the `for_each_task` field is present.\
\
[`clean_rooms_notebook_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-clean_rooms_notebook_task) object\
\
Public preview\
\
The task runs a [clean rooms](https://docs.databricks.com/en/clean-rooms/index.html) notebook\
when the `clean_rooms_notebook_task` field is present.\
\
[`existing_cluster_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-existing_cluster_id) string\
\
Example`"0923-164208-meows279"`\
\
If existing\_cluster\_id, the ID of an existing cluster that is used for all runs.\
When running jobs or tasks on an existing cluster, you may need to manually restart\
the cluster if it stops responding. We suggest running jobs and tasks on new clusters for\
greater reliability\
\
[`new_cluster`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-new_cluster) object\
\
If new\_cluster, a description of a new cluster that is created for each run.\
\
[`job_cluster_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-job_cluster_key) string\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
If job\_cluster\_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`.\
\
[`libraries`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-libraries) Array of object\
\
An optional list of libraries to be installed on the cluster.\
The default value is an empty list.\
\
[`timeout_seconds`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-timeout_seconds) int32\
\
Default`0`\
\
Example`86400`\
\
An optional timeout applied to each run of this job task. A value of `0` means no timeout.\
\
[`email_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-email_notifications) object\
\
Default`{}`\
\
An optional set of email addresses notified when the task run begins or completes. The default behavior is to not send any emails.\
\
[`notification_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-notification_settings) object\
\
Default`{}`\
\
Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task run.\
\
[`webhook_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-webhook_notifications) object\
\
Default`{}`\
\
A collection of system notification IDs to notify when the run begins or completes. The default behavior is to not send any system notifications. Task webhooks respect the task notification settings.\
\
[`environment_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-environment_key) string\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute.\
\
[`state`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-state) object\
\
Deprecated\
\
Deprecated. Please use the `status` field instead.\
\
[`run_page_url`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-run_page_url) string\
\
[`start_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-start_time) int64\
\
Example`1625060460483`\
\
The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued.\
\
[`setup_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-setup_duration) int64\
\
Example`0`\
\
The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.\
\
[`execution_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-execution_duration) int64\
\
Example`0`\
\
The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.\
\
[`cleanup_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-cleanup_duration) int64\
\
Example`0`\
\
The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.\
\
[`end_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-end_time) int64\
\
Example`1625060863413`\
\
The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running.\
\
[`run_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-run_duration) int64\
\
Example`110183`\
\
The time in milliseconds it took the job run and all of its repairs to finish.\
\
[`queue_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-queue_duration) int64\
\
Example`1625060863413`\
\
The time in milliseconds that the run has spent in the queue.\
\
[`cluster_instance`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-cluster_instance) object\
\
The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.\
\
[`attempt_number`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-attempt_number) int32\
\
Example`0`\
\
The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt\_number of 0. If the initial run attempt fails, and the job has a retry policy (`max_retries` \> 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job.\
\
[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-git_source) object\
\
Example\
\
An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks. If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task. Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.\
\
[`resolved_values`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-resolved_values) object\
\
Parameter values including resolved references\
\
[`status`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#tasks-status) object\
\
The current status of the run\
\
\]

[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#description) string

Description of the run

[`attempt_number`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#attempt_number) int32

Example`0`

The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt\_number of 0. If the initial run attempt fails, and the job has a retry policy (`max_retries` \> 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job.

[`job_clusters`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_clusters) Array of object

<= 100 items

Example

A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
If more than 100 job clusters are available, you can paginate through them using [jobs/getrun](https://docs.databricks.com/api/azure/workspace/jobs/getrun).

Array \[\
\
[`job_cluster_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_clusters-job_cluster_key) requiredstring\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
Example`"auto_scaling_cluster"`\
\
A unique name for the job cluster. This field is required and must be unique within the job.\
`JobTaskSettings` may refer to this field to determine which cluster to launch for the task execution.\
\
[`new_cluster`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_clusters-new_cluster) object\
\
If new\_cluster, a description of a cluster that is created for each task.\
\
\]

[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#git_source) object

Example

An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.

If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.

Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.

[`git_url`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#git_source-git_url) requiredstring

<= 300 characters

Example`"https://github.com/databricks/databricks-cli"`

URL of the repository to be cloned by this job.

[`git_provider`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#git_source-git_provider) requiredstring

Enum: `gitHub | bitbucketCloud | azureDevOpsServices | gitHubEnterprise | bitbucketServer | gitLab | gitLabEnterpriseEdition | awsCodeCommit`

Unique identifier of the service used to host the Git repository. The value is case insensitive.

[`git_branch`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#git_source-git_branch) string

<= 255 characters

Example`"main"`

Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git\_tag or git\_commit.

[`git_tag`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#git_source-git_tag) string

<= 255 characters

Example`"release-1.0.0"`

Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git\_branch or git\_commit.

[`git_commit`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#git_source-git_commit) string

<= 64 characters

Example`"e0056d01"`

Commit to be checked out and used by this job. This field cannot be specified in conjunction with git\_branch or git\_tag.

[`git_snapshot`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#git_source-git_snapshot) object

Read-only state of the remote repository at the time the job was run. This field is only included on job runs.

[`repair_history`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#repair_history) Array of object

The repair history of the run.

Array \[\
\
[`type`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#repair_history-type) string\
\
Enum: `ORIGINAL | REPAIR`\
\
The repair history item type. Indicates whether a run is the original run or a repair run.\
\
[`start_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#repair_history-start_time) int64\
\
Example`1625060460483`\
\
The start time of the (repaired) run.\
\
[`end_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#repair_history-end_time) int64\
\
Example`1625060863413`\
\
The end time of the (repaired) run.\
\
[`state`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#repair_history-state) object\
\
Deprecated\
\
Deprecated. Please use the `status` field instead.\
\
[`id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#repair_history-id) int64\
\
Example`734650698524280`\
\
The ID of the repair. Only returned for the items that represent a repair in `repair_history`.\
\
[`task_run_ids`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#repair_history-task_run_ids) Array of int64\
\
Example\
\
The run IDs of the task runs that ran as part of this repair history item.\
\
[`status`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#repair_history-status) object\
\
The current status of the run\
\
\]

[`status`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#status) object

The current status of the run

[`state`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#status-state) string

Enum: `BLOCKED | PENDING | QUEUED | RUNNING | TERMINATING | TERMINATED`

The current state of the run.

[`termination_details`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#status-termination_details) object

If the run is in a TERMINATING or TERMINATED state, details about the reason for terminating the run.

[`queue_details`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#status-queue_details) object

If the run was queued, details about the reason for queuing the run.

[`job_run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrun#job_run_id) int64

ID of the job run that this run belongs to.
For legacy and single-task job runs the field is populated with the job run ID.
For task runs, the field is populated with the ID of the job run that the task run belongs to.

This method might return the following HTTP codes: 400, 401, 403, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Response samples

200

```
{
  "job_id": 11223344,
  "run_id": 455644833,
  "creator_user_name": "user.name@databricks.com",
  "number_in_job": 455644833,
  "original_attempt_run_id": 455644833,
  "state": {
    "life_cycle_state": "PENDING",
    "result_state": "SUCCESS",
    "state_message": "string",
    "user_cancelled_or_timedout": false,
    "queue_reason": "Queued due to reaching maximum concurrent runs of 1."
  },
  "schedule": {
    "quartz_cron_expression": "20 30 * * * ?",
    "timezone_id": "Europe/London",
    "pause_status": "UNPAUSED"
  },
  "cluster_spec": {
    "existing_cluster_id": "0923-164208-meows279",
    "new_cluster": {
      "num_workers": 0,
      "autoscale": {
        "min_workers": 0,
        "max_workers": 0
      },
      "kind": "CLASSIC_PREVIEW",
      "cluster_name": "string",
      "spark_version": "string",
      "use_ml_runtime": true,
      "is_single_node": true,
      "spark_conf": {
        "property1": "string",
        "property2": "string"
      },
      "azure_attributes": {
        "log_analytics_info": {
          "log_analytics_workspace_id": "string",
          "log_analytics_primary_key": "string"
        },
        "first_on_demand": "1",
        "availability": "SPOT_AZURE",
        "spot_bid_max_price": "-1.0"
      },
      "node_type_id": "string",
      "driver_node_type_id": "string",
      "ssh_public_keys": [\
        "string"\
      ],
      "custom_tags": {
        "property1": "string",
        "property2": "string"
      },
      "cluster_log_conf": {
        "dbfs": {
          "destination": "string"
        }
      },
      "init_scripts": [\
        {\
          "workspace": {\
            "destination": "string"\
          },\
          "volumes": {\
            "destination": "string"\
          },\
          "file": {\
            "destination": "string"\
          },\
          "dbfs": {\
            "destination": "string"\
          },\
          "abfss": {\
            "destination": "string"\
          },\
          "gcs": {\
            "destination": "string"\
          }\
        }\
      ],
      "spark_env_vars": {
        "property1": "string",
        "property2": "string"
      },
      "autotermination_minutes": 0,
      "enable_elastic_disk": true,
      "instance_pool_id": "string",
      "policy_id": "string",
      "enable_local_disk_encryption": true,
      "driver_instance_pool_id": "string",
      "workload_type": {
        "clients": {
          "notebooks": "true",
          "jobs": "true"
        }
      },
      "runtime_engine": "NULL",
      "docker_image": {
        "url": "string",
        "basic_auth": {
          "username": "string",
          "password": "string"
        }
      },
      "data_security_mode": "DATA_SECURITY_MODE_AUTO",
      "single_user_name": "string",
      "apply_policy_default_values": false
    },
    "job_cluster_key": "string",
    "libraries": [\
      {\
        "jar": "string",\
        "egg": "string",\
        "pypi": {\
          "package": "string",\
          "repo": "string"\
        },\
        "maven": {\
          "coordinates": "string",\
          "repo": "string",\
          "exclusions": [\
            "string"\
          ]\
        },\
        "cran": {\
          "package": "string",\
          "repo": "string"\
        },\
        "whl": "string",\
        "requirements": "string"\
      }\
    ]
  },
  "cluster_instance": {
    "cluster_id": "0923-164208-meows279",
    "spark_context_id": "string"
  },
  "job_parameters": [\
    {\
      "default": "users",\
      "name": "table",\
      "value": "customers"\
    }\
  ],
  "overriding_parameters": {
    "pipeline_params": {
      "full_refresh": false
    },
    "jar_params": [\
      "john",\
      "doe",\
      "35"\
    ],
    "notebook_params": {
      "age": "35",
      "name": "john doe"
    },
    "python_params": [\
      "john doe",\
      "35"\
    ],
    "spark_submit_params": [\
      "--class",\
      "org.apache.spark.examples.SparkPi"\
    ],
    "python_named_params": {
      "data": "dbfs:/path/to/data.json",
      "name": "task"
    },
    "sql_params": {
      "age": "35",
      "name": "john doe"
    },
    "dbt_commands": [\
      "dbt deps",\
      "dbt seed",\
      "dbt run"\
    ]
  },
  "start_time": 1625060460483,
  "setup_duration": 0,
  "execution_duration": 0,
  "cleanup_duration": 0,
  "end_time": 1625060863413,
  "run_duration": 110183,
  "queue_duration": 1625060863413,
  "trigger": "PERIODIC",
  "trigger_info": {
    "run_id": 0
  },
  "run_name": "A multitask job run",
  "run_page_url": "https://my-workspace.cloud.databricks.com/#job/11223344/run/123",
  "run_type": "JOB_RUN",
  "tasks": [\
    {\
      "setup_duration": 0,\
      "start_time": 1629989929660,\
      "task_key": "Orders_Ingest",\
      "state": {\
        "life_cycle_state": "INTERNAL_ERROR",\
        "result_state": "FAILED",\
        "state_message": "Library installation failed for library due to user error. Error messages:\n'Manage' permissions are required to install libraries on a cluster",\
        "user_cancelled_or_timedout": false\
      },\
      "description": "Ingests order data",\
      "job_cluster_key": "auto_scaling_cluster",\
      "end_time": 1629989930171,\
      "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/20",\
      "run_id": 2112892,\
      "cluster_instance": {\
        "cluster_id": "0923-164208-meows279",\
        "spark_context_id": "4348585301701786933"\
      },\
      "spark_jar_task": {\
        "main_class_name": "com.databricks.OrdersIngest"\
      },\
      "libraries": [\
        {\
          "jar": "dbfs:/mnt/databricks/OrderIngest.jar"\
        }\
      ],\
      "attempt_number": 0,\
      "cleanup_duration": 0,\
      "execution_duration": 0,\
      "run_if": "ALL_SUCCESS"\
    },\
    {\
      "setup_duration": 0,\
      "start_time": 0,\
      "task_key": "Match",\
      "state": {\
        "life_cycle_state": "SKIPPED",\
        "state_message": "An upstream task failed.",\
        "user_cancelled_or_timedout": false\
      },\
      "description": "Matches orders with user sessions",\
      "notebook_task": {\
        "notebook_path": "/Users/user.name@databricks.com/Match",\
        "source": "WORKSPACE"\
      },\
      "end_time": 1629989930238,\
      "depends_on": [\
        {\
          "task_key": "Orders_Ingest"\
        },\
        {\
          "task_key": "Sessionize"\
        }\
      ],\
      "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/21",\
      "new_cluster": {\
        "autoscale": {\
          "max_workers": 16,\
          "min_workers": 2\
        },\
        "node_type_id": null,\
        "spark_conf": {\
          "spark.speculation": true\
        },\
        "spark_version": "7.3.x-scala2.12"\
      },\
      "run_id": 2112897,\
      "cluster_instance": {\
        "cluster_id": "0923-164208-meows279"\
      },\
      "attempt_number": 0,\
      "cleanup_duration": 0,\
      "execution_duration": 0,\
      "run_if": "ALL_SUCCESS"\
    },\
    {\
      "setup_duration": 0,\
      "start_time": 1629989929668,\
      "task_key": "Sessionize",\
      "state": {\
        "life_cycle_state": "INTERNAL_ERROR",\
        "result_state": "FAILED",\
        "state_message": "Library installation failed for library due to user error. Error messages:\n'Manage' permissions are required to install libraries on a cluster",\
        "user_cancelled_or_timedout": false\
      },\
      "description": "Extracts session data from events",\
      "end_time": 1629989930144,\
      "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/22",\
      "run_id": 2112902,\
      "cluster_instance": {\
        "cluster_id": "0923-164208-meows279",\
        "spark_context_id": "4348585301701786933"\
      },\
      "spark_jar_task": {\
        "main_class_name": "com.databricks.Sessionize"\
      },\
      "libraries": [\
        {\
          "jar": "dbfs:/mnt/databricks/Sessionize.jar"\
        }\
      ],\
      "attempt_number": 0,\
      "existing_cluster_id": "0923-164208-meows279",\
      "cleanup_duration": 0,\
      "execution_duration": 0,\
      "run_if": "ALL_SUCCESS"\
    }\
  ],
  "description": "string",
  "attempt_number": 0,
  "job_clusters": [\
    {\
      "job_cluster_key": "auto_scaling_cluster",\
      "new_cluster": {\
        "autoscale": {\
          "max_workers": 16,\
          "min_workers": 2\
        },\
        "node_type_id": null,\
        "spark_conf": {\
          "spark.speculation": true\
        },\
        "spark_version": "7.3.x-scala2.12"\
      }\
    }\
  ],
  "git_source": {
    "git_branch": "main",
    "git_provider": "gitHub",
    "git_url": "https://github.com/databricks/databricks-cli"
  },
  "repair_history": [\
    {\
      "type": "ORIGINAL",\
      "start_time": 1625060460483,\
      "end_time": 1625060863413,\
      "state": {\
        "life_cycle_state": "PENDING",\
        "result_state": "SUCCESS",\
        "state_message": "string",\
        "user_cancelled_or_timedout": false,\
        "queue_reason": "Queued due to reaching maximum concurrent runs of 1."\
      },\
      "id": 734650698524280,\
      "task_run_ids": [\
        1106460542112844,\
        988297789683452\
      ],\
      "status": {\
        "state": "BLOCKED",\
        "termination_details": {\
          "code": "SUCCESS",\
          "type": "SUCCESS",\
          "message": "string"\
        },\
        "queue_details": {\
          "code": "ACTIVE_RUNS_LIMIT_REACHED",\
          "message": "string"\
        }\
      }\
    }\
  ],
  "status": {
    "state": "BLOCKED",
    "termination_details": {
      "code": "SUCCESS",
      "type": "SUCCESS",
      "message": "string"
    },
    "queue_details": {
      "code": "ACTIVE_RUNS_LIMIT_REACHED",
      "message": "string"
    }
  },
  "job_run_id": 0
}
```

## GET /2.1/jobs/runs/get-output

Retrieve the output and metadata of a single task run. When a notebook task returns
a value through the `dbutils.notebook.exit()` call, you can use this endpoint to retrieve
that value. Azure Databricks restricts this API to returning the first 5 MB of the output.
To return a larger result, you can store job results in a cloud storage service.

This endpoint validates that the run\_id parameter is valid and returns an HTTP status
code 400 if the run\_id parameter is invalid. Runs are automatically removed after
60 days. If you to want to reference them beyond 60 days, you must save old run results
before they expire.

### Query parameters

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#run_id) requiredint64

Example`run_id=455644833`

The canonical identifier for the run.

### Responses

**200** Request completed successfully.

Request completed successfully.

[`metadata`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata) object

All details of the run except for its output.

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-job_id) int64

Example`11223344`

The canonical identifier of the job that contains this run.

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-run_id) int64

Example`455644833`

The canonical identifier of the run. This ID is unique across all runs of all jobs.

[`creator_user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-creator_user_name) string

Example`"user.name@databricks.com"`

The creator user name. This field won’t be included in the response if the user has already been deleted.

[`number_in_job`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-number_in_job) int64

Deprecated

Example`455644833`

A unique identifier for this job run. This is set to the same value as `run_id`.

[`original_attempt_run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-original_attempt_run_id) int64

Example`455644833`

If this run is a retry of a prior run attempt, this field contains the run\_id of the original attempt; otherwise, it is the same as the run\_id.

[`state`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-state) object

Deprecated

Deprecated. Please use the `status` field instead.

[`schedule`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-schedule) object

The cron schedule that triggered this run if it was triggered by the periodic scheduler.

[`cluster_spec`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-cluster_spec) object

A snapshot of the job’s cluster specification when this run was created.

[`cluster_instance`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-cluster_instance) object

The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.

[`job_parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-job_parameters) Array of object

Job-level parameters used in the run

[`overriding_parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-overriding_parameters) object

The parameters used for this run.

[`start_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-start_time) int64

Example`1625060460483`

The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued.

[`setup_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-setup_duration) int64

Example`0`

The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.

[`execution_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-execution_duration) int64

Example`0`

The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.

[`cleanup_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-cleanup_duration) int64

Example`0`

The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.

[`end_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-end_time) int64

Example`1625060863413`

The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running.

[`run_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-run_duration) int64

Example`110183`

The time in milliseconds it took the job run and all of its repairs to finish.

[`queue_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-queue_duration) int64

Example`1625060863413`

The time in milliseconds that the run has spent in the queue.

[`trigger`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-trigger) string

Enum: `PERIODIC | ONE_TIME | RETRY | RUN_JOB_TASK | FILE_ARRIVAL | TABLE`

The type of trigger that fired this run.

- `PERIODIC`: Schedules that periodically trigger runs, such as a cron scheduler.
- `ONE_TIME`: One time triggers that fire a single run. This occurs you triggered a single run on demand through the UI or the API.
- `RETRY`: Indicates a run that is triggered as a retry of a previously failed run. This occurs when you request to re-run the job in case of failures.
- `RUN_JOB_TASK`: Indicates a run that is triggered using a Run Job task.
- `FILE_ARRIVAL`: Indicates a run that is triggered by a file arrival.
- `TABLE`: Indicates a run that is triggered by a table update.
- `CONTINUOUS_RESTART`: Indicates a run created by user to manually restart a continuous job run.

[`trigger_info`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-trigger_info) object

Additional details about what triggered the run

[`run_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-run_name) string

<= 4096 characters

Default`"Untitled"`

Example`"A multitask job run"`

An optional name for the run. The maximum length is 4096 bytes in UTF-8 encoding.

[`run_page_url`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-run_page_url) string

Example`"https://my-workspace.cloud.databricks.com/#job/11223344/run/123"`

The URL to the detail page of the run.

[`run_type`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-run_type) string

Enum: `JOB_RUN | WORKFLOW_RUN | SUBMIT_RUN`

The type of a run.

- `JOB_RUN`: Normal job run. A run created with [jobs/runnow](https://docs.databricks.com/api/azure/workspace/jobs/runnow).
- `WORKFLOW_RUN`: Workflow run. A run created with [dbutils.notebook.run](https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow).
- `SUBMIT_RUN`: Submit run. A run created with [jobs/submit](https://docs.databricks.com/api/azure/workspace/jobs/submit).

[`tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-tasks) Array of object

<= 100 items

Example

The list of tasks performed by the run. Each task has its own `run_id` which you can use to call `JobsGetOutput` to retrieve the run resutls.
If more than 100 tasks are available, you can paginate through them using [jobs/getrun](https://docs.databricks.com/api/azure/workspace/jobs/getrun). Use the `next_page_token` field at the object root to determine if more results are available.

[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-description) string

Description of the run

[`attempt_number`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-attempt_number) int32

Example`0`

The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt\_number of 0. If the initial run attempt fails, and the job has a retry policy (`max_retries` \> 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job.

[`job_clusters`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-job_clusters) Array of object

<= 100 items

Example

A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
If more than 100 job clusters are available, you can paginate through them using [jobs/getrun](https://docs.databricks.com/api/azure/workspace/jobs/getrun).

[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-git_source) object

Example

An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.

If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.

Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.

[`repair_history`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-repair_history) Array of object

The repair history of the run.

[`status`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-status) object

The current status of the run

[`job_run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#metadata-job_run_id) int64

ID of the job run that this run belongs to.
For legacy and single-task job runs the field is populated with the job run ID.
For task runs, the field is populated with the ID of the job run that the task run belongs to.

[`error`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#error) string

Example`"ZeroDivisionError: integer division or modulo by zero"`

An error message indicating why a task failed or why output is not available. The message is unstructured, and its exact format is subject to change.

[`logs`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#logs) string

Example`"Hello World!"`

The output from tasks that write to standard streams (stdout/stderr) such as
spark\_jar\_task, spark\_python\_task, python\_wheel\_task.

It's not supported for the notebook\_task, pipeline\_task or spark\_submit\_task.

Azure Databricks restricts this API to return the last 5 MB of these logs.

[`logs_truncated`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#logs_truncated) boolean

Example`true`

Whether the logs are truncated.

[`error_trace`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#error_trace) string

If there was an error executing the run, this field contains any available stack traces.

[`info`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#info) string

[`notebook_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#notebook_output) object

The output of a notebook task, if available. A notebook task that terminates (either successfully or with a failure)
without calling `dbutils.notebook.exit()` is considered to have an empty output.
This field is set but its result value is empty. Azure Databricks restricts this API to return the first 5 MB of the output.
To return a larger result, use the [ClusterLogConf](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/clusters#clusterlogconf) field to configure log storage
for the job cluster.

[`result`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#notebook_output-result) string

Example`"An arbitrary string passed by calling dbutils.notebook.exit(...)"`

The value passed to [dbutils.notebook.exit()](https://docs.databricks.com/notebooks/notebook-workflows.html#notebook-workflows-exit).
Azure Databricks restricts this API to return the first 5 MB of the value. For a larger result, your job can store the results in a cloud storage service.
This field is absent if `dbutils.notebook.exit()` was never called.

[`truncated`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#notebook_output-truncated) boolean

Example`false`

Whether or not the result was truncated.

[`sql_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#sql_output) object

The output of a SQL task, if available.

[`query_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#sql_output-query_output) object

The output of a SQL query task, if available.

[`dashboard_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#sql_output-dashboard_output) object

The output of a SQL dashboard task, if available.

[`alert_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#sql_output-alert_output) object

The output of a SQL alert task, if available.

[`dbt_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#dbt_output) object

The output of a dbt task, if available.

[`artifacts_link`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#dbt_output-artifacts_link) string

A pre-signed URL to download the (compressed) dbt artifacts. This link is valid for a limited time (30 minutes). This information is only available after the run has finished.

[`artifacts_headers`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#dbt_output-artifacts_headers) object

An optional map of headers to send when retrieving the artifact from the `artifacts_link`.

[`run_job_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#run_job_output) object

The output of a run job task, if available

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#run_job_output-run_id) int64

The run id of the triggered job run

[`clean_rooms_notebook_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#clean_rooms_notebook_output) object

Public preview

The output of a clean rooms notebook task, if available

[`clean_room_job_run_state`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#clean_rooms_notebook_output-clean_room_job_run_state) object

The run state of the clean rooms notebook task.

[`notebook_output`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#clean_rooms_notebook_output-notebook_output) object

The notebook output for the clean room run

[`output_schema_info`](https://docs.databricks.com/api/azure/workspace/jobs_21/getrunoutput#clean_rooms_notebook_output-output_schema_info) object

Information on how to access the output schema for the clean room run

This method might return the following HTTP codes: 400, 401, 403, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Response samples

200

```
{
  "metadata": {
    "job_id": 11223344,
    "run_id": 455644833,
    "creator_user_name": "user.name@databricks.com",
    "number_in_job": 455644833,
    "original_attempt_run_id": 455644833,
    "state": {
      "life_cycle_state": "PENDING",
      "result_state": "SUCCESS",
      "state_message": "string",
      "user_cancelled_or_timedout": false,
      "queue_reason": "Queued due to reaching maximum concurrent runs of 1."
    },
    "schedule": {
      "quartz_cron_expression": "20 30 * * * ?",
      "timezone_id": "Europe/London",
      "pause_status": "UNPAUSED"
    },
    "cluster_spec": {
      "existing_cluster_id": "0923-164208-meows279",
      "new_cluster": {
        "num_workers": 0,
        "autoscale": {
          "min_workers": 0,
          "max_workers": 0
        },
        "kind": "CLASSIC_PREVIEW",
        "cluster_name": "string",
        "spark_version": "string",
        "use_ml_runtime": true,
        "is_single_node": true,
        "spark_conf": {
          "property1": "string",
          "property2": "string"
        },
        "azure_attributes": {
          "log_analytics_info": {
            "log_analytics_workspace_id": "string",
            "log_analytics_primary_key": "string"
          },
          "first_on_demand": "1",
          "availability": "SPOT_AZURE",
          "spot_bid_max_price": "-1.0"
        },
        "node_type_id": "string",
        "driver_node_type_id": "string",
        "ssh_public_keys": [\
          "string"\
        ],
        "custom_tags": {
          "property1": "string",
          "property2": "string"
        },
        "cluster_log_conf": {
          "dbfs": {
            "destination": "string"
          }
        },
        "init_scripts": [\
          {\
            "workspace": {\
              "destination": "string"\
            },\
            "volumes": {\
              "destination": "string"\
            },\
            "file": {\
              "destination": "string"\
            },\
            "dbfs": {\
              "destination": "string"\
            },\
            "abfss": {\
              "destination": "string"\
            },\
            "gcs": {\
              "destination": "string"\
            }\
          }\
        ],
        "spark_env_vars": {
          "property1": "string",
          "property2": "string"
        },
        "autotermination_minutes": 0,
        "enable_elastic_disk": true,
        "instance_pool_id": "string",
        "policy_id": "string",
        "enable_local_disk_encryption": true,
        "driver_instance_pool_id": "string",
        "workload_type": {
          "clients": {
            "notebooks": "true",
            "jobs": "true"
          }
        },
        "runtime_engine": "NULL",
        "docker_image": {
          "url": "string",
          "basic_auth": {
            "username": "string",
            "password": "string"
          }
        },
        "data_security_mode": "DATA_SECURITY_MODE_AUTO",
        "single_user_name": "string",
        "apply_policy_default_values": false
      },
      "job_cluster_key": "string",
      "libraries": [\
        {\
          "jar": "string",\
          "egg": "string",\
          "pypi": {\
            "package": "string",\
            "repo": "string"\
          },\
          "maven": {\
            "coordinates": "string",\
            "repo": "string",\
            "exclusions": [\
              "string"\
            ]\
          },\
          "cran": {\
            "package": "string",\
            "repo": "string"\
          },\
          "whl": "string",\
          "requirements": "string"\
        }\
      ]
    },
    "cluster_instance": {
      "cluster_id": "0923-164208-meows279",
      "spark_context_id": "string"
    },
    "job_parameters": [\
      {\
        "default": "users",\
        "name": "table",\
        "value": "customers"\
      }\
    ],
    "overriding_parameters": {
      "pipeline_params": {
        "full_refresh": false
      },
      "jar_params": [\
        "john",\
        "doe",\
        "35"\
      ],
      "notebook_params": {
        "age": "35",
        "name": "john doe"
      },
      "python_params": [\
        "john doe",\
        "35"\
      ],
      "spark_submit_params": [\
        "--class",\
        "org.apache.spark.examples.SparkPi"\
      ],
      "python_named_params": {
        "data": "dbfs:/path/to/data.json",
        "name": "task"
      },
      "sql_params": {
        "age": "35",
        "name": "john doe"
      },
      "dbt_commands": [\
        "dbt deps",\
        "dbt seed",\
        "dbt run"\
      ]
    },
    "start_time": 1625060460483,
    "setup_duration": 0,
    "execution_duration": 0,
    "cleanup_duration": 0,
    "end_time": 1625060863413,
    "run_duration": 110183,
    "queue_duration": 1625060863413,
    "trigger": "PERIODIC",
    "trigger_info": {
      "run_id": 0
    },
    "run_name": "A multitask job run",
    "run_page_url": "https://my-workspace.cloud.databricks.com/#job/11223344/run/123",
    "run_type": "JOB_RUN",
    "tasks": [\
      {\
        "setup_duration": 0,\
        "start_time": 1629989929660,\
        "task_key": "Orders_Ingest",\
        "state": {\
          "life_cycle_state": "INTERNAL_ERROR",\
          "result_state": "FAILED",\
          "state_message": "Library installation failed for library due to user error. Error messages:\n'Manage' permissions are required to install libraries on a cluster",\
          "user_cancelled_or_timedout": false\
        },\
        "description": "Ingests order data",\
        "job_cluster_key": "auto_scaling_cluster",\
        "end_time": 1629989930171,\
        "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/20",\
        "run_id": 2112892,\
        "cluster_instance": {\
          "cluster_id": "0923-164208-meows279",\
          "spark_context_id": "4348585301701786933"\
        },\
        "spark_jar_task": {\
          "main_class_name": "com.databricks.OrdersIngest"\
        },\
        "libraries": [\
          {\
            "jar": "dbfs:/mnt/databricks/OrderIngest.jar"\
          }\
        ],\
        "attempt_number": 0,\
        "cleanup_duration": 0,\
        "execution_duration": 0,\
        "run_if": "ALL_SUCCESS"\
      },\
      {\
        "setup_duration": 0,\
        "start_time": 0,\
        "task_key": "Match",\
        "state": {\
          "life_cycle_state": "SKIPPED",\
          "state_message": "An upstream task failed.",\
          "user_cancelled_or_timedout": false\
        },\
        "description": "Matches orders with user sessions",\
        "notebook_task": {\
          "notebook_path": "/Users/user.name@databricks.com/Match",\
          "source": "WORKSPACE"\
        },\
        "end_time": 1629989930238,\
        "depends_on": [\
          {\
            "task_key": "Orders_Ingest"\
          },\
          {\
            "task_key": "Sessionize"\
          }\
        ],\
        "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/21",\
        "new_cluster": {\
          "autoscale": {\
            "max_workers": 16,\
            "min_workers": 2\
          },\
          "node_type_id": null,\
          "spark_conf": {\
            "spark.speculation": true\
          },\
          "spark_version": "7.3.x-scala2.12"\
        },\
        "run_id": 2112897,\
        "cluster_instance": {\
          "cluster_id": "0923-164208-meows279"\
        },\
        "attempt_number": 0,\
        "cleanup_duration": 0,\
        "execution_duration": 0,\
        "run_if": "ALL_SUCCESS"\
      },\
      {\
        "setup_duration": 0,\
        "start_time": 1629989929668,\
        "task_key": "Sessionize",\
        "state": {\
          "life_cycle_state": "INTERNAL_ERROR",\
          "result_state": "FAILED",\
          "state_message": "Library installation failed for library due to user error. Error messages:\n'Manage' permissions are required to install libraries on a cluster",\
          "user_cancelled_or_timedout": false\
        },\
        "description": "Extracts session data from events",\
        "end_time": 1629989930144,\
        "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/22",\
        "run_id": 2112902,\
        "cluster_instance": {\
          "cluster_id": "0923-164208-meows279",\
          "spark_context_id": "4348585301701786933"\
        },\
        "spark_jar_task": {\
          "main_class_name": "com.databricks.Sessionize"\
        },\
        "libraries": [\
          {\
            "jar": "dbfs:/mnt/databricks/Sessionize.jar"\
          }\
        ],\
        "attempt_number": 0,\
        "existing_cluster_id": "0923-164208-meows279",\
        "cleanup_duration": 0,\
        "execution_duration": 0,\
        "run_if": "ALL_SUCCESS"\
      }\
    ],
    "description": "string",
    "attempt_number": 0,
    "job_clusters": [\
      {\
        "job_cluster_key": "auto_scaling_cluster",\
        "new_cluster": {\
          "autoscale": {\
            "max_workers": 16,\
            "min_workers": 2\
          },\
          "node_type_id": null,\
          "spark_conf": {\
            "spark.speculation": true\
          },\
          "spark_version": "7.3.x-scala2.12"\
        }\
      }\
    ],
    "git_source": {
      "git_branch": "main",
      "git_provider": "gitHub",
      "git_url": "https://github.com/databricks/databricks-cli"
    },
    "repair_history": [\
      {\
        "type": "ORIGINAL",\
        "start_time": 1625060460483,\
        "end_time": 1625060863413,\
        "state": {\
          "life_cycle_state": "PENDING",\
          "result_state": "SUCCESS",\
          "state_message": "string",\
          "user_cancelled_or_timedout": false,\
          "queue_reason": "Queued due to reaching maximum concurrent runs of 1."\
        },\
        "id": 734650698524280,\
        "task_run_ids": [\
          1106460542112844,\
          988297789683452\
        ],\
        "status": {\
          "state": "BLOCKED",\
          "termination_details": {\
            "code": "SUCCESS",\
            "type": "SUCCESS",\
            "message": "string"\
          },\
          "queue_details": {\
            "code": "ACTIVE_RUNS_LIMIT_REACHED",\
            "message": "string"\
          }\
        }\
      }\
    ],
    "status": {
      "state": "BLOCKED",
      "termination_details": {
        "code": "SUCCESS",
        "type": "SUCCESS",
        "message": "string"
      },
      "queue_details": {
        "code": "ACTIVE_RUNS_LIMIT_REACHED",
        "message": "string"
      }
    },
    "job_run_id": 0
  },
  "error": "ZeroDivisionError: integer division or modulo by zero",
  "logs": "Hello World!",
  "logs_truncated": true,
  "error_trace": "string",
  "info": "string",
  "notebook_output": {
    "result": "An arbitrary string passed by calling dbutils.notebook.exit(...)",
    "truncated": false
  },
  "sql_output": {
    "query_output": {
      "query_text": "string",
      "endpoint_id": "string",
      "sql_statements": [\
        {\
          "lookup_key": "string"\
        }\
      ],
      "output_link": "string",
      "warehouse_id": "string"
    },
    "dashboard_output": {
      "widgets": [\
        {\
          "widget_id": "string",\
          "widget_title": "string",\
          "output_link": "string",\
          "status": "PENDING",\
          "error": {\
            "message": "string"\
          },\
          "start_time": 0,\
          "end_time": 0\
        }\
      ],
      "warehouse_id": "string"
    },
    "alert_output": {
      "query_text": "string",
      "sql_statements": [\
        {\
          "lookup_key": "string"\
        }\
      ],
      "output_link": "string",
      "warehouse_id": "string",
      "alert_state": "UNKNOWN"
    }
  },
  "dbt_output": {
    "artifacts_link": "string",
    "artifacts_headers": {
      "property1": "string",
      "property2": "string"
    }
  },
  "run_job_output": {
    "run_id": 0
  },
  "clean_rooms_notebook_output": {
    "clean_room_job_run_state": {
      "life_cycle_state": "RUN_LIFE_CYCLE_STATE_UNSPECIFIED",
      "result_state": "RUN_RESULT_STATE_UNSPECIFIED"
    },
    "notebook_output": {
      "result": "An arbitrary string passed by calling dbutils.notebook.exit(...)",
      "truncated": false
    },
    "output_schema_info": {
      "catalog_name": "string",
      "schema_name": "string",
      "expiration_time": 0
    }
  }
}
```

## GET /2.1/jobs/runs/list

List runs in descending order by start time.

### Query parameters

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#job_id) int64

Example`job_id=11223344`

The job for which to list runs. If omitted, the Jobs service lists runs from all jobs.

[`active_only`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#active_only) boolean

Example`active_only=false`

If active\_only is `true`, only active runs are included in the results; otherwise,
lists both active and completed runs. An active run is a run in the `QUEUED`, `PENDING`,
`RUNNING`, or `TERMINATING`. This field cannot be `true` when completed\_only is `true`.

[`completed_only`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#completed_only) boolean

Example`completed_only=false`

If completed\_only is `true`, only completed runs are included in the results;
otherwise, lists both active and completed runs. This field cannot be `true` when
active\_only is `true`.

[`offset`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#offset) int32

<= 10000

Deprecated

Example`offset=0`

The offset of the first run to return, relative to the most recent run.
Deprecated since June 2023. Use `page_token` to iterate through the pages instead.

[`limit`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#limit) int32

\[ 1 .. 25 \]

Default`20`

The number of runs to return. This value must be greater than 0 and less than 25.
The default value is 20. If a request specifies a limit of 0, the service instead
uses the maximum limit.

[`run_type`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#run_type) string

Enum: `JOB_RUN | WORKFLOW_RUN | SUBMIT_RUN`

Example`run_type=JOB_RUN`

The type of runs to return. For a description of run types, see [jobs/getrun](https://docs.databricks.com/api/azure/workspace/jobs/getrun).

[`expand_tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#expand_tasks) boolean

Default`false`

Whether to include task and cluster details in the response.

[`start_time_from`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#start_time_from) int64

Example`start_time_from=1642521600000`

Show runs that started _at or after_ this value. The value must be a UTC timestamp
in milliseconds. Can be combined with _start\_time\_to_ to filter by a time range.

[`start_time_to`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#start_time_to) int64

Example`start_time_to=1642608000000`

Show runs that started _at or before_ this value. The value must be a UTC timestamp
in milliseconds. Can be combined with _start\_time\_from_ to filter by a time range.

[`page_token`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#page_token) string

Example`page_token=CAEomPSriYcxMPWM_IiIxvEB`

Use `next_page_token` or `prev_page_token` returned from the previous request to list the next or previous page of runs respectively.

### Responses

**200** Request completed successfully.

Request completed successfully.

[`runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs) Array of object

A list of runs, from most recently started to least. Only included in the response if there are runs to list.

Array \[\
\
[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-job_id) int64\
\
Example`11223344`\
\
The canonical identifier of the job that contains this run.\
\
[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-run_id) int64\
\
Example`455644833`\
\
The canonical identifier of the run. This ID is unique across all runs of all jobs.\
\
[`creator_user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-creator_user_name) string\
\
Example`"user.name@databricks.com"`\
\
The creator user name. This field won’t be included in the response if the user has already been deleted.\
\
[`number_in_job`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-number_in_job) int64\
\
Deprecated\
\
Example`455644833`\
\
A unique identifier for this job run. This is set to the same value as `run_id`.\
\
[`original_attempt_run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-original_attempt_run_id) int64\
\
Example`455644833`\
\
If this run is a retry of a prior run attempt, this field contains the run\_id of the original attempt; otherwise, it is the same as the run\_id.\
\
[`state`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-state) object\
\
Deprecated\
\
Deprecated. Please use the `status` field instead.\
\
[`schedule`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-schedule) object\
\
The cron schedule that triggered this run if it was triggered by the periodic scheduler.\
\
[`cluster_spec`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-cluster_spec) object\
\
A snapshot of the job’s cluster specification when this run was created.\
\
[`cluster_instance`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-cluster_instance) object\
\
The cluster used for this run. If the run is specified to use a new cluster, this field is set once the Jobs service has requested a cluster for the run.\
\
[`job_parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-job_parameters) Array of object\
\
Job-level parameters used in the run\
\
[`overriding_parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-overriding_parameters) object\
\
The parameters used for this run.\
\
[`start_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-start_time) int64\
\
Example`1625060460483`\
\
The time at which this run was started in epoch milliseconds (milliseconds since 1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled to run on a new cluster, this is the time the cluster creation call is issued.\
\
[`setup_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-setup_duration) int64\
\
Example`0`\
\
The time in milliseconds it took to set up the cluster. For runs that run on new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very short. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `setup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.\
\
[`execution_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-execution_duration) int64\
\
Example`0`\
\
The time in milliseconds it took to execute the commands in the JAR or notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `execution_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.\
\
[`cleanup_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-cleanup_duration) int64\
\
Example`0`\
\
The time in milliseconds it took to terminate the cluster and clean up any associated artifacts. The duration of a task run is the sum of the `setup_duration`, `execution_duration`, and the `cleanup_duration`. The `cleanup_duration` field is set to 0 for multitask job runs. The total duration of a multitask job run is the value of the `run_duration` field.\
\
[`end_time`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-end_time) int64\
\
Example`1625060863413`\
\
The time at which this run ended in epoch milliseconds (milliseconds since 1/1/1970 UTC). This field is set to 0 if the job is still running.\
\
[`run_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-run_duration) int64\
\
Example`110183`\
\
The time in milliseconds it took the job run and all of its repairs to finish.\
\
[`queue_duration`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-queue_duration) int64\
\
Example`1625060863413`\
\
The time in milliseconds that the run has spent in the queue.\
\
[`trigger`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-trigger) string\
\
Enum: `PERIODIC | ONE_TIME | RETRY | RUN_JOB_TASK | FILE_ARRIVAL | TABLE`\
\
The type of trigger that fired this run.\
\
- `PERIODIC`: Schedules that periodically trigger runs, such as a cron scheduler.\
- `ONE_TIME`: One time triggers that fire a single run. This occurs you triggered a single run on demand through the UI or the API.\
- `RETRY`: Indicates a run that is triggered as a retry of a previously failed run. This occurs when you request to re-run the job in case of failures.\
- `RUN_JOB_TASK`: Indicates a run that is triggered using a Run Job task.\
- `FILE_ARRIVAL`: Indicates a run that is triggered by a file arrival.\
- `TABLE`: Indicates a run that is triggered by a table update.\
- `CONTINUOUS_RESTART`: Indicates a run created by user to manually restart a continuous job run.\
\
[`trigger_info`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-trigger_info) object\
\
Additional details about what triggered the run\
\
[`run_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-run_name) string\
\
<= 4096 characters\
\
Default`"Untitled"`\
\
Example`"A multitask job run"`\
\
An optional name for the run. The maximum length is 4096 bytes in UTF-8 encoding.\
\
[`run_page_url`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-run_page_url) string\
\
Example`"https://my-workspace.cloud.databricks.com/#job/11223344/run/123"`\
\
The URL to the detail page of the run.\
\
[`run_type`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-run_type) string\
\
Enum: `JOB_RUN | WORKFLOW_RUN | SUBMIT_RUN`\
\
The type of a run.\
\
- `JOB_RUN`: Normal job run. A run created with [jobs/runnow](https://docs.databricks.com/api/azure/workspace/jobs/runnow).\
- `WORKFLOW_RUN`: Workflow run. A run created with [dbutils.notebook.run](https://docs.databricks.com/dev-tools/databricks-utils.html#dbutils-workflow).\
- `SUBMIT_RUN`: Submit run. A run created with [jobs/submit](https://docs.databricks.com/api/azure/workspace/jobs/submit).\
\
[`tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-tasks) Array of object\
\
<= 100 items\
\
Example\
\
The list of tasks performed by the run. Each task has its own `run_id` which you can use to call `JobsGetOutput` to retrieve the run resutls.\
If more than 100 tasks are available, you can paginate through them using [jobs/getrun](https://docs.databricks.com/api/azure/workspace/jobs/getrun). Use the `next_page_token` field at the object root to determine if more results are available.\
\
[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-description) string\
\
Description of the run\
\
[`attempt_number`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-attempt_number) int32\
\
Example`0`\
\
The sequence number of this run attempt for a triggered job run. The initial attempt of a run has an attempt\_number of 0. If the initial run attempt fails, and the job has a retry policy (`max_retries` \> 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number` is the same as the `max_retries` value for the job.\
\
[`job_clusters`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-job_clusters) Array of object\
\
<= 100 items\
\
Example\
\
A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.\
If more than 100 job clusters are available, you can paginate through them using [jobs/getrun](https://docs.databricks.com/api/azure/workspace/jobs/getrun).\
\
[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-git_source) object\
\
Example\
\
An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.\
\
If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.\
\
Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.\
\
[`repair_history`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-repair_history) Array of object\
\
The repair history of the run.\
\
[`status`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-status) object\
\
The current status of the run\
\
[`job_run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#runs-job_run_id) int64\
\
ID of the job run that this run belongs to.\
For legacy and single-task job runs the field is populated with the job run ID.\
For task runs, the field is populated with the ID of the job run that the task run belongs to.\
\
\]

[`has_more`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#has_more) boolean

If true, additional runs matching the provided filter are available for listing.

[`next_page_token`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#next_page_token) string

Example`"CAEomPuciYcxMKbM9JvMlwU="`

A token that can be used to list the next page of runs (if applicable).

[`prev_page_token`](https://docs.databricks.com/api/azure/workspace/jobs_21/listruns#prev_page_token) string

Example`"CAAos-uriYcxMN7_rt_v7B4="`

A token that can be used to list the previous page of runs (if applicable).

This method might return the following HTTP codes: 400, 401, 403, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Response samples

200

```
{
  "runs": [\
    {\
      "job_id": 11223344,\
      "run_id": 455644833,\
      "creator_user_name": "user.name@databricks.com",\
      "number_in_job": 455644833,\
      "original_attempt_run_id": 455644833,\
      "state": {\
        "life_cycle_state": "PENDING",\
        "result_state": "SUCCESS",\
        "state_message": "string",\
        "user_cancelled_or_timedout": false,\
        "queue_reason": "Queued due to reaching maximum concurrent runs of 1."\
      },\
      "schedule": {\
        "quartz_cron_expression": "20 30 * * * ?",\
        "timezone_id": "Europe/London",\
        "pause_status": "UNPAUSED"\
      },\
      "cluster_spec": {\
        "existing_cluster_id": "0923-164208-meows279",\
        "new_cluster": {\
          "num_workers": 0,\
          "autoscale": {\
            "min_workers": 0,\
            "max_workers": 0\
          },\
          "kind": "CLASSIC_PREVIEW",\
          "cluster_name": "string",\
          "spark_version": "string",\
          "use_ml_runtime": true,\
          "is_single_node": true,\
          "spark_conf": {\
            "property1": "string",\
            "property2": "string"\
          },\
          "azure_attributes": {\
            "log_analytics_info": {\
              "log_analytics_workspace_id": "string",\
              "log_analytics_primary_key": "string"\
            },\
            "first_on_demand": "1",\
            "availability": "SPOT_AZURE",\
            "spot_bid_max_price": "-1.0"\
          },\
          "node_type_id": "string",\
          "driver_node_type_id": "string",\
          "ssh_public_keys": [\
            "string"\
          ],\
          "custom_tags": {\
            "property1": "string",\
            "property2": "string"\
          },\
          "cluster_log_conf": {\
            "dbfs": {\
              "destination": "string"\
            }\
          },\
          "init_scripts": [\
            {\
              "workspace": {\
                "destination": "string"\
              },\
              "volumes": {\
                "destination": "string"\
              },\
              "file": {\
                "destination": "string"\
              },\
              "dbfs": {\
                "destination": "string"\
              },\
              "abfss": {\
                "destination": "string"\
              },\
              "gcs": {\
                "destination": "string"\
              }\
            }\
          ],\
          "spark_env_vars": {\
            "property1": "string",\
            "property2": "string"\
          },\
          "autotermination_minutes": 0,\
          "enable_elastic_disk": true,\
          "instance_pool_id": "string",\
          "policy_id": "string",\
          "enable_local_disk_encryption": true,\
          "driver_instance_pool_id": "string",\
          "workload_type": {\
            "clients": {\
              "notebooks": "true",\
              "jobs": "true"\
            }\
          },\
          "runtime_engine": "NULL",\
          "docker_image": {\
            "url": "string",\
            "basic_auth": {\
              "username": "string",\
              "password": "string"\
            }\
          },\
          "data_security_mode": "DATA_SECURITY_MODE_AUTO",\
          "single_user_name": "string",\
          "apply_policy_default_values": false\
        },\
        "job_cluster_key": "string",\
        "libraries": [\
          {\
            "jar": "string",\
            "egg": "string",\
            "pypi": {\
              "package": "string",\
              "repo": "string"\
            },\
            "maven": {\
              "coordinates": "string",\
              "repo": "string",\
              "exclusions": [\
                "string"\
              ]\
            },\
            "cran": {\
              "package": "string",\
              "repo": "string"\
            },\
            "whl": "string",\
            "requirements": "string"\
          }\
        ]\
      },\
      "cluster_instance": {\
        "cluster_id": "0923-164208-meows279",\
        "spark_context_id": "string"\
      },\
      "job_parameters": [\
        {\
          "default": "users",\
          "name": "table",\
          "value": "customers"\
        }\
      ],\
      "overriding_parameters": {\
        "pipeline_params": {\
          "full_refresh": false\
        },\
        "jar_params": [\
          "john",\
          "doe",\
          "35"\
        ],\
        "notebook_params": {\
          "age": "35",\
          "name": "john doe"\
        },\
        "python_params": [\
          "john doe",\
          "35"\
        ],\
        "spark_submit_params": [\
          "--class",\
          "org.apache.spark.examples.SparkPi"\
        ],\
        "python_named_params": {\
          "data": "dbfs:/path/to/data.json",\
          "name": "task"\
        },\
        "sql_params": {\
          "age": "35",\
          "name": "john doe"\
        },\
        "dbt_commands": [\
          "dbt deps",\
          "dbt seed",\
          "dbt run"\
        ]\
      },\
      "start_time": 1625060460483,\
      "setup_duration": 0,\
      "execution_duration": 0,\
      "cleanup_duration": 0,\
      "end_time": 1625060863413,\
      "run_duration": 110183,\
      "queue_duration": 1625060863413,\
      "trigger": "PERIODIC",\
      "trigger_info": {\
        "run_id": 0\
      },\
      "run_name": "A multitask job run",\
      "run_page_url": "https://my-workspace.cloud.databricks.com/#job/11223344/run/123",\
      "run_type": "JOB_RUN",\
      "tasks": [\
        {\
          "setup_duration": 0,\
          "start_time": 1629989929660,\
          "task_key": "Orders_Ingest",\
          "state": {\
            "life_cycle_state": "INTERNAL_ERROR",\
            "result_state": "FAILED",\
            "state_message": "Library installation failed for library due to user error. Error messages:\n'Manage' permissions are required to install libraries on a cluster",\
            "user_cancelled_or_timedout": false\
          },\
          "description": "Ingests order data",\
          "job_cluster_key": "auto_scaling_cluster",\
          "end_time": 1629989930171,\
          "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/20",\
          "run_id": 2112892,\
          "cluster_instance": {\
            "cluster_id": "0923-164208-meows279",\
            "spark_context_id": "4348585301701786933"\
          },\
          "spark_jar_task": {\
            "main_class_name": "com.databricks.OrdersIngest"\
          },\
          "libraries": [\
            {\
              "jar": "dbfs:/mnt/databricks/OrderIngest.jar"\
            }\
          ],\
          "attempt_number": 0,\
          "cleanup_duration": 0,\
          "execution_duration": 0,\
          "run_if": "ALL_SUCCESS"\
        },\
        {\
          "setup_duration": 0,\
          "start_time": 0,\
          "task_key": "Match",\
          "state": {\
            "life_cycle_state": "SKIPPED",\
            "state_message": "An upstream task failed.",\
            "user_cancelled_or_timedout": false\
          },\
          "description": "Matches orders with user sessions",\
          "notebook_task": {\
            "notebook_path": "/Users/user.name@databricks.com/Match",\
            "source": "WORKSPACE"\
          },\
          "end_time": 1629989930238,\
          "depends_on": [\
            {\
              "task_key": "Orders_Ingest"\
            },\
            {\
              "task_key": "Sessionize"\
            }\
          ],\
          "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/21",\
          "new_cluster": {\
            "autoscale": {\
              "max_workers": 16,\
              "min_workers": 2\
            },\
            "node_type_id": null,\
            "spark_conf": {\
              "spark.speculation": true\
            },\
            "spark_version": "7.3.x-scala2.12"\
          },\
          "run_id": 2112897,\
          "cluster_instance": {\
            "cluster_id": "0923-164208-meows279"\
          },\
          "attempt_number": 0,\
          "cleanup_duration": 0,\
          "execution_duration": 0,\
          "run_if": "ALL_SUCCESS"\
        },\
        {\
          "setup_duration": 0,\
          "start_time": 1629989929668,\
          "task_key": "Sessionize",\
          "state": {\
            "life_cycle_state": "INTERNAL_ERROR",\
            "result_state": "FAILED",\
            "state_message": "Library installation failed for library due to user error. Error messages:\n'Manage' permissions are required to install libraries on a cluster",\
            "user_cancelled_or_timedout": false\
          },\
          "description": "Extracts session data from events",\
          "end_time": 1629989930144,\
          "run_page_url": "https://my-workspace.cloud.databricks.com/#job/39832/run/22",\
          "run_id": 2112902,\
          "cluster_instance": {\
            "cluster_id": "0923-164208-meows279",\
            "spark_context_id": "4348585301701786933"\
          },\
          "spark_jar_task": {\
            "main_class_name": "com.databricks.Sessionize"\
          },\
          "libraries": [\
            {\
              "jar": "dbfs:/mnt/databricks/Sessionize.jar"\
            }\
          ],\
          "attempt_number": 0,\
          "existing_cluster_id": "0923-164208-meows279",\
          "cleanup_duration": 0,\
          "execution_duration": 0,\
          "run_if": "ALL_SUCCESS"\
        }\
      ],\
      "description": "string",\
      "attempt_number": 0,\
      "job_clusters": [\
        {\
          "job_cluster_key": "auto_scaling_cluster",\
          "new_cluster": {\
            "autoscale": {\
              "max_workers": 16,\
              "min_workers": 2\
            },\
            "node_type_id": null,\
            "spark_conf": {\
              "spark.speculation": true\
            },\
            "spark_version": "7.3.x-scala2.12"\
          }\
        }\
      ],\
      "git_source": {\
        "git_branch": "main",\
        "git_provider": "gitHub",\
        "git_url": "https://github.com/databricks/databricks-cli"\
      },\
      "repair_history": [\
        {\
          "type": "ORIGINAL",\
          "start_time": 1625060460483,\
          "end_time": 1625060863413,\
          "state": {\
            "life_cycle_state": "PENDING",\
            "result_state": "SUCCESS",\
            "state_message": "string",\
            "user_cancelled_or_timedout": false,\
            "queue_reason": "Queued due to reaching maximum concurrent runs of 1."\
          },\
          "id": 734650698524280,\
          "task_run_ids": [\
            1106460542112844,\
            988297789683452\
          ],\
          "status": {\
            "state": "BLOCKED",\
            "termination_details": {\
              "code": "SUCCESS",\
              "type": "SUCCESS",\
              "message": "string"\
            },\
            "queue_details": {\
              "code": "ACTIVE_RUNS_LIMIT_REACHED",\
              "message": "string"\
            }\
          }\
        }\
      ],\
      "status": {\
        "state": "BLOCKED",\
        "termination_details": {\
          "code": "SUCCESS",\
          "type": "SUCCESS",\
          "message": "string"\
        },\
        "queue_details": {\
          "code": "ACTIVE_RUNS_LIMIT_REACHED",\
          "message": "string"\
        }\
      },\
      "job_run_id": 0\
    }\
  ],
  "has_more": true,
  "next_page_token": "CAEomPuciYcxMKbM9JvMlwU=",
  "prev_page_token": "CAAos-uriYcxMN7_rt_v7B4="
}
```

## POST /2.1/jobs/create

Create a new job.

### Request body

[`name`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#name) string

<= 4096 characters

Default`"Untitled"`

Example`"A multitask job"`

An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding.

[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#description) string

<= 27700 characters

Example`"This job contain multiple tasks that are required to produce the weekly shark sightings report."`

An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding.

[`email_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#email_notifications) object

Default`{}`

An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.

[`on_start`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#email_notifications-on_start) Array of string

A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent.

[`on_success`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#email_notifications-on_success) Array of string

A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a `TERMINATED``life_cycle_state` and a `SUCCESS` result\_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent.

[`on_failure`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#email_notifications-on_failure) Array of string

A list of email addresses to be notified when a run unsuccessfully completes. A run is considered to have completed unsuccessfully if it ends with an `INTERNAL_ERROR``life_cycle_state` or a `FAILED`, or `TIMED_OUT` result\_state. If this is not specified on job creation, reset, or update the list is empty, and notifications are not sent.

[`on_duration_warning_threshold_exceeded`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#email_notifications-on_duration_warning_threshold_exceeded) Array of string

A list of email addresses to be notified when the duration of a run exceeds the threshold specified for the `RUN_DURATION_SECONDS` metric in the `health` field. If no rule for the `RUN_DURATION_SECONDS` metric is specified in the `health` field for the job, notifications are not sent.

[`on_streaming_backlog_exceeded`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#email_notifications-on_streaming_backlog_exceeded) Array of string

Public preview

A list of email addresses to notify when any streaming backlog thresholds are exceeded for any stream.
Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`.
Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes.

[`no_alert_for_skipped_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#email_notifications-no_alert_for_skipped_runs) boolean

Deprecated

Default`false`

If true, do not send email to recipients specified in `on_failure` if the run is skipped.
This field is `deprecated`. Please use the `notification_settings.no_alert_for_skipped_runs` field.

[`webhook_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#webhook_notifications) object

Default`{}`

A collection of system notification IDs to notify when runs of this job begin or complete.

[`on_start`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#webhook_notifications-on_start) Array of object

An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the `on_start` property.

[`on_success`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#webhook_notifications-on_success) Array of object

An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success` property.

[`on_failure`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#webhook_notifications-on_failure) Array of object

An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property.

[`on_duration_warning_threshold_exceeded`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#webhook_notifications-on_duration_warning_threshold_exceeded) Array of object

An optional list of system notification IDs to call when the duration of a run exceeds the threshold specified for the `RUN_DURATION_SECONDS` metric in the `health` field. A maximum of 3 destinations can be specified for the `on_duration_warning_threshold_exceeded` property.

[`on_streaming_backlog_exceeded`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#webhook_notifications-on_streaming_backlog_exceeded) Array of object

Public preview

An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream.
Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`.
Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes.
A maximum of 3 destinations can be specified for the `on_streaming_backlog_exceeded` property.

[`notification_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#notification_settings) object

Default`{}`

Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this job.

[`no_alert_for_skipped_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#notification_settings-no_alert_for_skipped_runs) boolean

Default`false`

If true, do not send notifications to recipients specified in `on_failure` if the run is skipped.

[`no_alert_for_canceled_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#notification_settings-no_alert_for_canceled_runs) boolean

Default`false`

If true, do not send notifications to recipients specified in `on_failure` if the run is canceled.

[`alert_on_last_attempt`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#notification_settings-alert_on_last_attempt) boolean

Default`false`

If true, do not send notifications to recipients specified in `on_start` for the retried runs and do not send notifications to recipients specified in `on_failure` until the last retry of the run.

[`timeout_seconds`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#timeout_seconds) int32

Default`0`

Example`86400`

An optional timeout applied to each run of this job. A value of `0` means no timeout.

[`health`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#health) object

An optional set of health rules that can be defined for this job.

[`rules`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#health-rules) Array of object

[`max_retries`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#max_retries) int32

Default`0`

Example`10`

An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the `FAILED` result\_state or `INTERNAL_ERROR``life_cycle_state`. The value `-1` means to retry indefinitely and the value `0` means to never retry.

[`min_retry_interval_millis`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#min_retry_interval_millis) int32

Example`2000`

An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried.

[`retry_on_timeout`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#retry_on_timeout) boolean

Default`false`

Example`true`

An optional policy to specify whether to retry a job when it times out. The default behavior
is to not retry on timeout.

[`disable_auto_optimization`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#disable_auto_optimization) boolean

Default`false`

Example`true`

An option to disable auto optimization in serverless

[`schedule`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#schedule) object

An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.

[`quartz_cron_expression`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#schedule-quartz_cron_expression) requiredstring

Example`"20 30 * * * ?"`

A Cron expression using Quartz syntax that describes the schedule for a job. See [Cron Trigger](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) for details. This field is required.

[`timezone_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#schedule-timezone_id) requiredstring

Example`"Europe/London"`

A Java timezone ID. The schedule for a job is resolved with respect to this timezone. See [Java TimeZone](https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html) for details. This field is required.

[`pause_status`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#schedule-pause_status) string

Enum: `UNPAUSED | PAUSED`

Default`"UNPAUSED"`

Indicate whether this schedule is paused or not.

[`trigger`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#trigger) object

A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.

[`pause_status`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#trigger-pause_status) string

Enum: `UNPAUSED | PAUSED`

Default`"UNPAUSED"`

Whether this trigger is paused or not.

[`file_arrival`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#trigger-file_arrival) object

File arrival trigger settings.

[`periodic`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#trigger-periodic) object

Periodic trigger settings.

[`continuous`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#continuous) object

An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of `schedule` and `continuous` can be used.

[`pause_status`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#continuous-pause_status) string

Enum: `UNPAUSED | PAUSED`

Default`"UNPAUSED"`

Indicate whether the continuous execution of the job is paused or not. Defaults to UNPAUSED.

[`max_concurrent_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#max_concurrent_runs) int32

Default`1`

Example`10`

An optional maximum allowed number of concurrent runs of the job.
Set this value if you want to be able to execute multiple runs of the same job concurrently.
This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters.
This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs.
However, from then on, new runs are skipped unless there are fewer than 3 active runs.
This value cannot exceed 1000. Setting this value to `0` causes all new runs to be skipped.

[`tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks) Array of object

<= 100 items

Example

A list of task specifications to be executed by this job.
If more than 100 tasks are available, you can paginate through them using [jobs/get](https://docs.databricks.com/api/azure/workspace/jobs/get). Use the `next_page_token` field at the object root to determine if more results are available.

Array \[\
\
[`task_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-task_key) requiredstring\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
Example`"Task_Key"`\
\
A unique name for the task. This field is used to refer to this task from other tasks.\
This field is required and must be unique within its parent job.\
On Update or Reset, this field is used to reference the tasks to be updated or reset.\
\
[`depends_on`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-depends_on) Array of object\
\
Example\
\
An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete before executing this task. The task will run only if the `run_if` condition is true.\
The key is `task_key`, and the value is the name assigned to the dependent task.\
\
[`run_if`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-run_if) string\
\
Enum: `ALL_SUCCESS | ALL_DONE | NONE_FAILED | AT_LEAST_ONE_SUCCESS | ALL_FAILED | AT_LEAST_ONE_FAILED`\
\
Default`"ALL_SUCCESS"`\
\
An optional value specifying the condition determining whether the task is run once its dependencies have been completed.\
\
- `ALL_SUCCESS`: All dependencies have executed and succeeded\
- `AT_LEAST_ONE_SUCCESS`: At least one dependency has succeeded\
- `NONE_FAILED`: None of the dependencies have failed and at least one was executed\
- `ALL_DONE`: All dependencies have been completed\
- `AT_LEAST_ONE_FAILED`: At least one dependency failed\
- `ALL_FAILED`: ALl dependencies have failed\
\
[`notebook_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-notebook_task) object\
\
The task runs a notebook when the `notebook_task` field is present.\
\
[`spark_jar_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-spark_jar_task) object\
\
The task runs a JAR when the `spark_jar_task` field is present.\
\
[`spark_python_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-spark_python_task) object\
\
The task runs a Python file when the `spark_python_task` field is present.\
\
[`spark_submit_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-spark_submit_task) object\
\
(Legacy) The task runs the spark-submit script when the `spark_submit_task` field is present. This task can run only on new clusters and is not compatible with serverless compute.\
\
In the `new_cluster` specification, `libraries` and `spark_conf` are not supported. Instead, use `--jars` and `--py-files` to add Java and Python libraries and `--conf` to set the Spark configurations.\
\
`master`, `deploy-mode`, and `executor-cores` are automatically configured by Azure Databricks; you _cannot_ specify them in parameters.\
\
By default, the Spark submit job uses all available memory (excluding reserved memory for Azure Databricks services). You can set `--driver-memory`, and `--executor-memory` to a smaller value to leave some room for off-heap usage.\
\
The `--jars`, `--py-files`, `--files` arguments support DBFS and S3 paths.\
\
[`pipeline_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-pipeline_task) object\
\
The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported.\
\
[`python_wheel_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-python_wheel_task) object\
\
The task runs a Python wheel when the `python_wheel_task` field is present.\
\
[`dbt_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-dbt_task) object\
\
The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse.\
\
[`sql_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-sql_task) object\
\
The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present.\
\
[`run_job_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-run_job_task) object\
\
The task triggers another job when the `run_job_task` field is present.\
\
[`condition_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-condition_task) object\
\
The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present.\
The condition task does not require a cluster to execute and does not support retries or notifications.\
\
[`for_each_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-for_each_task) object\
\
The task executes a nested task for every input provided when the `for_each_task` field is present.\
\
[`clean_rooms_notebook_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-clean_rooms_notebook_task) object\
\
Public preview\
\
The task runs a [clean rooms](https://docs.databricks.com/en/clean-rooms/index.html) notebook\
when the `clean_rooms_notebook_task` field is present.\
\
[`existing_cluster_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-existing_cluster_id) string\
\
Example`"0923-164208-meows279"`\
\
If existing\_cluster\_id, the ID of an existing cluster that is used for all runs.\
When running jobs or tasks on an existing cluster, you may need to manually restart\
the cluster if it stops responding. We suggest running jobs and tasks on new clusters for\
greater reliability\
\
[`new_cluster`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-new_cluster) object\
\
If new\_cluster, a description of a new cluster that is created for each run.\
\
[`job_cluster_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-job_cluster_key) string\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
If job\_cluster\_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`.\
\
[`libraries`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-libraries) Array of object\
\
An optional list of libraries to be installed on the cluster.\
The default value is an empty list.\
\
[`max_retries`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-max_retries) int32\
\
Default`0`\
\
Example`10`\
\
An optional maximum number of times to retry an unsuccessful run. A run is considered to be unsuccessful if it completes with the `FAILED` result\_state or `INTERNAL_ERROR``life_cycle_state`. The value `-1` means to retry indefinitely and the value `0` means to never retry.\
\
[`min_retry_interval_millis`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-min_retry_interval_millis) int32\
\
Example`2000`\
\
An optional minimal interval in milliseconds between the start of the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately retried.\
\
[`retry_on_timeout`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-retry_on_timeout) boolean\
\
Default`false`\
\
Example`true`\
\
An optional policy to specify whether to retry a job when it times out. The default behavior\
is to not retry on timeout.\
\
[`disable_auto_optimization`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-disable_auto_optimization) boolean\
\
Default`false`\
\
Example`true`\
\
An option to disable auto optimization in serverless\
\
[`timeout_seconds`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-timeout_seconds) int32\
\
Default`0`\
\
Example`86400`\
\
An optional timeout applied to each run of this job task. A value of `0` means no timeout.\
\
[`health`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-health) object\
\
An optional set of health rules that can be defined for this job.\
\
[`email_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-email_notifications) object\
\
Default`{}`\
\
An optional set of email addresses that is notified when runs of this task begin or complete as well as when this task is deleted. The default behavior is to not send any emails.\
\
[`notification_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-notification_settings) object\
\
Default`{}`\
\
Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task.\
\
[`webhook_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-webhook_notifications) object\
\
Default`{}`\
\
A collection of system notification IDs to notify when runs of this task begin or complete. The default behavior is to not send any system notifications.\
\
[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-description) string\
\
<= 1000 characters\
\
Example`"This is the description for this task."`\
\
An optional description for this task.\
\
[`environment_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tasks-environment_key) string\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute.\
\
\]

[`job_clusters`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#job_clusters) Array of object

<= 100 items

Example

A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
If more than 100 job clusters are available, you can paginate through them using [jobs/get](https://docs.databricks.com/api/azure/workspace/jobs/get).

Array \[\
\
[`job_cluster_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#job_clusters-job_cluster_key) requiredstring\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
Example`"auto_scaling_cluster"`\
\
A unique name for the job cluster. This field is required and must be unique within the job.\
`JobTaskSettings` may refer to this field to determine which cluster to launch for the task execution.\
\
[`new_cluster`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#job_clusters-new_cluster) object\
\
If new\_cluster, a description of a cluster that is created for each task.\
\
\]

[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#git_source) object

Example

An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.

If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.

Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.

[`git_url`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#git_source-git_url) requiredstring

<= 300 characters

Example`"https://github.com/databricks/databricks-cli"`

URL of the repository to be cloned by this job.

[`git_provider`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#git_source-git_provider) requiredstring

Enum: `gitHub | bitbucketCloud | azureDevOpsServices | gitHubEnterprise | bitbucketServer | gitLab | gitLabEnterpriseEdition | awsCodeCommit`

Unique identifier of the service used to host the Git repository. The value is case insensitive.

[`git_branch`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#git_source-git_branch) string

<= 255 characters

Example`"main"`

Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git\_tag or git\_commit.

[`git_tag`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#git_source-git_tag) string

<= 255 characters

Example`"release-1.0.0"`

Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git\_branch or git\_commit.

[`git_commit`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#git_source-git_commit) string

<= 64 characters

Example`"e0056d01"`

Commit to be checked out and used by this job. This field cannot be specified in conjunction with git\_branch or git\_tag.

[`git_snapshot`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#git_source-git_snapshot) object

Read-only state of the remote repository at the time the job was run. This field is only included on job runs.

[`tags`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#tags) object

Default`{}`

Example

A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.

[`format`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#format) string

Deprecated

Enum: `SINGLE_TASK | MULTI_TASK`

Example`"MULTI_TASK"`

Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`.

[`queue`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#queue) object

The queue settings of the job.

[`enabled`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#queue-enabled) requiredboolean

Example`true`

If true, enable queueing for the job. This is a required field.

[`parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#parameters) Array of object

Job-level parameter definitions

Array \[\
\
[`name`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#parameters-name) requiredstring\
\
^\[\\w\\-.\]+$\
\
Example`"table"`\
\
The name of the defined parameter. May only contain alphanumeric characters, `_`, `-`, and `.`\
\
[`default`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#parameters-default) requiredstring\
\
Example`"users"`\
\
Default value of the parameter.\
\
\]

[`run_as`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#run_as) object

Write-only setting. Specifies the user or service principal that the job runs as. If not specified, the job runs as the user who created the job.

Either `user_name` or `service_principal_name` should be specified. If not, an error is thrown.

[`user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#run_as-user_name) string

Example`"user@databricks.com"`

The email of an active workspace user. Non-admin users can only set this field to their own email.

[`service_principal_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#run_as-service_principal_name) string

Example`"692bc6d0-ffa3-11ed-be56-0242ac120002"`

Application ID of an active service principal. Setting this field requires the `servicePrincipal/user` role.

[`edit_mode`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#edit_mode) string

Enum: `UI_LOCKED | EDITABLE`

Edit mode of the job.

- `UI_LOCKED`: The job is in a locked UI state and cannot be modified.
- `EDITABLE`: The job is in an editable state and can be modified.

[`deployment`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#deployment) object

Deployment information for jobs managed by external sources.

[`kind`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#deployment-kind) requiredstring

Enum: `BUNDLE`

The kind of deployment that manages the job.

- `BUNDLE`: The job is managed by Databricks Asset Bundle.

[`metadata_file_path`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#deployment-metadata_file_path) string

Path of the file that contains deployment metadata.

[`environments`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#environments) Array of object

<= 10 items

A list of task execution environment specifications that can be referenced by serverless tasks of this job.
An environment is required to be present for serverless tasks.
For serverless notebook tasks, the environment is accessible in the notebook environment panel.
For other serverless tasks, the task environment is required to be specified using environment\_key in the task settings.

Array \[\
\
[`environment_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#environments-environment_key) requiredstring\
\
The key of an environment. It has to be unique within a job.\
\
[`spec`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#environments-spec) object\
\
The environment entity used to preserve serverless environment side panel and jobs' environment for non-notebook task.\
In this minimal environment spec, only pip dependencies are supported.\
\
\]

[`access_control_list`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#access_control_list) Array of object

List of permissions to set on the job.

Array \[\
\
[`user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#access_control_list-user_name) string\
\
name of the user\
\
[`group_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#access_control_list-group_name) string\
\
name of the group\
\
[`service_principal_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#access_control_list-service_principal_name) string\
\
application ID of a service principal\
\
[`permission_level`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#access_control_list-permission_level) string\
\
Enum: `CAN_MANAGE | IS_OWNER | CAN_MANAGE_RUN | CAN_VIEW`\
\
Permission level\
\
\]

### Responses

**200** Request completed successfully.

Request completed successfully.

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/create#job_id) int64

Example`11223344`

The canonical identifier for the newly created job.

This method might return the following HTTP codes: 400, 401, 403, 404, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

404

FEATURE\_DISABLED

If a given user/entity is trying to use a feature which has been disabled.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Request samples

JSON

Shark predictor workflows

```
{
  "email_notifications": {
    "on_failure": [\
      "sharky@databricks.com"\
    ]
  },
  "format": "MULTI_TASK",
  "max_concurrent_runs": 1,
  "name": "Shark Predictor",
  "notification_settings": {
    "alert_on_last_attempt": false,
    "no_alert_for_canceled_runs": false,
    "no_alert_for_skipped_runs": false
  },
  "run_as": {
    "user_name": "sharky@databricks.com"
  },
  "tasks": [\
    {\
      "existing_cluster_id": "0914-084715-44dhyjfb",\
      "notebook_task": {\
        "notebook_path": "/Users/sharky@databricks.com/weather_ingest",\
        "source": "WORKSPACE"\
      },\
      "run_if": "ALL_SUCCESS",\
      "task_key": "weather_ocean_data"\
    },\
    {\
      "existing_cluster_id": "0914-084715-44dhyjfb",\
      "notebook_task": {\
        "notebook_path": "/Users/sharky@databricks.com/shark_sightings_scraper",\
        "source": "WORKSPACE"\
      },\
      "run_if": "ALL_SUCCESS",\
      "task_key": "shark_sightings"\
    },\
    {\
      "existing_cluster_id": "0914-084715-44dhyjfb",\
      "notebook_task": {\
        "notebook_path": "/Users/sharky@databricks.com/reef_data",\
        "source": "WORKSPACE"\
      },\
      "run_if": "ALL_SUCCESS",\
      "task_key": "reef_data"\
    },\
    {\
      "depends_on": [\
        {\
          "task_key": "reef_data"\
        },\
        {\
          "task_key": "shark_sightings"\
        },\
        {\
          "task_key": "weather_ocean_data"\
        }\
      ],\
      "pipeline_task": {\
        "pipeline_id": "1165597e-f650-4bf3-9a4f-fc2f2d40d2c3"\
      },\
      "run_if": "AT_LEAST_ONE_SUCCESS",\
      "task_key": "combine_shark_data"\
    },\
    {\
      "depends_on": [\
        {\
          "task_key": "combine_shark_data"\
        }\
      ],\
      "existing_cluster_id": "0914-084715-44dhyjfb",\
      "notebook_task": {\
        "notebook_path": "/Users/sharky@databricks.com/check_drift",\
        "source": "WORKSPACE"\
      },\
      "run_if": "ALL_SUCCESS",\
      "task_key": "check_drift"\
    },\
    {\
      "condition_task": {\
        "left": "{{tasks.check_drift.values.retrain}}",\
        "op": "EQUAL_TO",\
        "right": "true"\
      },\
      "depends_on": [\
        {\
          "task_key": "check_drift"\
        }\
      ],\
      "run_if": "ALL_SUCCESS",\
      "task_key": "if_drift_above_threshold"\
    },\
    {\
      "depends_on": [\
        {\
          "outcome": "true",\
          "task_key": "if_drift_above_threshold"\
        }\
      ],\
      "existing_cluster_id": "0914-084715-44dhyjfb",\
      "run_if": "ALL_SUCCESS",\
      "spark_python_task": {\
        "python_file": "/Users/sharky@databricks.com/retrain.py"\
      },\
      "task_key": "retrain_model"\
    },\
    {\
      "depends_on": [\
        {\
          "task_key": "retrain_model"\
        },\
        {\
          "outcome": "false",\
          "task_key": "if_drift_above_threshold"\
        }\
      ],\
      "run_if": "ALL_SUCCESS",\
      "sql_task": {\
        "dashboard": {\
          "dashboard_id": "0007ce2d-9d7d-48ca-b273-734c75080f58"\
        },\
        "warehouse_id": "791ba2a31c7fd70a"\
      },\
      "task_key": "refresh_shark_dashboard"\
    }\
  ],
  "webhook_notifications": {}
}
```

# Response samples

200

```
{
  "job_id": 11223344
}
```

## POST /2.1/jobs/reset

Overwrite all settings for the given job. Use the [_Update_ endpoint](https://docs.databricks.com/api/azure/workspace/jobs/update) to update job settings partially.

### Request body

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#job_id) requiredint64

Example`11223344`

The canonical identifier of the job to reset. This field is required.

[`new_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings) requiredobject

The new settings of the job. These settings completely replace the old settings.

Changes to the field `JobBaseSettings.timeout_seconds` are applied to active runs. Changes to other fields are applied to future runs only.

[`name`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-name) string

<= 4096 characters

Default`"Untitled"`

Example`"A multitask job"`

An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding.

[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-description) string

<= 27700 characters

Example`"This job contain multiple tasks that are required to produce the weekly shark sightings report."`

An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding.

[`email_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-email_notifications) object

Default`{}`

An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.

[`webhook_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-webhook_notifications) object

Default`{}`

A collection of system notification IDs to notify when runs of this job begin or complete.

[`notification_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-notification_settings) object

Default`{}`

Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this job.

[`timeout_seconds`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-timeout_seconds) int32

Default`0`

Example`86400`

An optional timeout applied to each run of this job. A value of `0` means no timeout.

[`health`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-health) object

An optional set of health rules that can be defined for this job.

[`schedule`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-schedule) object

An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.

[`trigger`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-trigger) object

A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.

[`continuous`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-continuous) object

An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of `schedule` and `continuous` can be used.

[`max_concurrent_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-max_concurrent_runs) int32

Default`1`

Example`10`

An optional maximum allowed number of concurrent runs of the job.
Set this value if you want to be able to execute multiple runs of the same job concurrently.
This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters.
This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs.
However, from then on, new runs are skipped unless there are fewer than 3 active runs.
This value cannot exceed 1000. Setting this value to `0` causes all new runs to be skipped.

[`tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-tasks) Array of object

<= 100 items

Example

A list of task specifications to be executed by this job.
If more than 100 tasks are available, you can paginate through them using [jobs/get](https://docs.databricks.com/api/azure/workspace/jobs/get). Use the `next_page_token` field at the object root to determine if more results are available.

[`job_clusters`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-job_clusters) Array of object

<= 100 items

Example

A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
If more than 100 job clusters are available, you can paginate through them using [jobs/get](https://docs.databricks.com/api/azure/workspace/jobs/get).

[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-git_source) object

Example

An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.

If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.

Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.

[`tags`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-tags) object

Default`{}`

Example

A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.

[`format`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-format) string

Deprecated

Enum: `SINGLE_TASK | MULTI_TASK`

Example`"MULTI_TASK"`

Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`.

[`queue`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-queue) object

The queue settings of the job.

[`parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-parameters) Array of object

Job-level parameter definitions

[`run_as`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-run_as) object

Write-only setting. Specifies the user or service principal that the job runs as. If not specified, the job runs as the user who created the job.

Either `user_name` or `service_principal_name` should be specified. If not, an error is thrown.

[`edit_mode`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-edit_mode) string

Enum: `UI_LOCKED | EDITABLE`

Edit mode of the job.

- `UI_LOCKED`: The job is in a locked UI state and cannot be modified.
- `EDITABLE`: The job is in an editable state and can be modified.

[`deployment`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-deployment) object

Deployment information for jobs managed by external sources.

[`environments`](https://docs.databricks.com/api/azure/workspace/jobs_21/reset#new_settings-environments) Array of object

<= 10 items

A list of task execution environment specifications that can be referenced by serverless tasks of this job.
An environment is required to be present for serverless tasks.
For serverless notebook tasks, the environment is accessible in the notebook environment panel.
For other serverless tasks, the task environment is required to be specified using environment\_key in the task settings.

### Responses

**200** Request completed successfully.

Request completed successfully.

This method might return the following HTTP codes: 400, 401, 403, 404, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

404

FEATURE\_DISABLED

If a given user/entity is trying to use a feature which has been disabled.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Request samples

JSON

```
{
  "job_id": 11223344,
  "new_settings": {
    "name": "A multitask job",
    "description": "This job contain multiple tasks that are required to produce the weekly shark sightings report.",
    "email_notifications": {
      "on_start": [\
        "user.name@databricks.com"\
      ],
      "on_success": [\
        "user.name@databricks.com"\
      ],
      "on_failure": [\
        "user.name@databricks.com"\
      ],
      "on_duration_warning_threshold_exceeded": [\
        "user.name@databricks.com"\
      ],
      "on_streaming_backlog_exceeded": [\
        "user.name@databricks.com"\
      ],
      "no_alert_for_skipped_runs": false
    },
    "webhook_notifications": {
      "on_start": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_success": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_failure": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_duration_warning_threshold_exceeded": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_streaming_backlog_exceeded": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ]
    },
    "notification_settings": {
      "no_alert_for_skipped_runs": false,
      "no_alert_for_canceled_runs": false,
      "alert_on_last_attempt": false
    },
    "timeout_seconds": 86400,
    "health": {
      "rules": [\
        {\
          "metric": "RUN_DURATION_SECONDS",\
          "op": "GREATER_THAN",\
          "value": 10\
        }\
      ]
    },
    "schedule": {
      "quartz_cron_expression": "20 30 * * * ?",
      "timezone_id": "Europe/London",
      "pause_status": "UNPAUSED"
    },
    "trigger": {
      "pause_status": "UNPAUSED",
      "file_arrival": {
        "url": "string",
        "min_time_between_triggers_seconds": 0,
        "wait_after_last_change_seconds": 0
      },
      "periodic": {
        "interval": 0,
        "unit": "HOURS"
      }
    },
    "continuous": {
      "pause_status": "UNPAUSED"
    },
    "max_concurrent_runs": 10,
    "tasks": [\
      {\
        "max_retries": 3,\
        "task_key": "Sessionize",\
        "description": "Extracts session data from events",\
        "min_retry_interval_millis": 2000,\
        "depends_on": [],\
        "timeout_seconds": 86400,\
        "spark_jar_task": {\
          "main_class_name": "com.databricks.Sessionize",\
          "parameters": [\
            "--data",\
            "dbfs:/path/to/data.json"\
          ]\
        },\
        "libraries": [\
          {\
            "jar": "dbfs:/mnt/databricks/Sessionize.jar"\
          }\
        ],\
        "retry_on_timeout": false,\
        "existing_cluster_id": "0923-164208-meows279"\
      },\
      {\
        "max_retries": 3,\
        "task_key": "Orders_Ingest",\
        "description": "Ingests order data",\
        "job_cluster_key": "auto_scaling_cluster",\
        "min_retry_interval_millis": 2000,\
        "depends_on": [],\
        "timeout_seconds": 86400,\
        "spark_jar_task": {\
          "main_class_name": "com.databricks.OrdersIngest",\
          "parameters": [\
            "--data",\
            "dbfs:/path/to/order-data.json"\
          ]\
        },\
        "libraries": [\
          {\
            "jar": "dbfs:/mnt/databricks/OrderIngest.jar"\
          }\
        ],\
        "retry_on_timeout": false\
      },\
      {\
        "max_retries": 3,\
        "task_key": "Match",\
        "description": "Matches orders with user sessions",\
        "notebook_task": {\
          "base_parameters": {\
            "age": "35",\
            "name": "John Doe"\
          },\
          "notebook_path": "/Users/user.name@databricks.com/Match"\
        },\
        "min_retry_interval_millis": 2000,\
        "depends_on": [\
          {\
            "task_key": "Orders_Ingest"\
          },\
          {\
            "task_key": "Sessionize"\
          }\
        ],\
        "new_cluster": {\
          "autoscale": {\
            "max_workers": 16,\
            "min_workers": 2\
          },\
          "node_type_id": null,\
          "spark_conf": {\
            "spark.speculation": true\
          },\
          "spark_version": "7.3.x-scala2.12"\
        },\
        "timeout_seconds": 86400,\
        "retry_on_timeout": false,\
        "run_if": "ALL_SUCCESS"\
      }\
    ],
    "job_clusters": [\
      {\
        "job_cluster_key": "auto_scaling_cluster",\
        "new_cluster": {\
          "autoscale": {\
            "max_workers": 16,\
            "min_workers": 2\
          },\
          "node_type_id": null,\
          "spark_conf": {\
            "spark.speculation": true\
          },\
          "spark_version": "7.3.x-scala2.12"\
        }\
      }\
    ],
    "git_source": {
      "git_branch": "main",
      "git_provider": "gitHub",
      "git_url": "https://github.com/databricks/databricks-cli"
    },
    "tags": {
      "cost-center": "engineering",
      "team": "jobs"
    },
    "format": "SINGLE_TASK",
    "queue": {
      "enabled": true
    },
    "parameters": [\
      {\
        "default": "users",\
        "name": "table"\
      }\
    ],
    "run_as": {
      "user_name": "user@databricks.com",
      "service_principal_name": "692bc6d0-ffa3-11ed-be56-0242ac120002"
    },
    "edit_mode": "UI_LOCKED",
    "deployment": {
      "kind": "BUNDLE",
      "metadata_file_path": "string"
    },
    "environments": [\
      {\
        "environment_key": "string",\
        "spec": {\
          "client": "1",\
          "dependencies": [\
            "string"\
          ]\
        }\
      }\
    ]
  }
}
```

# Response samples

200

```
{}
```

## POST /2.1/jobs/runs/cancel

Cancels a job run or a task run. The run is canceled asynchronously, so it may still be running when
this request completes.

### Request body

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/cancelrun#run_id) requiredint64

Example`455644833`

This field is required.

### Responses

**200** Request completed successfully.

Request completed successfully.

This method might return the following HTTP codes: 400, 401, 403, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Request samples

JSON

```
{
  "run_id": 455644833
}
```

# Response samples

200

```
{}
```

## POST /2.1/jobs/runs/cancel-all

Cancels all active runs of a job. The runs are canceled asynchronously, so it doesn't
prevent new runs from being started.

### Request body

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/cancelallruns#job_id) int64

Example`11223344`

The canonical identifier of the job to cancel all runs of.

[`all_queued_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/cancelallruns#all_queued_runs) boolean

Default`false`

Optional boolean parameter to cancel all queued runs. If no job\_id is provided, all queued runs in the workspace are canceled.

### Responses

**200** Request completed successfully.

Request completed successfully.

This method might return the following HTTP codes: 400, 401, 403, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Request samples

JSON

```
{
  "job_id": 11223344,
  "all_queued_runs": false
}
```

# Response samples

200

```
{}
```

[iframe](https://insight.adsrvr.org/track/up?adv=vg37y0i&ref=https%3A%2F%2Fdocs.databricks.com%2Fapi%2Fazure%2Fworkspace%2Fjobs_21%2Fcancelallruns&upid=u69d5s0&upv=1.1.0&paapi=1)

## POST /2.1/jobs/runs/delete

Deletes a non-active run. Returns an error if the run is active.

### Request body

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/deleterun#run_id) requiredint64

Example`455644833`

ID of the run to delete.

### Responses

**200** Request completed successfully.

Request completed successfully.

This method might return the following HTTP codes: 400, 401, 403, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Request samples

JSON

```
{
  "run_id": 455644833
}
```

# Response samples

200

```
{}
```

## POST /2.1/jobs/runs/repair

Re-run one or more tasks. Tasks are re-run as part of the original job run.
They use the current job and task settings, and can be viewed in the history for the
original job run.

### Request body

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#run_id) requiredint64

Example`455644833`

The job run ID of the run to repair. The run must not be in progress.

[`latest_repair_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#latest_repair_id) int64

Example`734650698524280`

The ID of the latest repair. This parameter is not required when repairing a run for the first time, but must be provided on subsequent requests to repair the same run.

[`rerun_tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#rerun_tasks) Array of string

Example

The task keys of the task runs to repair.

[`job_parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#job_parameters) object

Job-level parameters used in the run. for example `"param": "overriding_val"`

[`pipeline_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#pipeline_params) object

Controls whether the pipeline should perform a full refresh

[`full_refresh`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#pipeline_params-full_refresh) boolean

Default`false`

If true, triggers a full refresh on the delta live table.

[`jar_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#jar_params) Array of string

Deprecated

Example

A list of parameters for jobs with Spark JAR tasks, for example `"jar_params": ["john doe", "35"]`.
The parameters are used to invoke the main function of the main class specified in the Spark JAR task.
If not specified upon `run-now`, it defaults to an empty list.
jar\_params cannot be specified in conjunction with notebook\_params.
The JSON representation of this field (for example `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.

Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.

[`notebook_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#notebook_params) object

Deprecated

Example

A map from keys to values for jobs with notebook task, for example `"notebook_params": {"name": "john doe", "age": "35"}`.
The map is passed to the notebook and is accessible through the [dbutils.widgets.get](https://docs.databricks.com/dev-tools/databricks-utils.html) function.

If not specified upon `run-now`, the triggered run uses the job’s base parameters.

notebook\_params cannot be specified in conjunction with jar\_params.

Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.

The JSON representation of this field (for example `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot exceed 10,000 bytes.

[`python_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#python_params) Array of string

Deprecated

Example

A list of parameters for jobs with Python tasks, for example `"python_params": ["john doe", "35"]`.
The parameters are passed to Python file as command-line parameters. If specified upon `run-now`, it would overwrite
the parameters specified in job setting. The JSON representation of this field (for example `{"python_params":["john doe","35"]}`)
cannot exceed 10,000 bytes.

Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs.

Important

These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error.
Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis.

[`spark_submit_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#spark_submit_params) Array of string

Deprecated

Example

A list of parameters for jobs with spark submit task, for example `"spark_submit_params": ["--class", "org.apache.spark.examples.SparkPi"]`.
The parameters are passed to spark-submit script as command-line parameters. If specified upon `run-now`, it would overwrite the
parameters specified in job setting. The JSON representation of this field (for example `{"python_params":["john doe","35"]}`)
cannot exceed 10,000 bytes.

Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters containing information about job runs

Important

These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an error.
Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis.

[`python_named_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#python_named_params) object

Deprecated

Example

[`sql_params`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#sql_params) object

Deprecated

Example

A map from keys to values for jobs with SQL task, for example `"sql_params": {"name": "john doe", "age": "35"}`. The SQL alert task does not support custom parameters.

[`dbt_commands`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#dbt_commands) Array of string

Deprecated

Example

An array of commands to execute for jobs with the dbt task, for example `"dbt_commands": ["dbt deps", "dbt seed", "dbt deps", "dbt seed", "dbt run"]`

[`rerun_all_failed_tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#rerun_all_failed_tasks) boolean

Default`false`

If true, repair all failed tasks. Only one of `rerun_tasks` or `rerun_all_failed_tasks` can be used.

[`rerun_dependent_tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#rerun_dependent_tasks) boolean

Default`false`

If true, repair all tasks that depend on the tasks in `rerun_tasks`, even if they were previously successful. Can be also used in combination with `rerun_all_failed_tasks`.

### Responses

**200** Request completed successfully.

Request completed successfully.

[`repair_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/repairrun#repair_id) int64

Example`734650698524280`

The ID of the repair. Must be provided in subsequent repairs using the `latest_repair_id` field to ensure sequential repairs.

This method might return the following HTTP codes: 400, 401, 403, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Request samples

JSON

```
{
  "run_id": 455644833,
  "latest_repair_id": 734650698524280,
  "rerun_tasks": [\
    "task0",\
    "task1"\
  ],
  "job_parameters": {
    "property1": "string",
    "property2": "string"
  },
  "pipeline_params": {
    "full_refresh": false
  },
  "jar_params": [\
    "john",\
    "doe",\
    "35"\
  ],
  "notebook_params": {
    "age": "35",
    "name": "john doe"
  },
  "python_params": [\
    "john doe",\
    "35"\
  ],
  "spark_submit_params": [\
    "--class",\
    "org.apache.spark.examples.SparkPi"\
  ],
  "python_named_params": {
    "data": "dbfs:/path/to/data.json",
    "name": "task"
  },
  "sql_params": {
    "age": "35",
    "name": "john doe"
  },
  "dbt_commands": [\
    "dbt deps",\
    "dbt seed",\
    "dbt run"\
  ],
  "rerun_all_failed_tasks": false,
  "rerun_dependent_tasks": false
}
```

# Response samples

200

```
{
  "repair_id": 734650698524280
}
```

## POST /2.1/jobs/runs/submit

Submit a one-time run. This endpoint allows you to submit a workload directly
without creating a job. Runs submitted using this endpoint don’t display in
the UI. Use the `jobs/runs/get` API to check the run state after the job is
submitted.

### Request body

[`run_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#run_name) string

Default`"Untitled"`

Example`"A multitask job run"`

An optional name for the run. The default value is `Untitled`.

[`timeout_seconds`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#timeout_seconds) int32

Default`0`

Example`86400`

An optional timeout applied to each run of this job. A value of `0` means no timeout.

[`health`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#health) object

An optional set of health rules that can be defined for this job.

[`rules`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#health-rules) Array of object

[`idempotency_token`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#idempotency_token) string

Example`"8f018174-4792-40d5-bcbc-3e6a527352c8"`

An optional token that can be used to guarantee the idempotency of job run requests. If a run with the provided token already exists,
the request does not create a new run but returns the ID of the existing run instead. If a run with the provided token is deleted,
an error is returned.

If you specify the idempotency token, upon failure you can retry until the request succeeds. Azure Databricks guarantees that exactly
one run is launched with that idempotency token.

This token must have at most 64 characters.

For more information, see [How to ensure idempotency for jobs](https://kb.databricks.com/jobs/jobs-idempotency.html).

[`tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks) Array of object

<= 100 items

Example

Array \[\
\
[`task_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-task_key) requiredstring\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
Example`"Task_Key"`\
\
A unique name for the task. This field is used to refer to this task from other tasks.\
This field is required and must be unique within its parent job.\
On Update or Reset, this field is used to reference the tasks to be updated or reset.\
\
[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-description) string\
\
<= 1000 characters\
\
Example`"This is the description for this task."`\
\
An optional description for this task.\
\
[`depends_on`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-depends_on) Array of object\
\
Example\
\
An optional array of objects specifying the dependency graph of the task. All tasks specified in this field must complete successfully before executing this task.\
The key is `task_key`, and the value is the name assigned to the dependent task.\
\
[`run_if`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-run_if) string\
\
Enum: `ALL_SUCCESS | ALL_DONE | NONE_FAILED | AT_LEAST_ONE_SUCCESS | ALL_FAILED | AT_LEAST_ONE_FAILED`\
\
Example`"ALL_SUCCESS"`\
\
An optional value indicating the condition that determines whether the task should be run once its dependencies have been completed. When omitted, defaults to `ALL_SUCCESS`. See [jobs/create](https://docs.databricks.com/api/azure/workspace/jobs/create) for a list of possible values.\
\
[`notebook_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-notebook_task) object\
\
The task runs a notebook when the `notebook_task` field is present.\
\
[`spark_jar_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-spark_jar_task) object\
\
The task runs a JAR when the `spark_jar_task` field is present.\
\
[`spark_python_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-spark_python_task) object\
\
The task runs a Python file when the `spark_python_task` field is present.\
\
[`spark_submit_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-spark_submit_task) object\
\
(Legacy) The task runs the spark-submit script when the `spark_submit_task` field is present. This task can run only on new clusters and is not compatible with serverless compute.\
\
In the `new_cluster` specification, `libraries` and `spark_conf` are not supported. Instead, use `--jars` and `--py-files` to add Java and Python libraries and `--conf` to set the Spark configurations.\
\
`master`, `deploy-mode`, and `executor-cores` are automatically configured by Azure Databricks; you _cannot_ specify them in parameters.\
\
By default, the Spark submit job uses all available memory (excluding reserved memory for Azure Databricks services). You can set `--driver-memory`, and `--executor-memory` to a smaller value to leave some room for off-heap usage.\
\
The `--jars`, `--py-files`, `--files` arguments support DBFS and S3 paths.\
\
[`pipeline_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-pipeline_task) object\
\
The task triggers a pipeline update when the `pipeline_task` field is present. Only pipelines configured to use triggered more are supported.\
\
[`python_wheel_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-python_wheel_task) object\
\
The task runs a Python wheel when the `python_wheel_task` field is present.\
\
[`dbt_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-dbt_task) object\
\
The task runs one or more dbt commands when the `dbt_task` field is present. The dbt task requires both Databricks SQL and the ability to use a serverless or a pro SQL warehouse.\
\
[`sql_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-sql_task) object\
\
The task runs a SQL query or file, or it refreshes a SQL alert or a legacy SQL dashboard when the `sql_task` field is present.\
\
[`run_job_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-run_job_task) object\
\
The task triggers another job when the `run_job_task` field is present.\
\
[`condition_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-condition_task) object\
\
The task evaluates a condition that can be used to control the execution of other tasks when the `condition_task` field is present.\
The condition task does not require a cluster to execute and does not support retries or notifications.\
\
[`for_each_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-for_each_task) object\
\
The task executes a nested task for every input provided when the `for_each_task` field is present.\
\
[`clean_rooms_notebook_task`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-clean_rooms_notebook_task) object\
\
Public preview\
\
The task runs a [clean rooms](https://docs.databricks.com/en/clean-rooms/index.html) notebook\
when the `clean_rooms_notebook_task` field is present.\
\
[`existing_cluster_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-existing_cluster_id) string\
\
Example`"0923-164208-meows279"`\
\
If existing\_cluster\_id, the ID of an existing cluster that is used for all runs.\
When running jobs or tasks on an existing cluster, you may need to manually restart\
the cluster if it stops responding. We suggest running jobs and tasks on new clusters for\
greater reliability\
\
[`new_cluster`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-new_cluster) object\
\
If new\_cluster, a description of a new cluster that is created for each run.\
\
[`job_cluster_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-job_cluster_key) string\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
If job\_cluster\_key, this task is executed reusing the cluster specified in `job.settings.job_clusters`.\
\
[`libraries`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-libraries) Array of object\
\
An optional list of libraries to be installed on the cluster.\
The default value is an empty list.\
\
[`timeout_seconds`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-timeout_seconds) int32\
\
Default`0`\
\
Example`86400`\
\
An optional timeout applied to each run of this job task. A value of `0` means no timeout.\
\
[`email_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-email_notifications) object\
\
Default`{}`\
\
An optional set of email addresses notified when the task run begins or completes. The default behavior is to not send any emails.\
\
[`health`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-health) object\
\
An optional set of health rules that can be defined for this job.\
\
[`notification_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-notification_settings) object\
\
Default`{}`\
\
Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this task run.\
\
[`webhook_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-webhook_notifications) object\
\
Default`{}`\
\
A collection of system notification IDs to notify when the run begins or completes. The default behavior is to not send any system notifications. Task webhooks respect the task notification settings.\
\
[`environment_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#tasks-environment_key) string\
\
\[ 1 .. 100 \] characters ^\[\\w\\-\\\_\]+$\
\
The key that references an environment spec in a job. This field is required for Python script, Python wheel and dbt tasks when using serverless compute.\
\
\]

[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#git_source) object

Example

An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.

If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.

Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.

[`git_url`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#git_source-git_url) requiredstring

<= 300 characters

Example`"https://github.com/databricks/databricks-cli"`

URL of the repository to be cloned by this job.

[`git_provider`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#git_source-git_provider) requiredstring

Enum: `gitHub | bitbucketCloud | azureDevOpsServices | gitHubEnterprise | bitbucketServer | gitLab | gitLabEnterpriseEdition | awsCodeCommit`

Unique identifier of the service used to host the Git repository. The value is case insensitive.

[`git_branch`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#git_source-git_branch) string

<= 255 characters

Example`"main"`

Name of the branch to be checked out and used by this job. This field cannot be specified in conjunction with git\_tag or git\_commit.

[`git_tag`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#git_source-git_tag) string

<= 255 characters

Example`"release-1.0.0"`

Name of the tag to be checked out and used by this job. This field cannot be specified in conjunction with git\_branch or git\_commit.

[`git_commit`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#git_source-git_commit) string

<= 64 characters

Example`"e0056d01"`

Commit to be checked out and used by this job. This field cannot be specified in conjunction with git\_branch or git\_tag.

[`git_snapshot`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#git_source-git_snapshot) object

Read-only state of the remote repository at the time the job was run. This field is only included on job runs.

[`webhook_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#webhook_notifications) object

Default`{}`

A collection of system notification IDs to notify when the run begins or completes.

[`on_start`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#webhook_notifications-on_start) Array of object

An optional list of system notification IDs to call when the run starts. A maximum of 3 destinations can be specified for the `on_start` property.

[`on_success`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#webhook_notifications-on_success) Array of object

An optional list of system notification IDs to call when the run completes successfully. A maximum of 3 destinations can be specified for the `on_success` property.

[`on_failure`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#webhook_notifications-on_failure) Array of object

An optional list of system notification IDs to call when the run fails. A maximum of 3 destinations can be specified for the `on_failure` property.

[`on_duration_warning_threshold_exceeded`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#webhook_notifications-on_duration_warning_threshold_exceeded) Array of object

An optional list of system notification IDs to call when the duration of a run exceeds the threshold specified for the `RUN_DURATION_SECONDS` metric in the `health` field. A maximum of 3 destinations can be specified for the `on_duration_warning_threshold_exceeded` property.

[`on_streaming_backlog_exceeded`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#webhook_notifications-on_streaming_backlog_exceeded) Array of object

Public preview

An optional list of system notification IDs to call when any streaming backlog thresholds are exceeded for any stream.
Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`.
Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes.
A maximum of 3 destinations can be specified for the `on_streaming_backlog_exceeded` property.

[`email_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#email_notifications) object

Default`{}`

An optional set of email addresses notified when the run begins or completes.

[`on_start`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#email_notifications-on_start) Array of string

A list of email addresses to be notified when a run begins. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent.

[`on_success`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#email_notifications-on_success) Array of string

A list of email addresses to be notified when a run successfully completes. A run is considered to have completed successfully if it ends with a `TERMINATED``life_cycle_state` and a `SUCCESS` result\_state. If not specified on job creation, reset, or update, the list is empty, and notifications are not sent.

[`on_failure`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#email_notifications-on_failure) Array of string

A list of email addresses to be notified when a run unsuccessfully completes. A run is considered to have completed unsuccessfully if it ends with an `INTERNAL_ERROR``life_cycle_state` or a `FAILED`, or `TIMED_OUT` result\_state. If this is not specified on job creation, reset, or update the list is empty, and notifications are not sent.

[`on_duration_warning_threshold_exceeded`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#email_notifications-on_duration_warning_threshold_exceeded) Array of string

A list of email addresses to be notified when the duration of a run exceeds the threshold specified for the `RUN_DURATION_SECONDS` metric in the `health` field. If no rule for the `RUN_DURATION_SECONDS` metric is specified in the `health` field for the job, notifications are not sent.

[`on_streaming_backlog_exceeded`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#email_notifications-on_streaming_backlog_exceeded) Array of string

Public preview

A list of email addresses to notify when any streaming backlog thresholds are exceeded for any stream.
Streaming backlog thresholds can be set in the `health` field using the following metrics: `STREAMING_BACKLOG_BYTES`, `STREAMING_BACKLOG_RECORDS`, `STREAMING_BACKLOG_SECONDS`, or `STREAMING_BACKLOG_FILES`.
Alerting is based on the 10-minute average of these metrics. If the issue persists, notifications are resent every 30 minutes.

[`no_alert_for_skipped_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#email_notifications-no_alert_for_skipped_runs) boolean

Deprecated

Default`false`

If true, do not send email to recipients specified in `on_failure` if the run is skipped.
This field is `deprecated`. Please use the `notification_settings.no_alert_for_skipped_runs` field.

[`notification_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#notification_settings) object

Default`{}`

Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this run.

[`no_alert_for_skipped_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#notification_settings-no_alert_for_skipped_runs) boolean

Default`false`

If true, do not send notifications to recipients specified in `on_failure` if the run is skipped.

[`no_alert_for_canceled_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#notification_settings-no_alert_for_canceled_runs) boolean

Default`false`

If true, do not send notifications to recipients specified in `on_failure` if the run is canceled.

[`alert_on_last_attempt`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#notification_settings-alert_on_last_attempt) boolean

Default`false`

If true, do not send notifications to recipients specified in `on_start` for the retried runs and do not send notifications to recipients specified in `on_failure` until the last retry of the run.

[`environments`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#environments) Array of object

<= 10 items

A list of task execution environment specifications that can be referenced by tasks of this run.

Array \[\
\
[`environment_key`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#environments-environment_key) requiredstring\
\
The key of an environment. It has to be unique within a job.\
\
[`spec`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#environments-spec) object\
\
The environment entity used to preserve serverless environment side panel and jobs' environment for non-notebook task.\
In this minimal environment spec, only pip dependencies are supported.\
\
\]

[`access_control_list`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#access_control_list) Array of object

List of permissions to set on the job.

Array \[\
\
[`user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#access_control_list-user_name) string\
\
name of the user\
\
[`group_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#access_control_list-group_name) string\
\
name of the group\
\
[`service_principal_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#access_control_list-service_principal_name) string\
\
application ID of a service principal\
\
[`permission_level`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#access_control_list-permission_level) string\
\
Enum: `CAN_MANAGE | IS_OWNER | CAN_MANAGE_RUN | CAN_VIEW`\
\
Permission level\
\
\]

[`queue`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#queue) object

The queue settings of the one-time run.

[`enabled`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#queue-enabled) requiredboolean

Example`true`

If true, enable queueing for the job. This is a required field.

[`run_as`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#run_as) object

Specifies the user or service principal that the job runs as. If not specified, the job runs as the user who submits the request.

[`user_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#run_as-user_name) string

Example`"user@databricks.com"`

The email of an active workspace user. Non-admin users can only set this field to their own email.

[`service_principal_name`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#run_as-service_principal_name) string

Example`"692bc6d0-ffa3-11ed-be56-0242ac120002"`

Application ID of an active service principal. Setting this field requires the `servicePrincipal/user` role.

### Responses

**200** Request completed successfully.

Request completed successfully.

[`run_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/submit#run_id) int64

Example`455644833`

The canonical identifier for the newly submitted run.

This method might return the following HTTP codes: 400, 401, 403, 404, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

404

FEATURE\_DISABLED

If a given user/entity is trying to use a feature which has been disabled.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Request samples

JSON

```
{
  "run_name": "A multitask job run",
  "timeout_seconds": 86400,
  "health": {
    "rules": [\
      {\
        "metric": "RUN_DURATION_SECONDS",\
        "op": "GREATER_THAN",\
        "value": 10\
      }\
    ]
  },
  "idempotency_token": "8f018174-4792-40d5-bcbc-3e6a527352c8",
  "tasks": [\
    {\
      "task_key": "Sessionize",\
      "description": "Extracts session data from events",\
      "min_retry_interval_millis": 2000,\
      "depends_on": [],\
      "timeout_seconds": 86400,\
      "spark_jar_task": {\
        "main_class_name": "com.databricks.Sessionize",\
        "parameters": [\
          "--data",\
          "dbfs:/path/to/data.json"\
        ]\
      },\
      "libraries": [\
        {\
          "jar": "dbfs:/mnt/databricks/Sessionize.jar"\
        }\
      ],\
      "retry_on_timeout": false,\
      "existing_cluster_id": "0923-164208-meows279"\
    },\
    {\
      "task_key": "Orders_Ingest",\
      "description": "Ingests order data",\
      "depends_on": [],\
      "timeout_seconds": 86400,\
      "spark_jar_task": {\
        "main_class_name": "com.databricks.OrdersIngest",\
        "parameters": [\
          "--data",\
          "dbfs:/path/to/order-data.json"\
        ]\
      },\
      "libraries": [\
        {\
          "jar": "dbfs:/mnt/databricks/OrderIngest.jar"\
        }\
      ],\
      "existing_cluster_id": "0923-164208-meows279"\
    },\
    {\
      "task_key": "Match",\
      "description": "Matches orders with user sessions",\
      "notebook_task": {\
        "base_parameters": {\
          "age": "35",\
          "name": "John Doe"\
        },\
        "notebook_path": "/Users/user.name@databricks.com/Match"\
      },\
      "depends_on": [\
        {\
          "task_key": "Orders_Ingest"\
        },\
        {\
          "task_key": "Sessionize"\
        }\
      ],\
      "new_cluster": {\
        "autoscale": {\
          "max_workers": 16,\
          "min_workers": 2\
        },\
        "node_type_id": null,\
        "spark_conf": {\
          "spark.speculation": true\
        },\
        "spark_version": "7.3.x-scala2.12"\
      },\
      "timeout_seconds": 86400,\
      "retry_on_timeout": false,\
      "run_if": "ALL_SUCCESS"\
    }\
  ],
  "git_source": {
    "git_branch": "main",
    "git_provider": "gitHub",
    "git_url": "https://github.com/databricks/databricks-cli"
  },
  "webhook_notifications": {
    "on_start": [\
      [\
        {\
          "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
        }\
      ]\
    ],
    "on_success": [\
      [\
        {\
          "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
        }\
      ]\
    ],
    "on_failure": [\
      [\
        {\
          "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
        }\
      ]\
    ],
    "on_duration_warning_threshold_exceeded": [\
      [\
        {\
          "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
        }\
      ]\
    ],
    "on_streaming_backlog_exceeded": [\
      [\
        {\
          "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
        }\
      ]\
    ]
  },
  "email_notifications": {
    "on_start": [\
      "user.name@databricks.com"\
    ],
    "on_success": [\
      "user.name@databricks.com"\
    ],
    "on_failure": [\
      "user.name@databricks.com"\
    ],
    "on_duration_warning_threshold_exceeded": [\
      "user.name@databricks.com"\
    ],
    "on_streaming_backlog_exceeded": [\
      "user.name@databricks.com"\
    ],
    "no_alert_for_skipped_runs": false
  },
  "notification_settings": {
    "no_alert_for_skipped_runs": false,
    "no_alert_for_canceled_runs": false,
    "alert_on_last_attempt": false
  },
  "environments": [\
    {\
      "environment_key": "string",\
      "spec": {\
        "client": "1",\
        "dependencies": [\
          "string"\
        ]\
      }\
    }\
  ],
  "access_control_list": [\
    {\
      "user_name": "string",\
      "group_name": "string",\
      "service_principal_name": "string",\
      "permission_level": "CAN_MANAGE"\
    }\
  ],
  "queue": {
    "enabled": true
  },
  "run_as": {
    "user_name": "user@databricks.com",
    "service_principal_name": "692bc6d0-ffa3-11ed-be56-0242ac120002"
  }
}
```

# Response samples

200

```
{
  "run_id": 455644833
}
```

## POST /2.1/jobs/update

Add, update, or remove specific settings of an existing job. Use the [_Reset_ endpoint](https://docs.databricks.com/api/azure/workspace/jobs/reset) to overwrite all job settings.

### Request body

[`job_id`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#job_id) requiredint64

Example`11223344`

The canonical identifier of the job to update. This field is required.

[`new_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings) object

The new settings for the job.

Top-level fields specified in `new_settings` are completely replaced, except for arrays which are merged. That is, new and existing entries are completely replaced based on the respective key fields, i.e. `task_key` or `job_cluster_key`, while previous entries are kept.

Partially updating nested fields is not supported.

Changes to the field `JobSettings.timeout_seconds` are applied to active runs. Changes to other fields are applied to future runs only.

[`name`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-name) string

<= 4096 characters

Default`"Untitled"`

Example`"A multitask job"`

An optional name for the job. The maximum length is 4096 bytes in UTF-8 encoding.

[`description`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-description) string

<= 27700 characters

Example`"This job contain multiple tasks that are required to produce the weekly shark sightings report."`

An optional description for the job. The maximum length is 27700 characters in UTF-8 encoding.

[`email_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-email_notifications) object

Default`{}`

An optional set of email addresses that is notified when runs of this job begin or complete as well as when this job is deleted.

[`webhook_notifications`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-webhook_notifications) object

Default`{}`

A collection of system notification IDs to notify when runs of this job begin or complete.

[`notification_settings`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-notification_settings) object

Default`{}`

Optional notification settings that are used when sending notifications to each of the `email_notifications` and `webhook_notifications` for this job.

[`timeout_seconds`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-timeout_seconds) int32

Default`0`

Example`86400`

An optional timeout applied to each run of this job. A value of `0` means no timeout.

[`health`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-health) object

An optional set of health rules that can be defined for this job.

[`schedule`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-schedule) object

An optional periodic schedule for this job. The default behavior is that the job only runs when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.

[`trigger`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-trigger) object

A configuration to trigger a run when certain conditions are met. The default behavior is that the job runs only when triggered by clicking “Run Now” in the Jobs UI or sending an API request to `runNow`.

[`continuous`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-continuous) object

An optional continuous property for this job. The continuous property will ensure that there is always one run executing. Only one of `schedule` and `continuous` can be used.

[`max_concurrent_runs`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-max_concurrent_runs) int32

Default`1`

Example`10`

An optional maximum allowed number of concurrent runs of the job.
Set this value if you want to be able to execute multiple runs of the same job concurrently.
This is useful for example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each other, or if you want to trigger multiple runs which differ by their input parameters.
This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent active runs. Then setting the concurrency to 3 won’t kill any of the active runs.
However, from then on, new runs are skipped unless there are fewer than 3 active runs.
This value cannot exceed 1000. Setting this value to `0` causes all new runs to be skipped.

[`tasks`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-tasks) Array of object

<= 100 items

Example

A list of task specifications to be executed by this job.
If more than 100 tasks are available, you can paginate through them using [jobs/get](https://docs.databricks.com/api/azure/workspace/jobs/get). Use the `next_page_token` field at the object root to determine if more results are available.

[`job_clusters`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-job_clusters) Array of object

<= 100 items

Example

A list of job cluster specifications that can be shared and reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent libraries in task settings.
If more than 100 job clusters are available, you can paginate through them using [jobs/get](https://docs.databricks.com/api/azure/workspace/jobs/get).

[`git_source`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-git_source) object

Example

An optional specification for a remote Git repository containing the source code used by tasks. Version-controlled source code is supported by notebook, dbt, Python script, and SQL File tasks.

If `git_source` is set, these tasks retrieve the file from the remote repository by default. However, this behavior can be overridden by setting `source` to `WORKSPACE` on the task.

Note: dbt and SQL File tasks support only version-controlled sources. If dbt or SQL File tasks are used, `git_source` must be defined on the job.

[`tags`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-tags) object

Default`{}`

Example

A map of tags associated with the job. These are forwarded to the cluster as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags can be added to the job.

[`format`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-format) string

Deprecated

Enum: `SINGLE_TASK | MULTI_TASK`

Example`"MULTI_TASK"`

Used to tell what is the format of the job. This field is ignored in Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`.

[`queue`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-queue) object

The queue settings of the job.

[`parameters`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-parameters) Array of object

Job-level parameter definitions

[`run_as`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-run_as) object

Write-only setting. Specifies the user or service principal that the job runs as. If not specified, the job runs as the user who created the job.

Either `user_name` or `service_principal_name` should be specified. If not, an error is thrown.

[`edit_mode`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-edit_mode) string

Enum: `UI_LOCKED | EDITABLE`

Edit mode of the job.

- `UI_LOCKED`: The job is in a locked UI state and cannot be modified.
- `EDITABLE`: The job is in an editable state and can be modified.

[`deployment`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-deployment) object

Deployment information for jobs managed by external sources.

[`environments`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#new_settings-environments) Array of object

<= 10 items

A list of task execution environment specifications that can be referenced by serverless tasks of this job.
An environment is required to be present for serverless tasks.
For serverless notebook tasks, the environment is accessible in the notebook environment panel.
For other serverless tasks, the task environment is required to be specified using environment\_key in the task settings.

[`fields_to_remove`](https://docs.databricks.com/api/azure/workspace/jobs_21/update#fields_to_remove) Array of string

Example

Remove top-level fields in the job settings. Removing nested fields is not supported, except for tasks and job clusters (`tasks/task_1`). This field is optional.

### Responses

**200** Request completed successfully.

Request completed successfully.

This method might return the following HTTP codes: 400, 401, 403, 404, 429, 500

Error responses are returned in the following format:

```
{
  "error_code": "Error code",
  "message": "Human-readable error message."
}
```

# Possible error codes:

HTTP code

error\_code

Description

400

INVALID\_PARAMETER\_VALUE

Supplied value for a parameter was invalid.

401

UNAUTHORIZED

The request does not have valid authentication credentials for the operation.

403

PERMISSION\_DENIED

Caller does not have permission to execute the specified operation.

404

FEATURE\_DISABLED

If a given user/entity is trying to use a feature which has been disabled.

429

REQUEST\_LIMIT\_EXCEEDED

Request is rejected due to throttling.

500

INTERNAL\_SERVER\_ERROR

Internal error.

# Request samples

JSON

```
{
  "job_id": 11223344,
  "new_settings": {
    "name": "A multitask job",
    "description": "This job contain multiple tasks that are required to produce the weekly shark sightings report.",
    "email_notifications": {
      "on_start": [\
        "user.name@databricks.com"\
      ],
      "on_success": [\
        "user.name@databricks.com"\
      ],
      "on_failure": [\
        "user.name@databricks.com"\
      ],
      "on_duration_warning_threshold_exceeded": [\
        "user.name@databricks.com"\
      ],
      "on_streaming_backlog_exceeded": [\
        "user.name@databricks.com"\
      ],
      "no_alert_for_skipped_runs": false
    },
    "webhook_notifications": {
      "on_start": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_success": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_failure": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_duration_warning_threshold_exceeded": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ],
      "on_streaming_backlog_exceeded": [\
        [\
          {\
            "id": "0481e838-0a59-4eff-9541-a4ca6f149574"\
          }\
        ]\
      ]
    },
    "notification_settings": {
      "no_alert_for_skipped_runs": false,
      "no_alert_for_canceled_runs": false,
      "alert_on_last_attempt": false
    },
    "timeout_seconds": 86400,
    "health": {
      "rules": [\
        {\
          "metric": "RUN_DURATION_SECONDS",\
          "op": "GREATER_THAN",\
          "value": 10\
        }\
      ]
    },
    "schedule": {
      "quartz_cron_expression": "20 30 * * * ?",
      "timezone_id": "Europe/London",
      "pause_status": "UNPAUSED"
    },
    "trigger": {
      "pause_status": "UNPAUSED",
      "file_arrival": {
        "url": "string",
        "min_time_between_triggers_seconds": 0,
        "wait_after_last_change_seconds": 0
      },
      "periodic": {
        "interval": 0,
        "unit": "HOURS"
      }
    },
    "continuous": {
      "pause_status": "UNPAUSED"
    },
    "max_concurrent_runs": 10,
    "tasks": [\
      {\
        "max_retries": 3,\
        "task_key": "Sessionize",\
        "description": "Extracts session data from events",\
        "min_retry_interval_millis": 2000,\
        "depends_on": [],\
        "timeout_seconds": 86400,\
        "spark_jar_task": {\
          "main_class_name": "com.databricks.Sessionize",\
          "parameters": [\
            "--data",\
            "dbfs:/path/to/data.json"\
          ]\
        },\
        "libraries": [\
          {\
            "jar": "dbfs:/mnt/databricks/Sessionize.jar"\
          }\
        ],\
        "retry_on_timeout": false,\
        "existing_cluster_id": "0923-164208-meows279"\
      },\
      {\
        "max_retries": 3,\
        "task_key": "Orders_Ingest",\
        "description": "Ingests order data",\
        "job_cluster_key": "auto_scaling_cluster",\
        "min_retry_interval_millis": 2000,\
        "depends_on": [],\
        "timeout_seconds": 86400,\
        "spark_jar_task": {\
          "main_class_name": "com.databricks.OrdersIngest",\
          "parameters": [\
            "--data",\
            "dbfs:/path/to/order-data.json"\
          ]\
        },\
        "libraries": [\
          {\
            "jar": "dbfs:/mnt/databricks/OrderIngest.jar"\
          }\
        ],\
        "retry_on_timeout": false\
      },\
      {\
        "max_retries": 3,\
        "task_key": "Match",\
        "description": "Matches orders with user sessions",\
        "notebook_task": {\
          "base_parameters": {\
            "age": "35",\
            "name": "John Doe"\
          },\
          "notebook_path": "/Users/user.name@databricks.com/Match"\
        },\
        "min_retry_interval_millis": 2000,\
        "depends_on": [\
          {\
            "task_key": "Orders_Ingest"\
          },\
          {\
            "task_key": "Sessionize"\
          }\
        ],\
        "new_cluster": {\
          "autoscale": {\
            "max_workers": 16,\
            "min_workers": 2\
          },\
          "node_type_id": null,\
          "spark_conf": {\
            "spark.speculation": true\
          },\
          "spark_version": "7.3.x-scala2.12"\
        },\
        "timeout_seconds": 86400,\
        "retry_on_timeout": false,\
        "run_if": "ALL_SUCCESS"\
      }\
    ],
    "job_clusters": [\
      {\
        "job_cluster_key": "auto_scaling_cluster",\
        "new_cluster": {\
          "autoscale": {\
            "max_workers": 16,\
            "min_workers": 2\
          },\
          "node_type_id": null,\
          "spark_conf": {\
            "spark.speculation": true\
          },\
          "spark_version": "7.3.x-scala2.12"\
        }\
      }\
    ],
    "git_source": {
      "git_branch": "main",
      "git_provider": "gitHub",
      "git_url": "https://github.com/databricks/databricks-cli"
    },
    "tags": {
      "cost-center": "engineering",
      "team": "jobs"
    },
    "format": "SINGLE_TASK",
    "queue": {
      "enabled": true
    },
    "parameters": [\
      {\
        "default": "users",\
        "name": "table"\
      }\
    ],
    "run_as": {
      "user_name": "user@databricks.com",
      "service_principal_name": "692bc6d0-ffa3-11ed-be56-0242ac120002"
    },
    "edit_mode": "UI_LOCKED",
    "deployment": {
      "kind": "BUNDLE",
      "metadata_file_path": "string"
    },
    "environments": [\
      {\
        "environment_key": "string",\
        "spec": {\
          "client": "1",\
          "dependencies": [\
            "string"\
          ]\
        }\
      }\
    ]
  },
  "fields_to_remove": [\
    "libraries",\
    "schedule",\
    "tasks/task_1",\
    "job_clusters/Default"\
  ]
}
```

# Response samples

200

```
{}
```

# General Documentation

Databricks REST API ReferenceAPI
Git Credentials
Cluster Policies
Command Execution
Global Init Scripts
Instance Pools
Managed Libraries
Policy compliance for clusters
Policy Families
Jobs (2.2)
Jobs (2.1)
Create a new job
Create and trigger a one-time run
Update all job settings (reset)
Update job settings partially
Delete a job
Get a single job
List jobs
Trigger a new job run
Repair a job run
List job runs
Get a single job run
Delete a job run
Cancel a run
Cancel all runs of a job
Get the output for a single run
Export and retrieve a job run
Policy compliance for jobs
Delta Live Tables
Files Public preview
Model Registry
Serving endpoints
Apps Public preview
Identity and Access Management
Account Access Control Proxy Public preview
Current User Public preview
Groups Public preview
Service Principals Public preview
Users Public preview
Alerts Public preview
Alerts (legacy) Public preview
Dashboards (legacy)
Data Sources (legacy)
ACL / Permissions
Queries Public preview
Queries (legacy)
Query History
Statement Execution
SQL Warehouses
Artifact Allowlists Public preview
Connections Public preview
External Locations
Model Versions
Online Tables Public preview
Quality Monitors
Registered Models
Resource Quotas
Storage Credentials
SystemSchemas Public preview
Table Constraints
Temporary Table Credentials
Workspace Bindings
Recipient Activation
IP Access Lists
Notification Destinations
Token management
Workspace Conf
Consumer Fulfillments Public preview
Consumer Installations Public preview
Consumer Listings Public preview
Consumer Personalization Requests Public preview
Consumer Providers Public preview
Provider Exchange Filters Public preview
Provider Exchanges Public preview
Provider Files Public preview
Provider Listings Public preview
Provider Personalization Requests Public preview
Provider Providers Analytics Dashboards Public preview
Provider Providers Public preview
Task Runs
Clean Rooms
## Jobs (2.1)
The Jobs API allows you to create, edit, and delete jobs.
You can use an Azure Databricks job to run a data processing or data analysis task in an Azure Databricks
cluster with scalable resources. Your job can consist of a single task or can be a large,
multi-task workflow with complex dependencies. Azure Databricks manages the task orchestration,
cluster management, monitoring, and error reporting for all of your jobs. You can run your jobs
immediately or periodically through an easy-to-use scheduling system. You can implement
job tasks using notebooks, JARS, Delta Live Tables pipelines, or Python, Scala, Spark
submit, and Java applications.
Secrets CLI
Databricks CLI
Secrets utility

