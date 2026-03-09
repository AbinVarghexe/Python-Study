def is_palindrome(text):
    """Check whether a string reads the same forward and backward."""
    return text == text[::-1]


def is_symmetrical(text):
    """Check whether both halves of the string are the same."""
    mid = len(text) // 2

    if len(text) % 2 == 0:
        return text[:mid] == text[mid:]

    return text[:mid] == text[mid + 1:]


def main():
    value = input("Enter the string: ")

    if is_palindrome(value):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    if is_symmetrical(value):
        print("The string is symmetrical.")
    else:
        print("The string is not symmetrical.")


if __name__ == "__main__":
    main()