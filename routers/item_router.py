from fastapi import APIRouter, HTTPException
from typing import List
from models.item_model import Item, ItemCreate, ItemUpdate
from services.item_service import ItemService
from pydantic import BaseModel

router = APIRouter()
item_service = ItemService()


@router.post("/items/", response_model=Item)
async def create_new_item(item: ItemCreate):
    return item_service.create_item(item)


@router.get("/items/", response_model=List[Item])
async def list_items():
    return item_service.get_items()


@router.get("/items/{item_id}", response_model=Item)
async def get_single_item(item_id: int):
    item = item_service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/items/{item_id}", response_model=Item)
async def update_existing_item(item_id: int, item: ItemUpdate):
    updated_item = item_service.update_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

# Remove um item
@router.delete("/items/{item_id}")
async def delete_existing_item(item_id: int):
    if not item_service.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

class PriceTransformRequest(BaseModel):
    transform_type: str  # Tipo de transformação (tax, discount, round)
    items: List[int]     # IDs dos itens a serem transformados

# Endpoint para transformar preços
@router.post("/items/transform-prices/", response_model=List[Item])
async def transform_prices(request: PriceTransformRequest):
    # Mapeamento de funções de transformação
    transform_fns = {
        "tax": lambda price: price * 1.10,       # Aplica 10% de taxa
        "discount": lambda price: price * 0.80,  # Aplica 20% de desconto
        "round": lambda price: round(price, 2),  # Arredonda para duas casas decimais
    }

    # Verifica se o tipo de transformação é válido
    if request.transform_type not in transform_fns:
        raise HTTPException(status_code=400, detail="Tipo de transformação inválido.")

    # Aplica a transformação aos itens
    transformed_items = item_service.transform_prices(transform_fns[request.transform_type],request.items)
    return transformed_items
