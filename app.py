from fastapi import FastAPI, Header, Depends, Security, HTTPException, Body
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import bg_search_agent

app = FastAPI()

class BGClauseResponse(BaseModel):
    response: str

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=True)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "Auth012346":
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    return api_key


@app.post("/bg/find-clause", response_model=BGClauseResponse, dependencies=[Depends(verify_api_key)])
def searchBG(text_to_search: str = Body(..., embed=True)):
   response = bg_search_agent.invoke_aget(input_text=text_to_search)
   return {"response":response}

if __name__ == '__main__':
    import uvicorn
    print("starting.....")
    uvicorn.run(app, host='0.0.0.0', port=8080)