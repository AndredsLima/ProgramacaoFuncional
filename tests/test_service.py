from services.item_service import ItemService
from models.item_model import ItemCreate, ItemUpdate

def test_create_item():
    service = ItemService()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = service.create_item(item_data)
    assert item.name == "Item 1"
    assert item.price == 10.0

def test_get_items():
    service = ItemService()
    item_data = ItemCreate(name="Item 1", price=10.0)
    service.create_item(item_data)
    items = service.get_items()
    assert len(items) == 1
    assert items[0].name == "Item 1"

def test_get_item_by_id():
    service = ItemService()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = service.create_item(item_data)
    fetched_item = service.get_item(item.id)
    assert fetched_item.name == "Item 1"

def test_update_item():
    service = ItemService()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = service.create_item(item_data)
    updated_data = ItemUpdate(name="Updated Item", price=15.0)
    updated_item = service.update_item(item.id, updated_data)
    assert updated_item.name == "Updated Item"
    assert updated_item.price == 15.0

def test_delete_item():
    service = ItemService()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = service.create_item(item_data)
    assert service.delete_item(item.id) is True
    assert service.get_item(item.id) is None

def test_search_items_by_name():
    service = ItemService()
    item_data = ItemCreate(name="Item 1", price=10.0)
    service.create_item(item_data)
    items = service.search_items_by_name("Item")
    assert len(items) == 1
    assert items[0].name == "Item 1"

def test_transform_prices():
    service = ItemService()
    item_data = ItemCreate(name="Item 1", price=10.0)
    item = service.create_item(item_data)
    transformed_items = service.transform_prices(lambda price: price * 1.10, [item.id])
    assert transformed_items[0].price == 11.0