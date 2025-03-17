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

@router.get("/items/search/", response_model=List[Item])
async def search_items_byname(name: str):
    items = item_service.search_items_by_name(name)
    if not items:
        raise HTTPException(status_code=404, detail="No items found with the given name")
    return items

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
    transform_type: str
    items: List[int]

# Endpoint para transformar preços
@router.post("/items/transform-prices/", response_model=List[Item])
async def transform_prices(request: PriceTransformRequest):
    """
    Aplica uma transformação nos preços dos itens com base no tipo de transformação especificado.

    Tipos de transformação disponíveis:
    - **tax**: Aplica uma taxa de 10% sobre o preço.
    - **discount**: Aplica um desconto de 20% sobre o preço.
    - **round**: Arredonda o preço para duas casas decimais.
    """
    transform_fns = {
        "tax": lambda price: price * 1.10,
        "discount": lambda price: price * 0.80,
        "round": lambda price: round(price, 2),
    }

    if request.transform_type not in transform_fns:
        raise HTTPException(status_code=400, detail="Tipo de transformação inválido.")

    transformed_items = item_service.transform_prices(transform_fns[request.transform_type], request.items)
    return transformed_items