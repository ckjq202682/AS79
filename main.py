# AS79

vowels = ["a", "e", "i", "o", "u"]


def make_it_laugh(string):
    for i in range(0, len(string)):
        if string[i] in vowels:
            string[i] = "haha"
    return string


string = list(input("Input string"))

print("".join(string))
print("".join(make_it_laugh(string)))
