import os
import subprocess
from pathlib import Path

def download_image_with_wget(image_url, save_path):
    # Perintah wget untuk mengunduh gambar
    wget_command = ["wget", "-P", save_path, image_url]

    try:
        # Jalankan perintah wget
        subprocess.run(wget_command, check=True)
        print("Gambar berhasil diunduh.")
    except subprocess.CalledProcessError:
        print("Gagal mengunduh gambar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

def rename_downloaded_images(directory):
    # List semua file gambar di direktori
    image_files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]

    # Ganti nama semua file gambar menjadi "featured.jpg"
    for image_file in image_files:
        old_path = os.path.join(directory, image_file)
        new_path = os.path.join(directory, "featured.jpg")
        os.rename(old_path, new_path)

def navigate_directories(base_directory):
    current_directory = base_directory

    while True:
        print(f"nAnda berada di: {current_directory}")
        folders = sorted([d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))])

        if not folders:
            print("Tidak ada folder tersedia di direktori ini.")
            break

        print("Pilih folder atau tindakan:")
        for idx, folder in enumerate(folders, start=1):
            print(f"{idx}. Masuk ke folder '{folder}'")

        print(f"{len(folders) + 1}. Kembali ke direktori sebelumnya")
        print(f"{len(folders) + 2}. Meletakkan hasil unduhan 'disini'")
        choice = input(f"Pilihan Anda (1-{len(folders) + 2}): ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(folders):
                current_directory = os.path.join(current_directory, folders[choice - 1])
            elif choice == len(folders) + 1:
                current_directory = os.path.dirname(current_directory)
            elif choice == len(folders) + 2:
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")
        else:
            print("Pilihan tidak valid. Coba lagi.")

    return current_directory

if __name__ == "__main__":
    base_directory = "/data/data/com.termux/files/home/rave"

    image_url = input("Masukkan URL gambar (.jpg): ")
    download_path = navigate_directories(base_directory)

    download_image_with_wget(image_url, download_path)
    rename_downloaded_images(download_path)

    print("Gambar berhasil diunduh dan dinamai 'featured.jpg'.")
