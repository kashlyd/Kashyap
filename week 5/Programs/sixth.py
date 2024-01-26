import sys
import shutil

def create_backup(original_file):
    try:
        # Append ".bak" to the original filename to create the backup filename
        backup_file = original_file + ".bak"

        # Use shutil.copy2 to create a backup copy of the file
        shutil.copy2(original_file, backup_file)

        print(f"Backup created successfully: {backup_file}")

    except FileNotFoundError:
        print(f"Error: File not found - {original_file}")
    except PermissionError:
        print(f"Error: Permission denied - {original_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python backup_file.py <filename>")
    else:
        filename = sys.argv[1]
        create_backup(filename)
