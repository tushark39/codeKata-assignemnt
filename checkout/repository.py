from .models import Item

class ItemRepository:
    @staticmethod
    def get_all_items():
        return Item.objects.all()

    @staticmethod
    def get_item_by_name(name):
        return Item.objects.filter(name=name).first()
