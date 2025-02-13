import requests
import aiohttp
import asyncio

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html?context=wx)
API_KEY = "J2RXBMWxC9R9ktvjuqeXahKg91QxMnFiwXCS5sV8qKQn"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
#print("header ",header)
# NOTE:  manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"messages":[{"content":"Fetch invoice needed number of days being 30, execute the function and send the results","role":"assistant"}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/61960b1c-b926-4136-a325-411721a54f7e/ai_service?version=2021-05-01', json=payload_scoring,
  headers={'Authorization': 'Bearer ' + mltoken})
try:
  for line in response_scoring.iter_lines():
    if line:
      print(line.decode('utf-8'))
except KeyboardInterrupt:
    print("Stream interrupted")
finally:
    response_scoring.close()
print("Scoring response")
print(response_scoring.content)

