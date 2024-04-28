#Ref finder outline
import sqlite3

def initialize_database():
    conn = sqlite3.connect('reference_photos.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS photos
                  (id INTEGER PRIMARY KEY, file_path TEXT, tags TEXT)''')
    conn.commit()
    conn.close()

def define_ref_folder():
    # prompt to select a source folder for the app every time on start
    pass

def upload_photo():
    file_path = input("Enter file path of the photo: ")
    if file_path:
        tags = input("Enter tags for the photo (comma-separated): ")
        insert_photo(file_path, tags)
        print("Photo uploaded successfully!")
    else:
        print("No file path provided.")


def insert_photo(file_path, tags):
    conn = sqlite3.connect('reference_photos.db')
    c = conn.cursor()
    c.execute("INSERT INTO photos (file_path, tags) VALUES (?, ?)", (file_path, tags))
    conn.commit()
    conn.close()

def search_photos():
    search_tags = input("Enter tags to search for photos: ")
    conn = sqlite3.connect('reference_photos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM photos WHERE tags LIKE ?", ('%'+search_tags+'%',))
    result = c.fetchall()
    if result:
        for row in result:
            print("File Path:", row[1])
            print("Tags:", row[2])

def main():
    initialize_database()
    while True:
        print("\nReference Photo Manager\n")
        print("1. Upload Photo")
        print("2. Search Photos")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            upload_photo()
        elif choice == '2':
            search_photos()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

