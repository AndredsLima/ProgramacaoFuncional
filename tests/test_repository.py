from repositories.item_repository import ItemRepository
from models.item_model import ItemCreate, ItemUpdate

def test_create_item():
    repo = ItemRepository()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = repo.create(item_data)
    assert item.id == 1
    assert item.name == "Item 1"
    assert item.price == 10.0

def test_get_all_items():
    repo = ItemRepository()
    item_data = ItemCreate(name="Item 1", price=10.0)
    repo.create(item_data)
    items = repo.get_all()
    assert len(items) == 1
    assert items[0].name == "Item 1"

def test_get_item_by_id():
    repo = ItemRepository()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = repo.create(item_data)
    fetched_item = repo.get_by_id(item.id)
    assert fetched_item.name == "Item 1"

def test_update_item():
    repo = ItemRepository()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = repo.create(item_data)
    updated_data = ItemUpdate(name="Updated Item", price=15.0)
    updated_item = repo.update(item.id, updated_data)
    assert updated_item.name == "Updated Item"
    assert updated_item.price == 15.0

def test_delete_item():
    repo = ItemRepository()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = repo.create(item_data)
    assert repo.delete(item.id) is True
    assert repo.get_by_id(item.id) is None