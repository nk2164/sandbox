def encode_data(data):
    # Check that the input data is 7 characters long
    if len(data) != 7:
        return None

    # Convert the input data to ASCII values
    ascii_values = [ord(c) for c in data]

    # Check that each character is either an uppercase letter or a digit
    for ascii_value in ascii_values:
        if not (48 <= ascii_value <= 57 or 65 <= ascii_value <= 90):
            return None

    # Split the data into 3 bytes
    byte1 = (ascii_values[0] & 31) << 11 | (ascii_values[1] & 31) << 6
    byte2 = (ascii_values[1] & 96) >> 5 | (ascii_values[2] & 31) << 11 | (ascii_values[3] & 31) << 6
    byte3 = (ascii_values[3] & 96) >> 5 | (ascii_values[4] & 31) << 11 | (ascii_values[5] & 31) << 6 | (ascii_values[6] & 15)

    return byte1.to_bytes(2, 'big') + byte2.to_bytes(2, 'big') + byte3.to_bytes(2, 'big')

def decode_data(bytes):
    # Check that the input data is 3 bytes long
    if len(bytes) != 3:
        return None

    # Split the 3 bytes into integers
    byte1, byte2, byte3 = int.from_bytes(bytes[:2], 'big'), int.from_bytes(bytes[2:4], 'big'), int.from_bytes(bytes[4:], 'big')

    # Decode the data
    ascii_values = [
        (byte1 & 63488) >> 11,
        ((byte1 & 2016) >> 6) | ((byte2 & 61440) >> 11),
        (byte2 & 2016) >> 6,
        (byte2 & 63) << 5 | ((byte3 & 63488) >> 11),
        (byte3 & 2016) >> 6,
        (byte3 & 63) << 5 | (byte3 & 15),
        0
    ]

    # Convert the ASCII values to characters
    data = ''.join([chr(ascii_value) for ascii_value in ascii_values])

    return data

print(encode_data('A12BCD7'))
print(decode_data(encode_data('A12BCD7')))