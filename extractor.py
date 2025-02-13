import os
import json
import wget
from pdf2image import convert_from_path
from PIL import Image
from langchain.document_loaders import PDFPlumberLoader
from langchain.schema import SystemMessage, HumanMessage
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from IPython.display import Image
import base64


filename = 'ibm_logo.jpg'
url = 'https://raw.github.com/IBM/watson-machine-learning-samples/master/cloud/data/logo/ibm_logo.jpg'
if not os.path.isfile(filename):
    wget.download(url, out=filename)
Image(filename=filename, width=600)
with open(filename, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# ---- 1. Convert Invoice PDF to Image ----
def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    image_path = "invoice.jpg"
    images[0].save(image_path, "JPEG")
    return image_path

# ---- 2. IBM Watsonx.ai Authentication ----
IBM_API_KEY = "your-ibm-api-key"
IBM_SERVICE_URL = "https://us-south.ml.cloud.ibm.com"
MODEL_ID = "meta-llama/llama-3-2-90b-vision-instruct"

credentials = Credentials(
    url="https://us-south.ml.cloud.ibm.com",
    api_key="jDAsTH4sneg9mAHK5tCjc6UULaIncdHEvRxwRm-VsOap"
    )
project_id = "273897d8-8d34-4b72-b2d0-c94de5c6b75e"
params = TextChatParameters(
    temperature=1
)
model  = ModelInference(
    model_id=MODEL_ID,
    credentials=credentials,
    project_id=project_id,
    params=params
)
question = "Describe the image"
messages = [
  {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": question
      },
      {
        "type": "image_url",
        "image_url": {
          "url": "data:image/jpeg;base64," + encoded_string,
        }
      }
    ]
  }
]
# response = model.chat(messages=messages)
# print(response)
# ---- 3. Process Invoice Image with Llama Vision ----
def extract_invoice_fields(image_path):
    prompt = (
        "Extract the following fields from the invoice image: "
        "Invoice Number, Date, PO Number, Order Date, VAT Number, Vendor Name, Value Added Tax, Total Amount,Total, Taxable Amount and Line Items."
        "Return the output in compressed JSON format."
    )
    intext = """
    Extract the following fields from the invoice image:         
    Invoice Number, Invoice Date, PO Number, Order Date, Vendor VAT Number, Vendor Name,Value Added Tax, Total Amount,Total, Taxable Amount and Line Items which consists of line item description, line item quantity, line item total and line item tax amount. 
    The vendor name cannot have IBM in it. The Vendor VAT number should be one of 008-106-583-00000, 008-601-483-00000, 108-596-583-00000,006-799-641-000
    Output must be in a proper json format where attributes should be in doube-quotes. new line character, i.e. \n should be avoided inside the invoice json.
    """
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
    msg = [
           {
    "role": "user",
    "content": [
      {
        "type": "text",
        "text": intext
      },
      {
        "type": "image_url",
        "image_url": {
          "url": "data:image/jpeg;base64," + encoded_string,
        }
      }
    ]
  }
    ]
    response = model.chat(messages=msg)
    #response = llm.generate(prompt=prompt, image=image_data)
    #response = model.generate(prompt=prompt, image_data=image_data)
    #response = model.generate(prompt=prompt)
    #print("response--",response)
    try:
        # extracted_data = json.loads(response)
        extracted_data = response
    except json.JSONDecodeError:
        extracted_data = {"error": "Invalid JSON response"}

    return extracted_data

# ---- 4. Main Execution ----
if __name__ == "__main__":
    pdf_path = "/home/bparasuram/python/vsc/first-project/818022022007-20220308-20220309110336358000000.pdf"  # Change this to your invoice file
    image_path = pdf_to_image(pdf_path)
    print(image_path)
    extracted_data = extract_invoice_fields(image_path)

    print("Extracted Invoice Data:", extracted_data)
