""" generate a grayscale hex string from a base 10 int from 0 to 255 incl. """


def generate_grayscale_hex(num: int) -> str:
    """ generate a grayscale hex string from a base 10 int from 0 to 255 incl. """

    def get_hex_str_aux(number: int) -> str:
        """ auxiliary function to generate convert int to hex string, accounting for single digit hex"""
        hex_str = str(hex(number))[2:]

        if len(hex_str) == 1:
            hex_str = '0' + hex_str

        return hex_str

    if 0 <= num <= 255:
        grayscale_hex_string = "#" + get_hex_str_aux(num) * 3
    else:
        raise Exception("generate_grayscale_hex error: input must be between 0 and 255")
    return grayscale_hex_string


if __name__ == '__main__':
    """unit test for generate_grayscale_hex.py"""
    print("hex string for generate_grayscale_hex(20) is: " + generate_grayscale_hex(20))
    print("hex string for generate_grayscale_hex(0) is: " + generate_grayscale_hex(0))
    print("hex string for generate_grayscale_hex(255) is: " + generate_grayscale_hex(255))
    print("hex string for generate_grayscale_hex(-1) is: " + generate_grayscale_hex(-1))
