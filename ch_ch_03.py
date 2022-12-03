def main():
    height = int(input("Jaką byś chciał wysokość choinki: "))
    christmas_tree(height)


def christmas_tree(height):
    empty_character = height
    character = 0
    for _ in range(height):
        print(empty_character * ' ', character * '*' + '*' + character * '*', )
        empty_character -= 1
        character += 1
    print(height * ' ' + '||')


main()
