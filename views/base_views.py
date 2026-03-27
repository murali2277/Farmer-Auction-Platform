from abc import ABC, abstractmethod


class Views(ABC):
    @abstractmethod
    def show_menu(self):
        pass

    @staticmethod
    def read_int(prompt, valid_options=None):
        while True:
            value = input(prompt).strip()
            if not value.isdigit():
                print("Please enter a valid number.")
                continue

            option = int(value)
            if valid_options is not None and option not in valid_options:
                print("Please choose a valid option from the menu.")
                continue

            return option

    @staticmethod
    def show_all_bids(bids):
        header = (
            f"{'BID ID':<7} {'PROD ID':<7} {'STATUS':<10} "
            f"{'BASE PRICE':<12} {'PRICE':<8}"
        )
        print(header)
        if len(bids) == 0:
            print("No Bids")
            return

        for obj in bids.values():
            row = (
                f"{obj.id:<7} {obj.prod_id:<7} {obj.status:<10} "
                f"{obj.base_price:<12} {obj.price:<8}"
            )
            print(row)
