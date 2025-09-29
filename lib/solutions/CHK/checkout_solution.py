from collections import defaultdict

class Product:
    def __init__(self, sku):
        self.sku = sku
        self.price = defaultdict(int)
        self.discount = defaultdict(str)


GOODS = defaultdict(Product)


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        group_items = defaultdict(str)
        if not skus:
            return -1
        skus = skus.upper()
        for sku in skus:
            group_items[sku] += sku
        total = 0
        for group, items in group_items.items():
            print(group, items)
            total += self.calculate_total(items)

        return len(group_items)


    def calculate_total(self, items):
        """
        Calculate the total price of a group of items.
        """
        total = len(items)
        return total