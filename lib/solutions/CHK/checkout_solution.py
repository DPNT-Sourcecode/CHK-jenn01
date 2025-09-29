from collections import defaultdict

class Product:
    def __init__(self, sku, price, offer):
        self.sku = sku
        self.price = price
        self.offer = offer


GOODS = defaultdict(Product)

GOODS['A'] = Product('A', 50, "3A for 130, 5A for 200")
GOODS['B'] = Product('B', 30, "2B for 45")
GOODS['C'] = Product('C', 20, "")
GOODS['D'] = Product('D', 15, "")
GOODS['E'] = Product('E', 40, "2E get one B free")


def apply_special_offers_for_new_good(skus):
    nb_new_e = skus.count('E')
    nb_rewarded_b = 0 if nb_new_e else nb_new_e // 2
    skus +=  "B" * nb_rewarded_b
    return skus


def calculate_total_single_offer(sku, offer, items):
    nb_items_offered, value, total = 0, 0, 0
    split_offer = offer.split(" for ")
    nb_items_offered = int(split_offer[0][:-1])
    value = int(split_offer[1])
    pairings = [items[i:i+nb_items_offered]
                for i in range(0, len(items), nb_items_offered)]
    total += sum([value for i in range(0, len(pairings)-1)])
    if len(pairings[-1]) < nb_items_offered:
        total += len(pairings[-1]) * GOODS[sku].price
    else:
        total += value
    return total


def calculate_total_multiple_offers(sku, offer, items):
    return 0


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        group_items = defaultdict(str)
        if not skus:
            return 0
        skus = apply_special_offers_for_new_good(skus)
        for sku in skus:
            if sku not in GOODS:
                return -1
            group_items[sku] += sku
        total = 0
        for sku, items in group_items.items():
            # print(sku, items)
            total += self.calculate_total(sku, items)

        return total


    def calculate_total(self, sku, items):
        """
        Calculate the total price of a group of items.
        """

        if sku not in GOODS:
            return -1
        offer = GOODS[sku].offer
        total = 0
        if offer:
            if sku == "A":
                total = calculate_total_multiple_offers(sku, offer, items)
            else:
                total = calculate_total_single_offer(sku, offer, items)

        else:
            total = GOODS[sku].price * len(items)
        return total