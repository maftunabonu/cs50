def main():
    while True:
        try:
            height = int(input("Height: "))
            if height <= 0 or height > 8:
                raise Exception()
            break
        except ValueError:
            print("Enter a number!!!")
            pass
        except Exception:
            print("Please, enter a number between 1 and 8")
            pass

    # building walls
    counter = 1
    while counter <= height:
        print(" " * (height - counter) + "#" * counter + "  " + "#" * counter)
        counter += 1


main()
