
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not skus:
            raise ValueError("Please provide skus")
