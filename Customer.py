from Bids import Bids


class Customer:
    __next_id = 1
    all_customer = {}

    def __init__(self):
        self.id = Customer.__next_id
        Customer.__next_id += 1
        self.name = "MMK"
        self.won = {}
        Customer.all_customer[self.id] = self

    def view_all_bids(self):
        Bids.view_all_bids()

    def ask_bid(self):
        self.view_all_bids()
        bid_id = int(input("Enter the BID ID: "))
        price = int(input("Enter the price: "))
        if bid_id in Bids.all_bids:
            bid = Bids.all_bids[bid_id]
            if price > bid.price:
                bid.price = price
                bid.customer_id = self.id
            else:
                print("Enter the correct bid price")
        else:
            print("Enter the correct BID ID")

    def view_won_bids(self):
        if len(self.won) == 0:
            print("No won bids")
        else:
            print(
                f"{'BID ID':<5} {'PROD ID':<5} {'BASE PRICE':<5} {'CURRENT PRICE':<5}"
            )
            for bid in self.won.values():
                print(
                    f"{bid.id:<5} {bid.prod_id:<5} {bid.base_price:<5} {bid.price:<5}"
                )
