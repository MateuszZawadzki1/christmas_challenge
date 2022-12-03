from math import sqrt as sq


warsaw = (1, 1)
paris = (4, 5)
amsterdam = (11, 5)


def main():
    data = set_route(warsaw, paris, amsterdam)
    piwo = fuel(data)
    print(f"Potrzebuje {piwo} litrów paliwka.")


def set_route(first_city, second_city, third_city):
    first_length = sq((second_city[0] - first_city[0])**2 + (second_city[1] - first_city[1])**2)
    second_length = sq((third_city[0] - second_city[0])**2 + (third_city[1] - second_city[1])**2)
    length = first_length + second_length
    return length


def fuel(data):
    amount = data * 2
    return amount


main()
