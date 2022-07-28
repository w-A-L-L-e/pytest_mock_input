def ask_name():
    name = input("what's your name? ")
    if name=="noah":
        return f"Hallo Noahtje!"
    else:
        return f"hello {name}"

def main():
    print(ask_name())

if __name__ == '__main__':
    main() # pragma: no cover

