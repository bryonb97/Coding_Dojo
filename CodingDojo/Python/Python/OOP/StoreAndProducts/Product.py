class Products:
    def __init__(self, name = "", price = 0, category = "", product_id = 0):
        self.name = name
        self.price = price
        self.category = category
        self.product_id = product_id

    def update_price(self, percent_change = 0, is_increased = False):
        price_change = self.price + (percent_change * self.price)
        if(is_increased):
            self.price += price_change
        else:
            self.price -= price_change
        return self
    
    def print_info(self):
        print(f"************************************\nName: {self.name}\nCategory: {self.category}\nPrice: {self.price}\nProduct-ID: {self.product_id}\n************************************\n")


