from collections import defaultdict


class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        group_items = defaultdict(str)
        if not skus:
            raise ValueError("Please provide skus")
        skus = skus.upper()
        for sku in skus:
            group_items[sku] += sku
        return len(group_items)
