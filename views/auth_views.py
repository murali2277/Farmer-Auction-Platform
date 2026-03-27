class AuthViews:
    @staticmethod
    def show_menu():
        print('1.Farmer')
        print('2.Customer')
        print('3.Exit')

    @staticmethod
    def get_menu_option():
        value = input("Enter the option: ").strip()
        while value not in {'1', '2', '3'}:
            print("Please choose 1, 2 or 3.")
            value = input("Enter the option: ").strip()
        return int(value)

    @staticmethod
    def show_farmer_login_success():
        print("Farmer logged in successfully!")

    @staticmethod
    def show_customer_login_success():
        print("Customer logged in successfully!")

    @staticmethod
    def show_exit_message():
        print("bye")
