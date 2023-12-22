def main():
    # promt the user to input a text
    text = list(input("Text: ").lower().strip())
    text.append(" ")
    if text == "":
        return 0

    # initialize count numbers of words, sentences, and letters
    letter_counter = 0
    word_counter = 0
    sentence_counter = 0

    # count letters, words, and sentences
    for letter in text:
        if letter.isalpha():
            letter_counter += 1
        elif letter == " ":
            word_counter += 1
        elif letter == "!" or letter == "." or letter == "?":
            sentence_counter += 1

    # find letter average
    letter_average = letter_counter / word_counter * 100

    # find sentence average
    sentence_average = sentence_counter / word_counter * 100

    # use Coleman-Liau index
    index = round(0.0588 * letter_average - 0.296 * sentence_average - 15.8)

    if index >= 16:
        print(f"Grade 16+")
    elif index < 1:
        print(f"Before Grade 1")
    else:
        print(f"Grade {index}")


main()
