from views.farmer_views import FarmerViews
from controller.auth_controller import AuthController
from models.bids import Bids
from models.customer import Customer


class FarmerController:
    def __init__(self):
        self.farmer_views = FarmerViews()

    def show_menu(self):
        self.farmer_views.show_menu()
        option = self.farmer_views.get_menu_option()
        if option == 1:
            self.create_bid()
        elif option == 2:
            self.view_bids()
        elif option == 3:
            self.close_bids()
        elif option == 4:
            self.view_products()
        elif option == 5:
            self.view_all_bids()
        elif option == 0:
            AuthController.current_user = None
            self.farmer_views.show_logout_success()

    def view_bids(self):
        self.farmer_views.show_farmer_bids(AuthController.current_user.bids)

    def create_bid(self):
        self.view_products()
        prod_id, base_price = self.farmer_views.get_new_bid_input()
        current_user = AuthController.current_user

        if prod_id not in current_user.products:
            self.farmer_views.show_invalid_product_id()
            return

        new_bid = Bids(
            current_user.id,
            prod_id,
            base_price,
            current_user.products[prod_id],
        )
        current_user.bids[new_bid.id] = new_bid
        self.farmer_views.show_bid_created()

    def view_products(self):
        self.farmer_views.show_products(AuthController.current_user.products)

    def view_all_bids(self):
        self.farmer_views.show_all_bids(Bids.all_bids)

    def close_bids(self):
        self.view_bids()
        user = AuthController.current_user
        bid_id = self.farmer_views.get_bid_id_to_close()
        if bid_id not in user.bids:
            self.farmer_views.show_bid_not_found()
            return

        bid = user.bids[bid_id]
        if bid.cust_id is None:
            option = self.farmer_views.get_close_without_sell_choice()
            if option == 1:
                bid.status = 'Cancel'
            else:
                self.farmer_views.show_bid_not_cancelled()
            return

        bid.status = 'Finished'
        Customer.all_customer[bid.cust_id].won[bid.id] = bid
        del Bids.all_bids[bid_id]
        del user.products[bid.prod_id]
        del user.bids[bid_id]
        self.farmer_views.show_bid_closed()
