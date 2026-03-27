from models.user import User

class Customer(User):
    all_customer={}
    def __init__(self):
        super().__init__('MK')
        self.won={}
        Customer.all_customer[self._id]=self