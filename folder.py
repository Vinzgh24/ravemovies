import os
import re

def write_folder_names_to_txt(root_dir, output_file):
    folders = {}
    
    # Traverse through the root directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            first_character = dirname[0].upper()
            if first_character.isalpha():
                if first_character not in folders:
                    folders[first_character] = []
                folders[first_character].append(dirname)
            elif first_character.isnumeric():
                if "0-9" not in folders:
                    folders["0-9"] = []
                folders["0-9"].append(dirname)
    
    # Sort the folder names alphabetically within each letter group
    for key in folders:
        if key != "0-9":
            folders[key].sort()
        else:
            folders[key].sort(key=lambda x: int(re.search(r"\d+", x).group()))
    
    # Write the formatted folder names to the output file
    with open(output_file, 'w') as file:
        for key, values in sorted(folders.items()):
            file.write(f"\n## {key}\n\n")
            for folder in values:
                file.write(f"- [{folder}]({{< ref \"movies/{folder}\" >}})\n")
    
    print("Folder names written to the output file.")

# Specify the root directory and output file path
root_directory = '/data/data/com.termux/files/home/rave/content/movies'
output_file_path = 'folder_names.txt'

# Call the function to write folder names to the text file
write_folder_names_to_txt(root_directory, output_file_path)