from views.base_views import Views


class CustomerViews(Views):
    def show_menu(self):
        print("1.View All Bids")
        print("2.Ask Bid")
        print("3.View Won Bids")
        print("0.Logout")

    def get_menu_option(self):
        return self.read_int("Enter the Option: ", {0, 1, 2, 3})

    def get_bid_request_input(self):
        bid_id = self.read_int("Enter the BID ID: ")
        price = self.read_int("Enter the Price: ")
        return bid_id, price

    @staticmethod
    def show_won_bids(won_bids):
        if len(won_bids) == 0:
            print("No wins")
            return

        header = (
            f"{'BID ID':<7} {'FARMER ID':<10} {'PROD ID':<7} "
            f"{'PRODUCT':<12} {'BASE PRICE':<12} {'FINAL PRICE':<12}"
        )
        print(header)
        for obj in won_bids.values():
            row = (
                f"{obj.id:<7} {obj.farm_id:<10} {obj.prod_id:<7} "
                f"{obj.prod_name:<12} {obj.base_price:<12} {obj.price:<12}"
            )
            print(row)

    @staticmethod
    def show_logout_success():
        print("Logged out successfully!")

    @staticmethod
    def show_bid_not_found():
        print("No Bid Present")

    @staticmethod
    def show_bid_not_live():
        print("Bid not in Live")

    @staticmethod
    def show_invalid_bid_price():
        print("Enter the price above current price")

    @staticmethod
    def show_bid_ask_success():
        print("Bid Ask Successfully")
