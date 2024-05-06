#Ref finder outline
import sqlite3
import shutil
import os

def initialize_database():
    conn = sqlite3.connect('reference_photos.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS photos
                  (id INTEGER PRIMARY KEY, file_path TEXT, tags TEXT)''')
    conn.commit()
    conn.close()

def define_ref_folder():
    folder_path = input("Enter the path of the reference photo folder: ")
    if os.path.isdir(folder_path):
        # Save the folder path to a configuration file or database
        print("Reference folder set to:", folder_path)
        return folder_path
    else:
        print("Invalid folder path. Please try again.")
        return None

def upload_photo(ref_folder):
    file_path = input("Enter file path of the photo: ")
    if os.path.isfile(file_path):
        tags = input("Enter tags for the photo (comma-separated): ")
        insert_photo(file_path, tags)
        print("Photo uploaded successfully!")
        
        # Copy the uploaded file to the specified reference folder
        file_name = os.path.basename(file_path)
        shutil.copy(file_path, os.path.join(ref_folder, file_name))
        
        # Organize the uploaded file based on tags
        tag_list = tags.split(',')
        for tag in tag_list:
            tag_folder = os.path.join(ref_folder, tag.strip())
            if not os.path.exists(tag_folder):
                os.makedirs(tag_folder)
            shutil.copy(file_path, os.path.join(tag_folder, file_name))
        
    else:
        print("Invalid file path. Please try again.")


def insert_photo(file_path, tags):
    conn = sqlite3.connect('reference_photos.db')
    c = conn.cursor()
    c.execute("INSERT INTO photos (file_path, tags) VALUES (?, ?)", (file_path, tags))
    conn.commit()
    conn.close()

def search_photos(ref_folder):
    search_tags = input("Enter tags to search for photos: ")
    conn = sqlite3.connect('reference_photos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM photos WHERE tags LIKE ?", ('%'+search_tags+'%',))
    result = c.fetchall()
    if result:
        for row in result:
            print("File Path:", row[1])
            # Extract the file name from the file path
            file_name = os.path.basename(row[1])
            # Search for the file in the specified reference folder
            for root, dirs, files in os.walk(ref_folder):
                if file_name in files:
                    print("Location:", os.path.join(root, file_name))
                    break
    else:
        print("No matching photos found.")
    conn.close()

def main():
    initialize_database()
    ref_folder = define_ref_folder()
    if ref_folder:
        while True:
            print("\nReference Photo Manager\n")
            print("1. Upload Photo")
            print("2. Search Photos")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")
            if choice == '1':
                upload_photo(ref_folder)
            elif choice == '2':
                search_photos(ref_folder)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

