from typing import List, Optional,Callable
from models.item_model import Item, ItemCreate, ItemUpdate
from repositories.item_repository import ItemRepository
class ItemService:
    def __init__(self):
        self.repository = ItemRepository()

    # Cria um novo item
    def create_item(self, item: ItemCreate) -> Item:
        return self.repository.create(item)

    # Retorna todos os itens
    def get_items(self) -> List[Item]:
        return self.repository.get_all()

    # Retorna um item específico pelo ID
    def get_item(self, item_id: int) -> Optional[Item]:
        return self.repository.get_by_id(item_id)

    # Retorna um item específico nome  (1.Função Lambda)
    def search_items_by_name(self, name: str) -> List[Item]:
        items = self.repository.get_all()
        # Usando lambda para filtrar itens pelo nome
        return list(filter(lambda item: name.lower() in item.name.lower(), items))

    # Atualiza um item existente
    def update_item(self, item_id: int, item: ItemUpdate) -> Optional[Item]:
        return self.repository.update(item_id, item)

    def transform_prices(self, transform_fn: Callable[[float], float], item_ids: List[int]) -> List[Item]:
        transformed_items = []

        for item_id in item_ids:
            item=self.repository.get_by_id(item_id)
            if item:
                new_price = transform_fn(item.price)
                updated_item = self.repository.update(item.id, ItemUpdate(price=new_price))
                if updated_item:
                    transformed_items.append(updated_item)

        return transformed_items

    # Remove um item
    def delete_item(self, item_id: int) -> bool:
        return self.repository.delete(item_id)