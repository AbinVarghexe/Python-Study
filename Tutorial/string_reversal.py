def reverse_string(text):
    """Return the reversed version of the input string."""
    return text[::-1]


def main():
    text = input("Enter a string: ")
    print("Reversed string:", reverse_string(text))


if __name__ == "__main__":
    main()
