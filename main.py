from Farmer import Farmer
from Company import Company
from Customer import Customer
from views import Views


class AuctionApplication:
    def __init__(self):
        self.current_user = None
        self.customer = Customer()
        self.company = Company()
        self.farmer = Farmer()

    def run(self):
        while True:
            if self.current_user is None:
                Views.choose_menu()
                option = int(input("Enter the Option: "))
                if option == 1:
                    self.current_user = self.farmer
                elif option == 2:
                    self.current_user = self.customer
                elif option == 3:
                    self.current_user = self.company
                elif option == 0:
                    print("Exited")
                    break
            elif isinstance(self.current_user, Farmer):
                Views.farmer_menu()
                option = int(input("Enter the option: "))
                if option == 1:
                    self.current_user.create_bid()
                elif option == 2:
                    self.current_user.view_bids()
                elif option == 3:
                    self.current_user.close_bid()
                elif option == 4:
                    self.current_user.view_all_bids()
                elif option == 0:
                    self.current_user = None
            elif isinstance(self.current_user, Customer):
                Views.customer_menu()
                option = int(input("Enter the option: "))
                if option == 1:
                    self.current_user.view_all_bids()
                elif option == 2:
                    self.current_user.ask_bid()
                elif option == 3:
                    self.current_user.view_won_bids()
                elif option == 0:
                    print("Logout Successfully")
                    self.current_user = None


if __name__ == "__main__":
    app = AuctionApplication()
    app.run()
