from views.base_views import Views


class FarmerViews(Views):
    def show_menu(self):
        print('1.Create Bid')
        print('2.View all Bids')
        print('3.Close Bid')
        print('4.View Products')
        print('5.View All Bids')
        print('0.Logout')

    def get_menu_option(self):
        return self.read_int("Enter the option: ", {0, 1, 2, 3, 4, 5})

    @staticmethod
    def show_products(products):
        print(f"{'PROD ID':<7} {'PRODUCT NAME':<20}")
        for key, value in products.items():
            print(f"{key:<7} {value:<20}")

    def get_new_bid_input(self):
        prod_id = self.read_int("Enter the prod id: ")
        base_price = self.read_int("Enter the Base Price: ")
        return prod_id, base_price

    @staticmethod
    def show_farmer_bids(bids):
        header = (
            f"{'BID ID':<7} {'PROD ID':<7} {'STATUS':<10} "
            f"{'BASE PRICE':<12} {'PRICE':<8}"
        )
        print(header)
        if len(bids) == 0:
            print("No Bids Present")
            return
        for bid in bids.values():
            row = (
                f"{bid.id:<7} {bid.prod_id:<7} {bid.status:<10} "
                f"{bid.base_price:<12} {bid.price:<8}"
            )
            print(row)

    def get_bid_id_to_close(self):
        return self.read_int("Enter the BID ID: ")

    def get_close_without_sell_choice(self):
        print('1.Cancel without sell')
        print('2.Keep it live')
        return self.read_int("Enter the Option: ", {1, 2})

    @staticmethod
    def show_bid_created():
        print("Bid Create Successfully")

    @staticmethod
    def show_invalid_product_id():
        print("Invalid product id")

    @staticmethod
    def show_bid_not_found():
        print("No Bids Present")

    @staticmethod
    def show_bid_not_cancelled():
        print("Bid not canceled")

    @staticmethod
    def show_bid_closed():
        print('Bid Closed Successfully')

    @staticmethod
    def show_logout_success():
        print("Logged out successfully!")
