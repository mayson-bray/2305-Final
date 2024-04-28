#Ref finder outline
import sqlite3

def initialize_database():
    # TODO create a function that initializes the database

def define_ref_folder():
    # prompt to select a source folder for the app every time on start

def upload_photo():
    # TODO find a way to upload the photo file path
    # it should upload to a local folder

def insert_photo(file_path, tags):
    # TODO Insert photo information into photos table
    # Commit changes
    # Close connection

def search_photos():
    # TODO fimd a Prompt user to enter tags to search for photos
    # Connect to database
    # Give you the fil path for the photo

def main():
    # Initialize database
    # Enter loop:
        # Display menu options
        # Prompt user for choice
        # If choice is to upload photo:
            # Call upload_photo function
        # If choice is to search photos:
            # Call search_photos function
        # If choice is to exit:
            # Print exit message
            # Break out of loop
        # If choice is invalid:
            # Print error message

if __name__ == "__main__":
    main()

