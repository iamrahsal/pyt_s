#python program count every letters from a string

def countLetters():
    the_string = input("Please enter a string: ")
    simplified_string = "".join(dict.fromkeys(the_string))
    for i in simplified_string:
        print(i, "=", the_string.count(i))

if __name__ == "__main__":
    countLetters()
