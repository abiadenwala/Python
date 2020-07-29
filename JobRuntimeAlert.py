# Databricks notebook source
dbutils.widgets.text("Runs_Longer_By(Min)", " ")

# COMMAND ----------

#print all the Job runs actively running for longer than X minutes
Runs_Longer_By_Millisec = int(dbutils.widgets.get("Runs_Longer_By(Min)")) * 60000
#print(Runs_Longer_By_Millisec)

# COMMAND ----------

# Fetch region and token 
apiUrl = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().getOrElse(None)
token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().getOrElse(None)

# COMMAND ----------

#Form API Endpoint and Header
import requests
import json
import os
apiEndpoint = apiUrl + "/api/2.0/jobs/runs/list?active_only=true&limit=150"
headers={'Authorization': "Bearer " + token, 'Accept':"application/json"}

# COMMAND ----------

# Get current time for time comparison later
import time
current_time = int(round(time.time() * 1000))

# COMMAND ----------

# Get all the active runs and print only runs which are running for more than X mins
jobsDetails =  requests.get(apiEndpoint , headers=headers).json()
runslist = jobsDetails['runs']
for runs in runslist:
#  print("Run StartTime =" , runs['start_time'])
  run_start_time = runs['start_time']
  execution_duration = current_time - run_start_time
#  print(execution_duration)
  if execution_duration > Runs_Longer_By_Millisec:
    print("Run ", runs['run_page_url'] , "is running for", round(execution_duration/60000) , "Minutes")
