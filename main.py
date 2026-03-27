from controller.auth_controller import AuthController
from controller.customer_controller import CustomerController
from controller.farmer_controller import FarmerController
from models.farmer import Farmer
from models.customer import Customer

class AuctionPlatform:
    def __init__(self):
        self.auth=AuthController()
        self.customer=CustomerController()
        self.farmer=FarmerController()

    def run(self):
        while True:
            if AuthController.current_user is None:
                self.auth.show_menu()
            else:
                #if AuthController.role=='farmer'
                if isinstance(AuthController.current_user, Farmer):
                    self.farmer.show_menu()
                #elif AuthController.role=='customer':
                elif isinstance(AuthController.current_user, Customer):
                    self.customer.show_menu()
if __name__ == "__main__":
    platform=AuctionPlatform()
    platform.run()