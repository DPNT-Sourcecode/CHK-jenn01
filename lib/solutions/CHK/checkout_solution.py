from collections import defaultdict

class Product:
    def __init__(self, sku, price, offer):
        self.sku = sku
        self.price = price
        self.offer = offer


GOODS = defaultdict(Product)

GOODS['A'] = Product('A', 20, "2A for 25")
GOODS['B'] = Product('B', 10, "")
GOODS['C'] = Product('C', 5, "3C for 12")
GOODS['D'] = Product('D', 6, "5D for 25")

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
            # print(sku, items)
            total += self.calculate_total(sku, items)

        return len(group_items)


    def calculate_total(self, sku, items):
        """
        Calculate the total price of a group of items.
        """

        if sku not in GOODS:
            return 0
        offer = GOODS[sku].offer
        nb_items_offered, value, total = 0, 0, 0
        if offer:
            split_offer = offer.split(" for ")
            nb_items_offered = int(split_offer[0][:-1])
            value = int(split_offer[1])
            pairings = [items[i:i+nb_items_offered]
                        for i in range(0, len(items), nb_items_offered)]
            print(pairings)
            total = len(items)
        else:
            total = GOODS[sku].price * len(items)
        return total



