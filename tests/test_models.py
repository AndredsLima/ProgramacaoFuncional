import pytest
from models.item_model import ItemBase, ItemCreate, ItemUpdate, Item

def test_item_base_validation():

    item = ItemBase(name="Item 1", price=10.0)
    assert item.name == "Item 1"
    assert item.price == 10.0


    with pytest.raises(ValueError):
        ItemBase(name="Item 1", price=-10.0)

def test_item_create_validation():

    item = ItemCreate(name="Item 1", price=10.0)
    assert item.name == "Item 1"
    assert item.price == 10.0

def test_item_update_validation():

    item = ItemUpdate(name="Item 1", price=10.0)
    assert item.name == "Item 1"
    assert item.price == 10.0


    item = ItemUpdate(price=15.0)
    assert item.price == 15.0
    assert item.name is None

def test_item_validation():

    item = Item(id=1, name="Item 1", price=10.0)
    assert item.id == 1
    assert item.name == "Item 1"
    assert item.price == 10.0