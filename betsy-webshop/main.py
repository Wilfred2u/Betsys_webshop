from models import User, Product, Transaction, Tag
from peewee import DoesNotExist
import difflib

# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line


def search(term):
    """Search the database for products with a given term."""
    print(f"Searching for products with term '{term}'...\n")

    try:
        # if search-term does exactly match:
        matching_products = (
            Product.select(User, Product)
            .join(User)
            .where((Product.name.contains(term)) | (Product.description.contains(term)))
        )

        list_matching_products = [
            f"- {product.name}\n   {product.description}\n"
            for product in matching_products
        ]

        # if search-term does NOT exactly match
        if list_matching_products == []:
            all_products = Product.select()
            list_all_products = [product.name for product in all_products]

            almost_matching_product = "".join(
                difflib.get_close_matches(term, list_all_products, 1, cutoff=0.75)
            )

            if almost_matching_product:
                almost_matching_products = (
                    Product.select(User, Product)
                    .join(User)
                    .where(
                        (Product.name.contains(almost_matching_product))
                        | (Product.description.contains(almost_matching_product))
                    )
                )

                list_almost_matching_products = [
                    f"- {product.name}\n   {product.description}\n"
                    for product in almost_matching_products
                ]

                list_matching_products = list_almost_matching_products

            # if no match:
            else:
                # Flag: if Error, run except
                list_matching_products[0]

    except IndexError:
        return "Product not found.\n"

    else:
        return f"{''.join(list_matching_products)}"


def list_user_products(user_id):
    """Return a list with all the products of a given user's id."""
    print(f"Listing products for user with ID {user_id}...\n")

    try:
        user = User.get(User.id == user_id)
        products = (
            Product.select()
            .join(User)
            .where((Product.owner == user_id) & (Product.quantity > 0))
        )

        list = [f"- {product.name}\n" for product in products]

    except DoesNotExist:
        return f"ID {user_id} not found.\n"

    else:
        return f"{user.name} owns the following products:\n{''.join(list)}\n"


def list_products_per_tag(tag):
    """Create a list of all the products which match the tag."""
    print(f"Listing products with tag '{tag}'...\n")

    try:
        matching_products = Tag.select(Tag.product_name).where(Tag.tag == tag)

        list_matching_products = [
            f"- {item.product_name}\n" for item in matching_products
        ]

        # if search-term does NOT exactly match
        if list_matching_products == []:
            all_tags = Tag.select()
            list_all_tags = [tag.tag for tag in all_tags]

            almost_matching_tag = "".join(
                difflib.get_close_matches(tag, list_all_tags, 1, cutoff=0.75)
            )

            if almost_matching_tag:
                almost_matching_products = Tag.select(Tag.product_name).where(
                    Tag.tag == almost_matching_tag
                )

                list_almost_matching_products = [
                    f"- {item.product_name}\n" for item in almost_matching_products
                ]

                list_matching_products = list_almost_matching_products

            # if no match:
            else:
                # Flag: if Error, run except
                list_matching_products[0]

    except IndexError:
        return f"Tag '{tag}' not found.\n"

    else:
        return f"Tag '{tag}' matches the following products:\n{''.join(list_matching_products)}\n"


def add_product_to_catalog(user_id, product):
    """Create a new product a user wants to sell."""
    print("Creating new product...\n")

    try:
        user = User.get(User.id == user_id)
        products = (
            Product.select()
            .join(User)
            .where((Product.owner == user_id) & (Product.quantity > 0))
        )

        # Flags: if Error, run except
        product["quantity"] + 1
        product["price"] + 1

        list = ["".join(product.name) for product in products]

        if product["name"] in list:
            return f"{user.name} already owns a {product['name']}. Product has not been added.\n"

        added_product = Product(
            name=product["name"],
            description=product["description"],
            price_per_unit=round(product["price"], 2),
            quantity=product["quantity"],
            owner=user_id,
        )
        added_product.save()

    except DoesNotExist:
        return f"ID {user_id} not found.\n"

    except TypeError:
        try:
            product["quantity"] + 1
            return f"Price: {product['price']}. '{product['price']}' is not an integer. Product has not been added.\n"

        except TypeError:
            return f"Quantity: {product['quantity']}. '{product['quantity']}' is not an integer. Product has not been added.\n"

    else:
        return f"{product['name']} has succesfully been added to {user.name}!\n"


