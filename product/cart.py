from django.conf import settings
from .models import Product


class Cart(object):
    def __init__(self, request):
        # info abt user, browser, etc.
        self.session = request.session
        # 1 checks if session contains an object with the settings ID
        cart = self.session.get(settings.CART_SESSION_ID)

        # 2 if the cart has already been accessed
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        # set variable to object that either matches #1 or #2 cart event above
        self.cart = cart

    # get info by iter through cart
    def __iter__(self):
        # loop through products
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)  # get info from db, insert to ['product'] variable

        for item in self.cart.values():
            item['total_price'] = int(item['product'].price * item['quantity']) / 100  # remember its in cents

            yield item  # calculate

    # overrides length function in python
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # session is tied to the cart, server knows smt is happening so calculations happen in the bg
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)  # id is key in session

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': int(quantity), 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)  # increments quantity by int quantity

        self.save()  # and redirect to front page

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        return int(sum(item['product'].price * item['quantity'] for item in self.cart.values())) / 100
