import httpx
from datetime import datetime, timedelta
from typing import List, Optional
from ..config import settings
from ..models import Trademark, TrademarkCreate, TrademarkStatus

class WIPOService:
    def __init__(self):
        self.base_url = "https://api.wipo.int/api/v1"
        self.headers = {
            "X-API-Key": settings.wipo_api_key,
            "X-API-Secret": settings.wipo_api_secret,
        }

    async def create_trademark(self, trademark_data: TrademarkCreate) -> Trademark:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/trademarks",
                    headers=self.headers,
                    json=trademark_data.dict()
                )
                response.raise_for_status()
                data = response.json()
                
                return Trademark(
                    id=data["id"],
                    name=data["name"],
                    description=data.get("description"),
                    registration_date=datetime.now(),
                    expiration_date=datetime.now() + timedelta(days=3650),  # 10 years
                    status=TrademarkStatus.PENDING,
                    owner=data["owner"],
                    classes=data["classes"],
                    country_codes=data["country_codes"]
                )
            except httpx.HTTPError as e:
                raise Exception(f"Failed to create trademark: {str(e)}")

    async def get_trademark(self, trademark_id: str) -> Trademark:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{self.base_url}/trademarks/{trademark_id}",
                    headers=self.headers
                )
                response.raise_for_status()
                data = response.json()
                
                return Trademark(**data)
            except httpx.HTTPError as e:
                raise Exception(f"Failed to get trademark: {str(e)}")

    async def search_trademarks(self, query: str, registration_year: Optional[int] = None) -> List[Trademark]:
        async with httpx.AsyncClient() as client:
            try:
                params = {"q": query}
                if registration_year:
                    params["year"] = registration_year
                    
                response = await client.get(
                    f"{self.base_url}/trademarks/search",
                    headers=self.headers,
                    params=params
                )
                response.raise_for_status()
                data = response.json()
                
                return [Trademark(**item) for item in data["results"]]
            except httpx.HTTPError as e:
                raise Exception(f"Failed to search trademarks: {str(e)}")

    async def update_trademark(self, trademark_id: str, trademark_data: TrademarkUpdate) -> Trademark:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.put(
                    f"{self.base_url}/trademarks/{trademark_id}",
                    headers=self.headers,
                    json=trademark_data.dict(exclude_unset=True)
                )
                response.raise_for_status()
                data = response.json()
                
                return Trademark(**data)
            except httpx.HTTPError as e:
                raise Exception(f"Failed to update trademark: {str(e)}")

    async def delete_trademark(self, trademark_id: str):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.delete(
                    f"{self.base_url}/trademarks/{trademark_id}",
                    headers=self.headers
                )
                response.raise_for_status()
            except httpx.HTTPError as e:
                raise Exception(f"Failed to delete trademark: {str(e)}")
