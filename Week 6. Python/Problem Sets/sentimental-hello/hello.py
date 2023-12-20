def main():
    try:
        name = input("What is your name?: ")
        print(f"Hello, {name}")
    except EOFError:
        exit()
    print()


main()
