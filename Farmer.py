from Bids import Bids
from Customer import Customer


class Farmer:
    __next_id = 1

    def __init__(self):
        self.id = Farmer.__next_id
        self.name = "MK"
        self.products = {1: "PRODUCT1", 2: "PRODUCT2", 3: "PRODUCT3"}
        self.bids = {}
        Farmer.__next_id += 1

    def create_bid(self):
        self.view_products()
        prod_id = int(input("Enter the ID: "))
        base_price = int(input("Enter the Base Price: "))
        if prod_id in self.products:
            new_bid = Bids(self.id, prod_id, base_price)
            self.bids[new_bid.id] = new_bid
            print("Bid Create Successfully")
        else:
            print("Choose the correct BID ID")

    def view_products(self):
        if len(self.products) == 0:
            print("No Products")
        else:
            for key, value in self.products.items():
                print(f"{key} {value}")

    def view_bids(self):
        if len(self.bids) == 0:
            print("No bids")
        else:
            for bid in self.bids.values():
                print(f"{bid.id} {bid.prod_id} {bid.status}")

    def close_bid(self):
        self.view_bids()
        bid_id = int(input("Enter the Bid ID: "))
        if bid_id not in self.bids:
            print("No Bid in Live for this BID ID")
            return
        else:
            product = self.bids[bid_id]
            cust_id = product.customer_id
            if cust_id is None:
                print("No Customer has placed the bid")
                option = int(
                    input(
                        "Enter 1 to close the bid without selling the product or 0 to keep the bid live: "
                    )
                )
                if option == 1:
                    del self.products[product.prod_id]
                    del self.bids[bid_id]
                    print("Bid closed successfully")
                elif option == 0:
                    product.status = "Cancelled"
                    print("Bid is live now")
            else:
                product.status = "Completed"
                customer = Customer.all_customer[cust_id]
                customer.won[bid_id] = product
                del self.products[product.prod_id]
                del self.bids[bid_id]
                print("Bid closed successfully")

    def view_all_bids(self):
        Bids.view_all_bids()
