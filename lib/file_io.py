def write_file(file_name, file_content):
    """
    Write content to a .txt file.
    
    Args:
        file_name: Name or path of the file (without .txt extension)
        file_content: Content to write to the file
    """
    # Add .txt extension to the file name
    full_file_name = f"{file_name}.txt"
    
    # Open file in write mode ('w') and write content
    with open(full_file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Append content to an existing .txt file.
    
    Args:
        file_name: Name or path of the file (without .txt extension)
        append_content: Content to append to the file
    """
    # Add .txt extension to the file name
    full_file_name = f"{file_name}.txt"
    
    # Open file in append mode ('a') and add content
    with open(full_file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """
    Read and return content from a .txt file.
    
    Args:
        file_name: Name or path of the file (without .txt extension)
    
    Returns:
        str: Content of the file
    """
    # Add .txt extension to the file name
    full_file_name = f"{file_name}.txt"
    
    # Open file in read mode ('r') and return content
    with open(full_file_name, 'r') as file:
        return file.read()