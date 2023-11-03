import os

# Function to format the folder name as a hyperlink
def format_folder_name(folder_name):
    return f"- [{folder_name}]({{< ref \"movies/{folder_name}\" >}})"

# Function to generate the formatted text content
def generate_text_content(folder_list):
    content = ""
    current_letter = ""

    for folder in folder_list:
        # Extract the first character of the folder name
        first_char = folder[0]

        # Check if it's a numeric folder name
        if first_char.isdigit():
            if current_letter != "0-9":
                current_letter = "0-9"
                content += "\n" + current_letter + "\n"

        # Check if the first character has changed
        elif first_char.upper() != current_letter:
            current_letter = first_char.upper()
            content += "\n" + "## " + current_letter + "\n"

        # Format the folder name and add to the content
        content += format_folder_name(folder) + "\n"

    return content

# Specify the folder path
folder_path = "/data/data/com.termux/files/home/rave/content/movies"

# Get all folder names
folders = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

# Sort the folders correctly
folders.sort(key=lambda x: x.strip('(0123456789)'))

# Generate the formatted text content
text_content = generate_text_content(folders)

# Write the content to a text file
with open("folder_names.txt", "w") as file:
    file.write(text_content)