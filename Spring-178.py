# Author Jurijus Pacalovas
# Function to reverse specific bit patterns during compression and extraction
def reverse_bits(data):
    # Bit pattern replacements
    replacements = {
        b'000000000': b'111001101',
        b'111001101': b'000000000',
        b'01011': b'11111',
        b'00000': b'01100',
        b'00001': b'01101',
        b'00010': b'01110',
        b'00011': b'01111',
        b'00100': b'11100',
        b'11111': b'01011',
        b'01100': b'00000',
        b'01101': b'00001',
        b'01110': b'00010',
        b'11100': b'00011',
        b'10': b'11',
        b'00': b'10',
        b'01': b'00',
        b'10': b'00',
    }

    for pattern, replacement in replacements.items():
        data = data.replace(pattern, replacement)

    return data

# Function to perform bit replacements based on the specified steps
def perform_bit_replacements(data, num_bits, num_steps, delete=True):
    for step in range(num_steps):
        for i in range(num_bits):
            bit_value = '0' if delete else '1'
            data = data.replace(bytes(str((2 ** (23 + step)) // 2 + i), 'utf-8'), bytes(bit_value, 'utf-8'))
            data = data.replace(bytes(str((2 ** (23 + step)) // 2 - i), 'utf-8'), bytes(bit_value, 'utf-8'))
        delete = not delete  # Alternate between deleting and adding
    return data

# Function to find Pythagorean triples
def find_pythagorean_triples(limit):
    d = 2
    e = 2
    f = 1
    g = 1
    triples = []
    for a in range(1, limit - f):
        for b in range(a, limit + g):
            c = (a ** d + b ** e)
            f += 1
            g += 1
            d += 1
            e += 1
            if isinstance(c, float) and c.is_integer():
                triples.append((a, b, int(c)))
    return triples

# Function to convert Pythagorean triples to binary data
def triples_to_binary(triples):
    binary_data = b''
    for triple in triples:
        for component in triple:
            if 0 <= component <= 255:
                binary_data += bytes([component])
            else:
                raise ValueError("Triple component out of the valid byte range (0-255)")
    return binary_data

# Function to convert binary data to Pythagorean triples
def binary_to_triples(binary_data):
    triples = []
    current_triple = []

    for value in binary_data:
        current_triple.append(value)
        if len(current_triple) == 3:
            triples.append(tuple(current_triple))
            current_triple = []

    return triples

# Initialize the 'triples' variable to an empty list
triples = []

# Ask the user for options
print("Options:")
print("1. Compression and Save")
print("2. Extraction and Save")
option = input("Select an option (1 or 2): ")

if option == "1":
    # Compression and Save
    input_file_name = input("Enter the name of the input file for compression: ")
    output_file_name = input("Enter the name of the output file for saving compressed data: ")

    try:
        with open(input_file_name, 'rb') as input_file:
            input_data = input_file.read()

        # Reverse the first 512 bits
        input_data = reverse_bits(input_data[:512]) + input_data[512:]

        # Set the limit for finding Pythagorean triples to 7
        limit = 7  # Adjust the limit as needed

        # Step 1: Find Pythagorean triples within the specified limit
        triples = find_pythagorean_triples(limit)

        # Step 2: Convert Pythagorean triples to binary data
        binary_data = triples_to_binary(triples)

        # Step 3: Append binary data to the original input data
        input_data += binary_data

        # Perform bit replacements for 100 steps, alternating between deleting and adding
        num_bits = 23
        num_steps = 100
        input_data = perform_bit_replacements(input_data, num_bits, num_steps)

        # Step 4: Save the combined data to the specified file in binary mode ('wb')
        with open(output_file_name, 'wb') as compressed_file:
            compressed_file.write(input_data)

        print(f"Data successfully compressed and saved to '{output_file_name}'.")
    except FileNotFoundError:
        print(f"Error: File not found.")

elif option == "2":
    # Extraction and Save
    input_file_name = input("Enter the name of the input compressed file for extraction: ")
    output_file_name = input("Enter the name of the output file for saving extracted data: ") + ".bin"

    try:
        with open(input_file_name, 'rb') as input_file:
            paq_compressed_data = input_file.read()

        # Step 1: Decompress the Paq compressed data
        decompressed_data = paq_compressed_data

        # Reverse the first 512 bits
        decompressed_data = reverse_bits(decompressed_data[:512]) + decompressed_data[512:]

        # Set the limit for finding Pythagorean triples to 7
        limit = 7  # Adjust the limit as needed

        # Step 3: Find binary data that represents Pythagorean triples
       
        binary_data = decompressed_data[-(len(triples) * 3):]  # Assuming each triple is 3 bytes

        # Perform bit replacements for 100 steps, alternating between deleting and adding
        num_bits = 23
        num_steps = 100
        binary_data = perform_bit_replacements(binary_data, num_bits, num_steps)

        # Step 4: Convert binary data back to Pythagorean triples
        extracted_triples = binary_to_triples(binary_data)

        # Step 5: Save the extracted data to the specified file in binary mode ('wb')
        with open(output_file_name, 'wb') as extracted_file:
            extracted_file.write(binary_data)

        print(f"Data successfully extracted and saved to '{output_file_name}'.")
    except FileNotFoundError:
        print(f"Error: File not found.")
else:
    print("Invalid option. Please select 1 for Compression and Save or 2 for Extraction and Save.")
