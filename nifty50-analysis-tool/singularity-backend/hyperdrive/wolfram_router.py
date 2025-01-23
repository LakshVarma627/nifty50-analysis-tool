from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from quantum_core.wolfram.api_integrator import WolframService

router = APIRouter()

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    pods: list

wolfram_service = WolframService()

@router.post("/wolfram/query", response_model=QueryResponse)
async def query_wolfram(request: QueryRequest):
    try:
        result = wolfram_service.query(request.question)
        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])
        return QueryResponse(pods=result["pods"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
