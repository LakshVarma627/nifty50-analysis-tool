from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from quantum_core.wolfram.api_integrator import WolframService

router = APIRouter()

class WolframQuery(BaseModel):
    question: str

@router.post("/wolfram/query")
async def query_wolfram(query: WolframQuery):
    service = WolframService()
    result = service.query(query.question)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
