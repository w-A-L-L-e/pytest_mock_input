import random
def ask_name():
    name = input("what's your name? ")
    if name=="noah":
        return f"Hallo Noahtje!"
    else:
        return f"hello {name}"

def main():
    print(ask_name())
    dice_result = random.randint(1,6)
    print(f"your dice throw = {dice_result}")


if __name__ == '__main__':
    main() # pragma: no cover

