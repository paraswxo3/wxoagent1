import json

str = """
{
    "id": "chatcmpl-83d1d6382fd296dc8549df172084a3ff",
    "model_id": "meta-llama/llama-3-2-90b-vision-instruct",
    "model": "meta-llama/llama-3-2-90b-vision-instruct",
    "choices": [{
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "**Invoice Data Extraction**\n\n**Invoice Number:** 21-499\n**Invoice Date:** 6-Nov-21\n**PO Number:** P6QQWT01-19/July/21\n**Order Date:** Not provided\n**VAT Number:** Not provided\n**Vendor Name:** IBM Solutions Delivery, Inc.\n**Value Added Tax:** Not applicable (based on the statement that "THIS DOCUMENT IS NOT VALID FOR CLAIMING INPUT TAX")\n**Total Amount:** PHP 47,700.00\n**Total:** PHP 47,700.00\n**Taxable Amount:** Not applicable (as Value Added Tax is not applicable)\n\n**Line Items:**\n\n* **Base Daily Billing:** PHP 636,000.00\n* **Night Shift Differential:** PHP 63,600.00\n* **Standby Support:** PHP 103,125.00\n\n**JSON Object:**\n\n```\n{\n  "Invoice Number": "21-499",\n  "Invoice Date": "6-Nov-21",\n  "PO Number": "P6QQWT01-19/July/21",\n  "Order Date": "N/A",\n  "VAT Number": "N/A",\n  "Vendor Name": "IBM Solutions Delivery, Inc.",\n  "Value Added Tax": "N/A",\n  "Total Amount": "PHP 47,700.00",\n  "Total": "PHP 47,700.00",\n  "Taxable Amount": "N/A",\n  "Line Items": [\n    {\n      "Description": "Base Daily Billing",\n      "Amount": "PHP 636,000.00"\n    },\n    {\n      "Description": "Night Shift Differential",\n      "Amount": "PHP 63,600.00"\n    },\n    {\n      "Description": "Standby Support",\n      "Amount": "PHP 103,125.00"\n    }\n  ]\n}\n```\n\nNote: N/A indicates that the information was not provided in the invoice."
            },
            "finish_reason": "stop"
        }
    ],
    "created": 1738923963,
    "model_version": "3.2.0",
    "created_at": "2025-02-07T10:26:23.744Z",
    "usage": {
        "completion_tokens": 406,
        "prompt_tokens": 6471,
        "total_tokens": 6877
    },
    "system": {
        "warnings": [{
                "message": "This model is a Non-IBM Product governed by a third-party license that may impose use restrictions and other obligations. By using this model you agree to its terms as identified in the following URL.",
                "id": "disclaimer_warning",
                "more_info": "https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models.html?context=wx"
            }, {
                "message": "The value of "max_tokens" for this model was set to value 1024",
                "id": "unspecified_max_token",
                "additional_properties": {
                    "limit": 0,
                    "new_value": 1024,
                    "parameter": "max_tokens",
                    "value": 0
                }
            }
        ]
    }
}
"""

print(json.loads(str))