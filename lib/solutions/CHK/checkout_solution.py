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
GOODS['F'] = Product('F', 10, "2F get one F free")


def apply_special_offers_for_new_good(skus):
    """
    Applies special offers for new skus to the list of products.
    Presumably we have the new product E as provided. Now we have new F.
    2F free 1F, get 3 but pay 2
    """
    nb_new_e = skus.count('E')
    nb_rewarded_b = 0 if nb_new_e <= 0 else nb_new_e // 2
    # remove the nb_rewarded_b of 'B' because of the new good 'E'
    for i in range(0, nb_rewarded_b):
        skus = skus.replace('B', '', 1)
    return skus


def extract_offer_cost(sku, offer):
    """
    Split offers into two parts.
    """
    nb_items_offered, value = 0, 0
    if sku == "E":
        nb_items_offered = 1
        value = 40
    elif sku == "F":
        nb_items_offered = 1
        value = 10
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
    if nb_items_offered == 1:
        total = value * len(items)
        return total, True, nb_items_offered
    pairings = split_skus(items, nb_items_offered)
    total = sum([value for i in range(0, len(pairings)-1)])
    last_pairing = pairings[-1]
    even = False
    if nb_items_offered == 1:
        even = True
        last_pairing = ""
    elif len(last_pairing) < nb_items_offered:
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
    while tail and i < len(sorted_offers):
        offer = sorted_offers[i]
        nb, value = extract_offer_cost(sku, offer)
        while tail:
            block = tail[:nb]
            if len(block) == nb:
                # found a block of the size nb
                total += value
                tail = tail[nb:]
            else:
                i += 1
                break
    # add up the tail if it is not empty
    for _item in tail:
        total += GOODS[sku].price
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

