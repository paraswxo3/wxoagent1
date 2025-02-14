from fastapi import FastAPI, File, Header, Depends, Security, HTTPException, Body, UploadFile
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import bg_search_agent
from pdf_extractor import extract_paragraphs_from_base64
from typing import List

app = FastAPI()

class BGClauseResponse(BaseModel):
    response: str

class BGParagraphs(BaseModel):
    paragraphs: List[str]

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=True)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "Auth012346":
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    return api_key


@app.post("/find-clause", response_model=BGClauseResponse, dependencies=[Depends(verify_api_key)])
def searchBG(text_to_search: str = Body(..., embed=True)):
   response = bg_search_agent.invoke_aget(input_text=text_to_search)
   return {"response":response}

# @app.post("/upload_pdf", response_model=BGParagraphs, dependencies=[Depends(verify_api_key)])
# async def upload_pdf(file: UploadFile = File(...)):
#     pdf_bytes = await file.read()  # Read file content
#     paragraphs = extract_paragraphs_from_base64(pdf_bytes)
#     return {"paragraphs":paragraphs}

@app.post("/upload_pdf", response_model=BGParagraphs, dependencies=[Depends(verify_api_key)])
async def upload_pdf(content: str = Body(..., embed=True)):
    paragraphs = extract_paragraphs_from_base64(content)
    return {"paragraphs":paragraphs}

if __name__ == '__main__':
    import uvicorn
    print("starting.....")
    uvicorn.run(app, host='0.0.0.0', port=8080)