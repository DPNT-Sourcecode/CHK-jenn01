from collections import defaultdict
from math import floor


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
GOODS['G'] = Product('G', 20, "")
GOODS['H'] = Product('H', 10, "5H for 45, 10H for 80")
GOODS['I'] = Product('I', 35, "")
GOODS['J'] = Product('J', 60, "")
GOODS['K'] = Product('K', 70, "2K for 120")
GOODS['L'] = Product('L', 90, "")
GOODS['M'] = Product('M', 15, "")
GOODS['N'] = Product('N', 40, "3N get one M free")
GOODS['O'] = Product('O', 10, "")
GOODS['P'] = Product('P', 50, "5P for 200")
GOODS['Q'] = Product('Q', 30, "3Q for 80")
GOODS['R'] = Product('R', 50, "3R get one Q free")
GOODS['S'] = Product('S', 20, "buy any 3 of (S,T,X,Y,Z) for 45")
GOODS['T'] = Product('T', 20, "buy any 3 of (S,T,X,Y,Z) for 45")
GOODS['U'] = Product('U', 40, "3U get one U free")
GOODS['V'] = Product('V', 50, "2V for 90, 3V for 130")
GOODS['W'] = Product('W', 20, "")
GOODS['X'] = Product('X', 17, "buy any 3 of (S,T,X,Y,Z) for 45")
GOODS['Y'] = Product('Y', 20, "buy any 3 of (S,T,X,Y,Z) for 45")
GOODS['Z'] = Product('Z', 21, "buy any 3 of (S,T,X,Y,Z) for 45")

DISCOUNTED_PRODUCTS = defaultdict(Product)
DISCOUNTED_PRODUCTS['BUY_MULTIPLE_PAY_LESS'] = ["A", "H", "V"]
DISCOUNTED_PRODUCTS['BUY_MULTIPLE_GET_FREE'] = ["E", "F", "N", "R", "U"]
DISCOUNTED_PRODUCTS['BUY_MORE_PAY_LESS'] = []
DISCOUNTED_PRODUCTS['BUY_ANY_OF'] = ["S", "T", "X", "Y", "Z"]

def do_apply_special_offer_get_one_free(skus, USED_OFFERS):
    """
    Buy n good SKU, get m good SKU free (the same product)
    """
    # For example: buy 3 pay 2
    for sku in DISCOUNTED_PRODUCTS['BUY_MULTIPLE_GET_FREE']:
        # e.g., 2F get one F free
        if USED_OFFERS[sku]:
            continue
        parts = GOODS[sku].offer.split(' get one ')
        n = int(parts[0][:-1]) # e.g., 2E -> 2
        free_item = parts[1][:1] # e.g., one F free
        if free_item == sku:
            USED_OFFERS[sku] = True
            amount = skus.count(sku)
            items_to_pay = floor(amount / (n + 1)) * n + amount%(n + 1)
            skus = skus.replace(sku, '')
            skus += sku * items_to_pay
    return skus


def do_apply_special_offer_get_other_free(skus, USED_OFFERS):
    """
    Buy n good SKU, get m free other good
    """
    for sku in DISCOUNTED_PRODUCTS['BUY_MULTIPLE_GET_FREE']:
        if USED_OFFERS[sku]:
            continue
        parts = GOODS[sku].offer.split(' get one ')
        nb_bought_items = int(parts[0][:-1]) # e.g., 2E -> 2
        free_item = parts[1][:1] # e.g., B
        if free_item != sku:
            USED_OFFERS[sku] = True
            nb_new_e = skus.count(sku)
            nb_rewarded_b = 0 if nb_new_e <= 0 else nb_new_e // nb_bought_items
            # remove the nb_rewarded_b of 'free_item'
            for i in range(0, nb_rewarded_b):
                skus = skus.replace(free_item, '', 1)
    return skus


def apply_special_offers_for_new_good(skus):
    """
    Applies special offers for new skus to the list of products.
    Presumably we have the new product E as provided. Now we have new F.
    2F free 1F, get 3 but pay 2
    """
    USED_OFFERS = dict.fromkeys(GOODS, False)

    # Discounted programmes like buy 3F get one B free
    skus = do_apply_special_offer_get_other_free(skus, USED_OFFERS)

    # Discounted programmes like buy 3F get 1F free (buy 3 pay 2)
    skus = do_apply_special_offer_get_one_free(skus, USED_OFFERS)

    # Discounted programmes like buy any of 3 ("S", "T", "X", "Y", "Z")
    return skus


def extract_offer_cost(sku, offer):
    """
    Split offers into two parts.
    """
    nb_items_offered, value = 0, 0
    if sku in DISCOUNTED_PRODUCTS['BUY_MULTIPLE_GET_FREE']:
        nb_items_offered = 1
        value = GOODS[sku].price
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

def sort_multiple_offers(offers_lst):
    """
    Sorts a list of offer strings in descending order based on the
    numeric value of the first word (the hours).

    The key extraction logic:
    1. s.split()[0]: Gets the first word (e.g., "5H", "10H").
    2. [:-1]: Removes the last character ('H').
    3. int(...): Converts the resulting string ("5", "10") to an integer for comparison.
    """
    sorted_list = sorted(
        offers_lst,
        key=lambda s: int(s.split()[0][:-1]),
        reverse=True
    )
    return sorted_list

def calculate_total_multiple_offers(sku, offers, items):
    """
    Calculate the total price of multiple offers
    Presumably, we have only product having multiple offers.
    """
    offers = offers.split(", ")
    sorted_offers = sort_multiple_offers(offers)
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


    def sort_products_by_price(product_list):
        """
        Sorts a list of products (represented as [name, price] lists)
        in descending order based on their price.

        Args:
            product_list (list): A list where each element is a list
                                 [product_name (str), price (int/float)].

        Returns:
            list: The sorted list of products.
        """
    # We use the 'sorted()' function with a lambda function for the key.
    # lambda item: item[1] tells Python to use the element at index 1 (the price)
    # for comparison.
    # reverse=True ensures the order is descending (highest price first).
    sorted_list = sorted(
        product_list,
        key=lambda item: item[1],
        reverse=True
    )
    return sorted_list


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
        group_discount = ""
        for sku, items in group_items.items():
            # print(sku, items)
            if sku in DISCOUNTED_PRODUCTS['BUY_ANY_OF']:
                group_discount += group_items[sku]
            else:
                total += self.calculate_total(sku, items)
        if group_discount:
            total += self.calculate_total_group_discount(group_discount)

        return total



    def calculate_total(self, sku, items):
        """
        Calculate the total price of a group of items.
        """

        if sku not in GOODS:
            return -1
        offer = GOODS[sku].offer
        if offer:
            if sku in DISCOUNTED_PRODUCTS['BUY_MULTIPLE_PAY_LESS']:
                total = calculate_total_multiple_offers(sku, offer, items)
            else:
                total, _, _ = calculate_total_single_offer(sku, offer, items)

        else:
            total = GOODS[sku].price * len(items)
        return total

    def calculate_total_group_discount(self, group_discount):
        group_discount = sort_descending_by_price(group_discount)
        nb_groups_of_three = len(group_discount)//3
        total = nb_groups_of_three * 45
        remainder = len(group_discount) % 3
        remaining_items = group_discount[:remainder]
        for sku in remaining_items:
            if sku in GOODS:
                total += GOODS[sku].price
        return total




