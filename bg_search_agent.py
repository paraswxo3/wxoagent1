import requests
import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account (https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html?context=wx)
def invoke_aget(input_text: str):
  API_KEY = "J2RXBMWxC9R9ktvjuqeXahKg91QxMnFiwXCS5sV8qKQn"
  token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
  API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
  mltoken = token_response.json()["access_token"]

  header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
  #print("header ",header)
  # NOTE:  manually define and pass the array(s) of values to be scored in the next line
  payload_scoring = {"messages":[{"content":input_text,"role":"assistant"}]}
  # payload_scoring = {"messages":[{"content":"Fetch the invoices needed in the next 30 days","role":"assistant"}]}

  response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2acd2a87-5a25-4afb-9ea4-af8c91ab1248/ai_service?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
  response = "unable to identify the BG clause"
  try:
    for line in response_scoring.iter_lines():
      if line:
        line = line.decode('utf-8')
        # print(line)
        val = json.loads(line)
        response = val["choices"][0]["message"]["content"]
  except KeyboardInterrupt:
      print("Stream interrupted")
  finally:
      response_scoring.close()
  return response

text = "For this text identify the BG clause and BG category that is most relevant: The clause will remain valid from 10th of March 2024 to 10 of Feb 2025"
print(invoke_aget(text))
# print(response_scoring.content)

