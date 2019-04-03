import Product, random

class Store: 

    def __init__(self, name = ""):
        self.name = name
        self.product_list = []

    def add_product(self, new_product = Product.Products()):
        self.product_list.append(new_product)
        print("{} added to the store!".format(new_product))
        return self

    def sell_product(self, id = 0):
        print("Selling {}".format(self.product_list[id].name))
        del self.product_list[id]
        return self
    
    def inflation(self, percent_increase):
        for i in range(len(self.product_list)):
            print(f"Inflating price for {self.product_list[i].name} from {self.product_list[i].price}")
            self.product_list[i].update_price(percent_increase)
            print(f'To {self.product_list[i].price}')
    
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.product_list)):
            print(f'Clearance set for: {category}')
            if(self.product_list[i].category == category):
                print(f'Decreasing price for {self.product_list[i].name} from {self.product_list[i].price}')
                self.product_list[i].update_price(percent_discount,False)
                print(f'To {self.product_list[i].price}')
        return self

    def create_id(self):
        new_id = int(random.random() * 999)
        return new_id

    def id_check_unique(self, new_id):
        for i in range(len(self.product_list)):
            #check if new_id is equal to any product ids
            if(new_id == self.product_list[i].product_id):
                #if true, generate a new random number for new_id
                new_id = int(random.random()*999)
                self.id_check_unique(new_id)  #after each new number is generated, run lines 48-52
                #if false do nothing

        return new_id
    
my_store = Store()

my_store.add_product(Product.Products('item 1',5,'milk', my_store.id_check_unique(my_store.create_id())))
my_store.product_list[0].print_info()
my_store.add_product(Product.Products('item 2',10,'eggs', my_store.id_check_unique(my_store.create_id())))
my_store.product_list[1].print_info()
my_store.add_product(Product.Products('item 2',15,'apple', my_store.id_check_unique(my_store.create_id())))
my_store.product_list[2].print_info()

my_store.sell_product()

my_store.inflation(.2)

my_store.set_clearance('thing',.2)
