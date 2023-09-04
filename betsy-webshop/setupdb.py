from models import User, Product, Transaction, Tag, db
import os


def main():
    """Comment out the fuction you are not using and run the file."""
    delete_database()
    setup_data()


def setup_data():
    """Create the database and fill it with data."""
    db.connect()
    db.create_tables([User, Product, Transaction, Tag])

    user_data = [
        ("Mila", "Karspelstraat 5", "Nijmegen", 24758221197),
        ("Noah", "Steenbakkersweg 26", "Hoogwoud", 24758221197),
        ("Lucas", "Schiphorsterweg 80", "Waardenburg", 64167079086),
        ("Emma", "Haagweg 7", "Leimuiderbrug", 88861775361),
        ("Julia", "Leuvensbroek 91", "Apeldoorn", 27736399773),
        ("James", "Clematisstraat 41", "Leiden", 67943295160),
        ("Olivia", "Weezenhof 42", "Katwijk", 85064187673),
        ("Sem", "Tricotstraat 46", "Beert", 50955049913),
        ("Daan", "Vlinderweg 81", "Boerakker", 47307924781),
        ("Zoë", "Malvert 88", "Almere", 36735847613),
        ("Levi", "Kaard 123", "Maarssen", 71813928542),
        ("Luca", "Rigel 108", "Spierdijk", 17530743579),
        ("Nora", "Verlengde Oosterdiep OZ 120", "Terband", 14872956212),
        ("Anna", "Wilgeboorderweg 54", "Oudehaske", 32061686450),
        ("Finn", "Heibloem 79", "Spanbroek", 69514650892),
        ("Milou", "Baanbergenweg 59", "Heiloo", 80662480799),
        ("Adam", "Middenhof 90", "Amsterdam", 39592645922),
        ("Sam", "Tjalk 125", "Tilburg", 68430158808),
        ("Sophie", "Velserhooftlaan 125", "Blaricum", 11406891118),
        ("Saar", "Utrechtseweg 90", "Vught", 24333751229),
    ]

    product_data = [
        ("herenfiets", "framemaat 61", 350, 1, 9),
        ("vogelkooi", "voor 1 grote of 2 kleine vogels", 25, 1, 3),
        ("televisie", "2 jaar oud", 500, 1, 1),
        ("kookboeken", "van Jamie Oliver", 8, 4, 18),
        ("knuffelbeest", "hele mooie Elmo", 7.50, 1, 8),
        ("legkippen", "lekkere eieren", 10, 4, 4),
        ("airpods", "weinig gebruikt", 45, 1, 5),
        ("volkswagen golf", "auto is van een oud vrouwtje geweest", 2500, 1, 15),
        ("zaklantaarn", "doet 't altijd", 12.50, 1, 12),
        ("vouwwagen", "Trigano, 2007", 2100, 1, 14),
        ("lego kasteel", "compleet met boekje", 50, 1, 17),
        ("theeservies", "antiek, van porselein", 350, 1, 11),
        ("CD Frans Bauer", "kan 'm niet meer horen", 4.50, 1, 1),
        ("damesbroek", "maat 38", 20, 1, 7),
        ("schilderij", "stilleven met fruit", 295, 1, 2),
        ("playstation 4", "doet 't nog prima", 240, 1, 6),
        ("monopolyspel", "de originele versie", 20, 1, 16),
        ("DVD Titanic", "", 7.50, 1, 10),
        ("2 concertkaartjes Iron Maiden", "voor aanstaande vrijdag", 160, 1, 19),
        ("2 tickets sauna", "voor de Zwaluwhoeve", 40, 1, 3),
        ("openhaardhout", "per zak van 20kg", 12.50, 15, 9),
        ("boormachine", "heb nieuwe gekocht", 75, 1, 17),
        ("verrekijker", "voor de natuurliefhebber", 60, 1, 15),
        ("akoustische gitaar", "wel een beetje vals", 95, 1, 6),
        ("sportschoenen", "1 paar Nikes, maat 41", 25, 1, 14),
        ("kinderjurk", "mooi jurkje", 30, 1, 11),
        ("buitenzwembad", "diameter 2,5m", 111, 1, 17),
        ("parasol", "wel een beetje oud", 15, 1, 4),
        ("misdaadroman", "verschillende, van Baantjer", 1, 16, 18),
        ("zonnebril", "nog nieuw in doos", 100, 1, 13),
        ("wandklok", "van Annemiekes A-lunch", 19.95, 1, 11),
        ("GRATIS tuintegels", "30x30, 74 stuks", 0, 1, 6),
        ("bankstel", "2-zits, leer", 295, 1, 5),
        ("keyboard", "met standaard", 40, 1, 7),
        ("airfryer", "Philips, werkt prima", 45, 1, 15),
        ("kaart Amsterdam anno 1700", "ZELDZAAM item!", 4750, 1, 20),
        ("voetbal", "gekregen, maar ik voetbal niet", 8, 1, 10),
        ("tennisracket", "gebruikt", 12.50, 1, 6),
    ]

    tag_data = [
        {
            "electronica": [
                "machine",
                "televisie",
                "airfryer",
                "klok",
                "airpod",
                "playstation",
                "zaklantaarn",
            ]
        },
        {
            "sport": [
                "bal",
                "tennis",
                "hockey",
                "judo",
                "zwemmen",
                "boksen",
                "bat",
                "ping-pong",
            ]
        },
        {
            "muziek": [
                "gitaar",
                "keyboard",
                "microfoon",
                "drumstel",
                "basgitaar",
                "bladmuziek",
            ]
        },
        {
            "meubels": [
                "bankstel",
                "stoel",
                "lamp",
                "dressoir",
                "meubel",
                "tafel",
                "fauteuil",
            ]
        },
        {"lezen": ["boek", "strip", "roman", "biografie", "handleiding"]},
        {
            "kleding": [
                "shirt",
                "broek",
                "jurk",
                "rok",
                "jas",
                "kleding",
                "pantalon",
                "schoen",
            ]
        },
        {
            "vrije tijd": [
                "bioscoop",
                "sauna",
                "concert",
                "attractiepark",
                "spel",
                "dagje weg",
                "creatief",
            ]
        },
        {
            "huisdieren": [
                "hond",
                "kat",
                "poes",
                "vogel",
                "kip",
                "cavia",
                "rat",
                "leguaan",
            ]
        },
        {
            "tuin": [
                "boom",
                "plant",
                "bloem",
                "tegel",
                "parasol",
                "potgrond",
                "zwembad",
                "hout",
            ]
        },
        {
            "kunst": [
                "schilderij",
                "beeld",
                "muziek",
                "foto",
                "video",
                "museum",
                "geschiedenis",
            ]
        },
        {
            "entertainment": [
                "DVD",
                "CD",
                "muziek",
                "film",
                "show",
                "boek",
                "televisie",
                "radio",
            ]
        },
        {
            "vervoer": [
                "fiets",
                "step",
                "scooter",
                "auto",
                "wagen",
                "trein",
                "vliegtuig",
                "bus",
                "ov",
            ]
        },
        {"lifestyle": ["horloge", "zonnebril", "sieraad"]},
        {"hobby": ["lego", "game", "koken", "spel", "tuin", "boek", "foto"]},
        {
            "gaming": [
                "playstation",
                "Wii",
                "xbox",
                "pc",
                "gameboy",
                "nintendo",
                "atari",
            ]
        },
        {
            "kamperen": [
                "caravan",
                "vouwwagen",
                "camper",
                "camping",
                "zaklantaarn",
                "verrekijker",
                "vissen",
            ]
        },
        {
            "verzamelen": [
                "kaart",
                "postzegel",
                "servies",
                "bierviltje",
                "lego",
                "munt",
                "collectie",
            ]
        },
        {
            "kinderen": [
                "lego",
                "playmobil",
                "knuffel",
                "strip",
                "spel",
                "game",
                "barbie",
            ]
        },
    ]

    transaction_data = []

    for data in transaction_data:
        data = Transaction.create(
            purchaser=data[0], seller=data[1], product=data[2], quantity=data[3]
        )

    for data in user_data:
        data = User.create(
            name=data[0], adress=data[1], city=data[2], billing_info=data[3]
        )

    for data in product_data:
        data = Product.create(
            name=data[0],
            description=data[1],
            price_per_unit=data[2],
            quantity=data[3],
            owner=data[4],
        )

    query = Product.select()
    product_names = [product.name for product in query]

    for product_name in product_names:
        keys = []
        for tag_dict in tag_data:
            for tag_key, tag_values in tag_dict.items():
                for value in tag_values:
                    if value in product_name:
                        keys.append(tag_key)
        data = Tag.create(product_name=product_name, tag=", ".join(keys))


def delete_database():
    """Delete the database."""
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "webshop.db")
    if os.path.exists(database_path):
        os.remove(database_path)


if __name__ == "__main__":
    main()
