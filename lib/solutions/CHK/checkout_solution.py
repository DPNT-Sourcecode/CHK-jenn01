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


def extract_offer_cost(sku, offer):
    """
    Split offers into two parts.
    """
    nb_items_offered, value = 0, 0
    if sku == "E":
        nb_items_offered = 1
        value = 40
    else:
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
    nb_items_offered, value = extract_offer_cost(sku, offer)
    pairings = split_skus(items, nb_items_offered)
    total = sum([value for i in range(0, len(pairings)-1)])
    last_pairing = pairings[-1]
    even = False
    if len(last_pairing) < nb_items_offered:
        total += len(last_pairing) * GOODS[sku].price
        last_pairing = ""
    else:
        even = True
        total += value
    if last_pairing == items:
        last_pairing = ""
    return total, even, last_pairing


def calculate_total_multiple_offers(sku, offers, items):
    """
    Calculate the total price of multiple offers
    Presumably, we have only product having multiple offers.
    """
    offers = offers.split(", ")
    sorted_offers = sorted(offers, reverse=True)
    tail = items
    i = 0
    total = 0
    while tail:
        if (len(items) < extract_offer_cost(sku, sorted_offers[i])[0] and i <
                len(sorted_offers) - 1):
            i += 1
        else:
            _total, even, tail = calculate_total_single_offer(sku, sorted_offers[i], items)
            items = tail
            total += _total
    return total


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
                total, _, _ = calculate_total_single_offer(sku, offer, items)

        else:
            total = GOODS[sku].price * len(items)
        return total
