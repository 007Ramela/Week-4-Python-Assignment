
def read_and_modify_file():
    # Ask the user for the filename
    input_filename = input("Enter the filename to read: ")
    output_filename = "modified_" + input_filename  # Output file with 'modified_' prefix
    
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        modified_content = content.upper()  # You can change this modification logic

        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"File has been successfully modified. The modified content is saved in '{output_filename}'.")

    except FileNotFoundError:

        print(f"Error: The file '{input_filename}' does not exist.")

    except PermissionError:

print(f"Error: You do not have permission to read or write to '{input_filename}'.")

    except Exception as e:

        print(f"An unexpected error occurred: {e}")


read_and_modify_file()
