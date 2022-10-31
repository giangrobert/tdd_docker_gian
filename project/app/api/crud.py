# project/app/api/crud.py

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from typing import Union
 
 
async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
   	 url=payload.url,
   	 summary="dummy summary",
    )
    await summary.save()
    return summary.id

async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
   	 return summary
    return None