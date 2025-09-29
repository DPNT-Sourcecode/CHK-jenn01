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
    """
    Applies special offers for new skus to the list of products.
    Presumably we have the new product E as provided
    """
    nb_new_e = skus.count('E')
    nb_rewarded_b = 0 if nb_new_e else nb_new_e // 2
    skus +=  "B" * nb_rewarded_b
    return skus


def extract_offer_cost(offer):
    """
    Split offers into two parts.
    """
    nb_items_offered, value = 0, 0
    split_offer = offer.split(" for ")
    nb_items_offered = int(split_offer[0][:-1])
    value = int(split_offer[1])
    return nb_items_offered, value

def split_skus(skus, size):
    """
    Split a sku into smaller chunks of a specified size
    """
    s = [skus[i:i+size] for i in range(0, len(skus), size)]
    return s


def calculate_total_single_offer(sku, offer, items):
    """
    Calculate the total price of a single offer
    """
    nb_items_offered, value = extract_offer_cost(offer)
    pairings = split_skus(items, nb_items_offered)
    total = sum([value for i in range(0, len(pairings)-1)])
    if len(pairings[-1]) < nb_items_offered:
        total += len(pairings[-1]) * GOODS[sku].price
    else:
        total += value
    return total


def calculate_total_multiple_offers(sku, offers, items):
    """
    Calculate the total price of multiple offers
    Presumably, we have only product having multiple offers.
    """
    offers = offers.split(", ")
    sorted_offers = sorted(offers, reverse=True)
    for offer in offers:
        pass
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
        if offer:
            if sku == "A":
                total = calculate_total_multiple_offers(sku, offer, items)
            else:
                total = calculate_total_single_offer(sku, offer, items)

        else:
            total = GOODS[sku].price * len(items)
        return total





