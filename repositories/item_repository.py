from typing import Dict, List, Optional
from models.item_model import Item, ItemCreate, ItemUpdate
from utils.functional_utils import generate_id


class ItemRepository:
    def __init__(self):

        self.db: Dict[int, Dict] = {}


    def create(self, item: ItemCreate) -> Item:
        item_id = generate_id(self.db)()
        item_dict = item.model_dump()
        item_dict["id"] = item_id
        self.db[item_id] = item_dict
        return Item(**item_dict)


    def get_all(self) -> List[Item]:
        return [Item(**item) for item in self.db.values()]


    def get_by_id(self, item_id: int) -> Optional[Item]:
        item = self.db.get(item_id)
        return Item(**item) if item else None


    def update(self, item_id: int, item: ItemUpdate) -> Optional[Item]:
        if item_id not in self.db:
            return None

        current_item = self.db[item_id]
        update_data = item.model_dump(exclude_unset=True)
        updated_item = {**current_item, **update_data}
        self.db[item_id] = updated_item

        return Item(**updated_item)


    def delete(self, item_id: int) -> bool:
        if item_id not in self.db:
            return False
        del self.db[item_id]
        return True