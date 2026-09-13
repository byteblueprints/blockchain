def get_message_input(prompt: str = "Enter message: "):
    """
    Step 1: Get the input message for SHA-512 processing.
    Prompts the user for a message, converts it to ASCII values and bits.
    """
    message = input(prompt)
    ascii_values = [ord(char) for char in message]
    bits = ''.join(format(value, '08b') for value in ascii_values)

    print(f"1. Message : {message}")
    print(f"2. Input: {message}")
    print(f"3. ASCII: {ascii_values}")
    print(f"4. Bits: {bits}")

    return message, ascii_values, bits


if __name__ == "__main__":
    get_message_input()
