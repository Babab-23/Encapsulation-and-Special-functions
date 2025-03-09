class StringReverser:
    @staticmethod
    def reverse_words(s: str) -> str:
        # Split the string into words, reverse the list, and join back into a string
        return ' '.join(s.split()[::-1])

# Example usage:
if __name__ == "__main__":
    s = "Hello World! This is Python."
    reverser = StringReverser()
    print(reverser.reverse_words(s))
