class Bids:
    next_id=1
    all_bids={}
    def __init__(self,farm_id,prod_id,base_price):
        self.id=Bids.next_id
        self.farm_id=farm_id
        self.prod_id=prod_id
        self.status='Live'
        self.base_price=base_price
        self.price=base_price
        Bids.all_bids[self.id]=self
        Bids.next_id+=1
        self.customer_id=None

    def view_all_bids():
        if len(Bids.all_bids)==0:
            print("No Bids")
        else:
            print(f"{'BID ID':<5} {'FARM ID':<5} {'PROD ID':<5} {'STATUS':<5} {'BASE PRICE':<5} {'CURRENT PRICE'}")
            for obj in Bids.all_bids.values():
                print(f"\n{obj.id:<5} {obj.farm_id:<5} {obj.prod_id:<5} {obj.status:<5} {obj.base_price:<5} {obj.price:<5}")