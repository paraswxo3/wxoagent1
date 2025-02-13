from requests import post
payload = {"days":"30"}
response = post('https://dev.api.ibm.com/rpa/sandbox/baw-automation-service/automation-service/CIODXIP/IPInvoiceAutomation/fetchInvoicesNeeded', json=payload,
  headers={'client_id': '6626bd6d3b271eebe0d87392a704d806','Content-Type':'application/json'})
#print(response.content.decode('utf-8'))