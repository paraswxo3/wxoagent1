import requests
import json
import os


def invoke_agent(input_text: str):
  API_KEY = os.getenv("API_KEY")
  token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
  API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
  mltoken = token_response.json()["access_token"]

  header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
  #print("header ",header)
  # NOTE:  manually define and pass the array(s) of values to be scored in the next line
  context = "The input text to search for bank guarantee clause is the following sentence."
  instruction = "Execute the function that best matches the text and return the response. When providing the response, please provide a precise and summarized answer that answers the query. Avoid including the input text. Only mention the relevance score, the type of the clause and the clause content"
  input_text = context+input_text+instruction
  payload_scoring = {"messages":[{"content":input_text,"role":"assistant"}]}
  # payload_scoring = {"messages":[{"content":"Fetch the invoices needed in the next 30 days","role":"assistant"}]}

  response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5057c777-1440-495a-acfc-7309688d101c/ai_service?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})
  response = "unable to identify the BG clause"
  try:
    for line in response_scoring.iter_lines():
      if line:
        line = line.decode('utf-8')
        val = json.loads(line)
        response = val["choices"][0]["message"]["content"]
  except KeyboardInterrupt:
      print("Stream interrupted")
  finally:
      response_scoring.close()
  return response
# text = "The clause will remain valid from 10th of March 2024 to 10 of Feb 2025."
# text = "Find the clause in this text: This Guarantee shall remain valid for a period of 24 months from the date of issuance."
# print(invoke_agent(input_text=text))
# print(response_scoring.content)

