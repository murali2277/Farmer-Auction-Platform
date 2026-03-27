from views.auth_views import AuthViews
from models.farmer import Farmer
from models.customer import Customer


class AuthController:
    current_user = None

    # role=None
    def __init__(self):
        self.authview = AuthViews()
        self.farmer = Farmer()
        self.customer = Customer()

    def show_menu(self):
        self.authview.show_menu()
        option = self.authview.get_menu_option()
        if option == 1:
            AuthController.current_user = self.farmer
            self.authview.show_farmer_login_success()
        elif option == 2:
            AuthController.current_user = self.customer
            self.authview.show_customer_login_success()
        elif option == 3:
            self.authview.show_exit_message()
            exit()