def update_stock(product_id, new_quantity):
    """Update the stock quantity of a product."""
    print("Updating stock...\n")

    try:
        product = Product.get_by_id(product_id)

        # Flag: if Error, run except
        new_quantity + 1

        old_quantity = product.quantity
        product.quantity = new_quantity
        product.save()

    except DoesNotExist:
        return f"ID {product_id} not found.\n"

    except TypeError:
        return f"Quantity: {new_quantity}. '{new_quantity}' is not an integer. Product has not been added.\n"

    else:
        return f"The quantity of {product.name} has been updated. It was {old_quantity} and it's now {product.quantity}.\n"


def remove_product(product_id):
    """remove a product from a user."""

    try:
        product = Product.get_by_id(product_id)
        product.delete_instance()

    except DoesNotExist:
        return f"ID {product_id} not found.\n"

    else:
        return f"Product with ID {product_id} removed.\n"


def fill_transaction_database(purchaser, product, quantity):
    added_product = Transaction(
        purchaser=purchaser.name,
        seller=product.owner.name,
        product=product.name,
        quantity=quantity,
    )
    added_product.save()


def purchase_product(product_id, purchaser_id, quantity):
    """Purchase a product by another user."""

    try:
        product = Product.get_by_id(product_id)
        purchaser = User.get_by_id(purchaser_id)

        # Flag: if Error, run except
        quantity + 1

        if str(product.owner_id) == str(purchaser):
            return f"You can't purchase your own product.\n"
        elif product.quantity < quantity:
            return f"{product.owner.name} only has {product.quantity} {product.name}, so that is not enough.\n"
        else:
            product.quantity -= quantity
            if product.quantity == 0:
                remove_product(product_id)
            product.save()

    except DoesNotExist:
        try:
            purchaser = User.get_by_id(purchaser_id)
            return f"Product with ID {product_id} not found.\n"

        except DoesNotExist:
            return f"User with ID {purchaser_id} not found.\n"

    except TypeError:
        return f"Quantity: {quantity}. {quantity} is not an integer. Product has not been purchased.\n"

    else:
        fill_transaction_database(purchaser, product, quantity)
        return f"{purchaser.name} has purchased {quantity} {product.name} from {product.owner.name}.\n"


def view_all_transactions():
    """View all transactions made by the users."""
    try:
        query = Transaction.select()

        all_transactions = [
            f"purchaser: {item.purchaser}  | seller: {item.seller}  | product: {item.product}  | quantity: {item.quantity}\n"
            for item in query
        ]

        all_transactions[0]

    except:
        return "No transactions have been made. The transaction table is empty.\n"

    else:
        return "".join(all_transactions)


if __name__ == "__main__":
    """Select the function(s) you want to execute."""
    # Querying-the-database functions:
    print(search("zonnebril"))
    print(search("knufelbees"))
    print(search("foo"))

    print(list_user_products(17))
    print(list_user_products(50))

    print(list_products_per_tag("electronica"))
    print(list_products_per_tag("elektronika"))
    print(list_products_per_tag("foo"))

    # Modifying-the-database functions:
    print(purchase_product(5, 9, 1))
    print(purchase_product(3, 16, 1))
    print(purchase_product(10, 2, 1))
    print(purchase_product(34, 14, 1))
    print(purchase_product(7, 5, 1))
    print(purchase_product(1, 8, 3))
    print(purchase_product(1, 8, "1"))

    print(update_stock(9, 3))
    print(update_stock(9, "5"))
    print(update_stock(44, 2))

    print(remove_product(16))
    print(remove_product(80))

    print(
        add_product_to_catalog(
            3,
            {
                "name": "computer",
                "description": "PC uit 2004",
                "price": 25,
                "quantity": 1,
            },
        )
    )
    print(
        add_product_to_catalog(
            3,
            {
                "name": "kaarsen",
                "description": "allerlei soorten",
                "price": 8,
                "quantity": "1",
            },
        )
    )

    print(view_all_transactions())
