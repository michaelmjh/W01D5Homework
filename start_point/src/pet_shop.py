# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash_value):
    pet_shop["admin"]["total_cash"] += cash_value
    return pet_shop["admin"]["total_cash"]


def pets_sold(pet_shop):
    