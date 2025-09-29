from collections import defaultdict

class Product:
    def __init__(self, sku):
        self.sku = sku
        self.price = defaultdict(int)

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        group_items = defaultdict(str)
        if not skus:
            return -1
        skus = skus.upper()
        for sku in skus:
            group_items[sku] += sku
        return len(group_items)



