from models.user import User

class Farmer(User):
    all_farmers={}
    def __init__(self):
        super().__init__('MMK')
        self.bids={}
        self.all_farmers[self._id]=self
        self.products={
            1:'Wheat',
            2:'Rice',
            3:'Sugarcane',
            4:'Cotton',
            5:'Maize'
        }
        Farmer.all_farmers[self._id]=self