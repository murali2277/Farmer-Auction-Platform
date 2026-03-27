class Bids:
    __next_id=1
    all_bids={}
    def __init__(self,farm_id,prod_id,price,prod_name):
        self.id=Bids.__next_id
        self.farm_id=farm_id
        self.prod_id=prod_id
        self.prod_name=prod_name
        self.cust_id=None
        self.status='Live'
        self.base_price=price
        self.price=price
        Bids.all_bids[self.id]=self