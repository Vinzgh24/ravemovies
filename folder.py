import os

# Definisikan direktori yang ingin Anda proses
direktori_utama = '/data/data/com.termux/files/home/rave/content/movies'

# Fungsi untuk menghasilkan daftar folder dalam format MD
def generate_md_list(directory):
    folders = {}

    # Iterasi melalui direktori
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # Hanya proses folder, bukan file
        if os.path.isdir(folder_path):
            first_letter = folder_name[0].upper()
            if first_letter == 'A':
                if first_letter not in folders:
                    folders[first_letter] = []
                folders[first_letter].append(folder_name)

    # Mengurutkan folder berdasarkan nama
    for key in folders:
        folders[key].sort()

    # Membuat daftar dalam format MD
    md_list = ''

    for key, folder_names in sorted(folders.items()):
        md_list += f'n## {key}n'
        for folder_name in folder_names:
            link_text = f'- [{folder_name}]({{< ref "movies/{folder_name}" >}})n'
            md_list += link_text

    return md_list

# Hasilkan daftar MD
md_result = generate_md_list(direktori_utama)

# Tulis hasil ke file MD
with open('list.md', 'w') as md_file:
    md_file.write(md_result)

print('Daftar folder dengan urutan berawalan A telah dibuat dalam format MD dan disimpan dalam list.md')
