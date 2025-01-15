from .repository import ItemRepository
from .errors import ItemNotFoundError

class PricingRules:
    @staticmethod
    def get_all_items():
        items = ItemRepository.get_all_items()
        pricing = {}
        for item in items:
            pricing[item.name] = {
                'unit_price': item.unit_price,
                'special_price': (item.special_quantity, item.special_price) if item.special_quantity and item.special_price else None,
            }
        return pricing



class CheckoutService:
    def __init__(self):
        self.pricing_rules = PricingRules.get_all_items()

    def calculate_total(self, items):
        item_counts = self.count_items(items)
        total = 0

        for item, count in item_counts.items():
            pricing = self.pricing_rules[item]
            unit_price = pricing['unit_price']
            special_price = pricing['special_price']

            if special_price:
                special_quantity, special_cost = special_price
                total += (count // special_quantity) * special_cost
                total += (count % special_quantity) * unit_price
            else:
                total += count * unit_price

        return total

    def count_items(self, items):
        item_counts = {}
        for item in items:
            if item not in self.pricing_rules:
                raise ItemNotFoundError(item)
            item_counts[item] = item_counts.get(item, 0) + 1
        return item_counts