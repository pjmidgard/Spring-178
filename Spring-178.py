import paq

X = 0
Z = 0
Number_of_the_file = 0
y = 0
Add = 0
T_Real = 0
Divided_coordinates = 1
number_of_file = 10  # Replace with your desired value

# Ask the user for extraction option (1 or 2)
extract_option = input("Enter '1' for one type of extraction or '2' for another type: ")

# Ask the user for the name of the file for compression
compression_file_name = input("Enter the name of the file for compression: ")

# Ask the user for the name of the file to save compressed data
save_file_name = input("Enter the name of the file to save compressed data: ")

with open(compression_file_name, "rb") as file:
    compressed_data_check_size = file.read()

if extract_option == "2":
    num_bits_minus = len(compressed_data_check_size)
    num_bits = (num_bits_minus % 8) - 1
    print("This number you must use for extracting your file")
    print(num_bits)
elif extract_option == "1":
    num_bits = int(input("Enter the number of bits for the file numbers: "))

max_value = 2 ** num_bits

# Prompt the user for extraction options

while X < max_value:
    # Increment X by 1
    X += 1

    # Save X in binary format with leading zeros to match the specified number of bits
    binary_representation = format(X, f"0{num_bits}b")

    # Save the binary representation to a binary file
    with open(compression_file_name, "wb") as file:
        file.write(binary_representation.encode('utf-8'))

    # Read the binary data from the file
    with open(compression_file_name, "rb") as file:
        binary_data = file.read()

    # Extract the binary data to recover X
    extracted_X = int(binary_data, 2)

    # Increment Z by 1
    Z += 1

    # Using the provided formula
    Number_of_the_file = (((Number_of_the_file * 2 ** y) + Add) // 3) * T_Real // Divided_coordinates
    Divided_coordinates += 1
    T_Real += 1
    Add += 1
    y += 1
    Number_of_the_file += 1

    # Compression and data extraction can be added here
    if extract_option == '1':
        # Option 1 for extraction
        data_to_compress = f"Your data to be compressed for iteration {Number_of_the_file}"
    elif extract_option == '2':
        # Option 2 for extraction
        data_to_compress = f"Another data to be compressed for iteration {Number_of_the_file}"
    else:
        # Handle invalid extraction option
        print("Invalid extraction option. Please choose '1' or '2'.")

    # Perform compression
    compressed_data = paq.compress(data_to_compress.encode('utf-8'))

    # Save compressed data to the specified file
    with open(save_file_name, "wb") as file:
        file.write(compressed_data)

    # Read the compressed data from the file
    with open(save_file_name, "rb") as file:
        compressed_data = file.read()

    # Extract the data
    extracted_data = paq.decompress(compressed_data)

    # Print or work with the extracted data
    # print(f"Number_of_the_file: {Number_of_the_file}")
    # print(f"Extracted data for iteration {Number_of_the_file}: {extracted_data.decode('utf-8')}")

# End of the loop