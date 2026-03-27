from views.customer_views import CustomerViews
from controller.auth_controller import AuthController
from models.bids import Bids


class CustomerController:
    def __init__(self):
        self.custviews = CustomerViews()

    def show_menu(self):
        self.custviews.show_menu()
        option = self.custviews.get_menu_option()
        if option == 1:
            self.view_all_bids()
        elif option == 2:
            self.ask_bid()
        elif option == 3:
            self.view_won_bids()
        elif option == 0:
            AuthController.current_user = None
            self.custviews.show_logout_success()

    def view_all_bids(self):
        self.custviews.show_all_bids(Bids.all_bids)

    def ask_bid(self):
        self.view_all_bids()
        bid_id, price = self.custviews.get_bid_request_input()
        bids = Bids.all_bids
        if bid_id not in bids:
            self.custviews.show_bid_not_found()
            return

        bid = bids[bid_id]
        if bid.status != 'Live':
            self.custviews.show_bid_not_live()
            return

        if price <= bid.price:
            self.custviews.show_invalid_bid_price()
            return

        bid.price = price
        bid.cust_id = AuthController.current_user.id
        self.custviews.show_bid_ask_success()

    def view_won_bids(self):
        user_won = AuthController.current_user.won
        self.custviews.show_won_bids(user_won)
