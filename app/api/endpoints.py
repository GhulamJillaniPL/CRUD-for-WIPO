from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from ..services.wipo_service import WIPOService
from ..models import Trademark, TrademarkCreate, TrademarkUpdate

router = APIRouter()
wipo_service = WIPOService()

@router.post("/trademarks", response_model=Trademark)
async def create_trademark(trademark_data: TrademarkCreate):
    try:
        trademark = await wipo_service.create_trademark(trademark_data)
        return trademark
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/trademarks/{trademark_id}", response_model=Trademark)
async def get_trademark(trademark_id: str):
    try:
        trademark = await wipo_service.get_trademark(trademark_id)
        return trademark
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/trademarks/search/", response_model=List[Trademark])
async def search_trademarks(
    query: str = Query(..., description="Search query"),
    year: Optional[int] = Query(None, description="Registration year")
):
    try:
        trademarks = await wipo_service.search_trademarks(query, year)
        return trademarks
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/trademarks/{trademark_id}", response_model=Trademark)
async def update_trademark(trademark_id: str, trademark_data: TrademarkUpdate):
    try:
        trademark = await wipo_service.update_trademark(trademark_id, trademark_data)
        return trademark
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/trademarks/{trademark_id}")
async def delete_trademark(trademark_id: str):
    try:
        await wipo_service.delete_trademark(trademark_id)
        return {"message": f"Trademark {trademark_id} has been deleted"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
