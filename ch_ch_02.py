from random import choice


gifts = ["Perfume", "Socks", "Sweater", "Cup", "Hat", "Tea", "Coffe",
         "Clock", "Bag", "Book", "Wallet", "Cream", "Earrings"]


def main():
    print(choose_gifts(gifts))


def choose_gifts(gifts):
    choosen_gifts = []
    while len(choosen_gifts) < 3:
        gift = choice(gifts)
        if gift not in choosen_gifts:
            choosen_gifts.append(gift)
    return choosen_gifts


main()
