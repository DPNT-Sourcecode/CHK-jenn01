from collections import defaultdict

class Product:
    def __init__(self, sku):
        self.sku = sku
        self.price = defaultdict(int)
        self.offer = defaultdict(str)


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
        for sku, items in group_items.items():
            print(sku, items)
            total += self.calculate_total(sku, items)

        return len(group_items)


    def calculate_total(self, sku, items):
        """
        Calculate the total price of a group of items.
        """

        if sku not in GOODS:
            return 0
        offer = GOODS[sku]["offer"]
        total = len(items)
        return total