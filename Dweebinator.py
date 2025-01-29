import os
import shutil
import time
import yaml

# Load config from the YAML file
def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

# Clean ROM name by removing special characters and spaces
def clean_rom_name(rom_name):
    return rom_name.replace(" ", "_").replace("'", "").replace("-", "_")

# Function to move the ROM to the appropriate folder and rename it
def move_rom(rom_path, target_folder, system):
    try:
        if system:
            # Clean the ROM name and append the extension
            cleaned_rom_name = clean_rom_name(os.path.basename(rom_path))
            
            # Ensure the target system folder exists
            target_folder_path = os.path.join(target_folder, system.lower())
            if not os.path.exists(target_folder_path):
                os.makedirs(target_folder_path)
                
            # Move the ROM into the correct folder
            target_path = os.path.join(target_folder_path, cleaned_rom_name)
            shutil.move(rom_path, target_path)
            print(f"{rom_path} moved and renamed successfully to {target_path}")
    except Exception as e:
        print(f"Error moving {rom_path}: {e}")

# Check for conflicts based on ROM extension and mapping from config
def check_for_conflicts(rom_path, rom_system_mapping):
    extension = os.path.splitext(rom_path)[1].lstrip('.')
    if extension in rom_system_mapping:
        systems = rom_system_mapping[extension]
        if len(systems) == 1:
            # If there's only one system for the extension, automatically return it
            return systems[0]
        else:
            print(f"Conflict detected for {rom_path} with extension .{extension}")
            print("Which system is this ROM for?")
            for i, system in enumerate(systems):
                print(f"{i + 1}. {system}")
            choice = input(f"Enter the number corresponding to the system: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(systems):
                return systems[int(choice) - 1]
            else:
                print("Invalid choice, skipping ROM.")
                return None
    return None

# Function to print ASCII art for Dweebinator
def print_ascii_art():
    print("""
    ________
   /        \\
  /          \\
 /   O    O   \\
|     ___     |   Dweebinator
|    |   |    |
|    |___|    |
|   /     \\   |
|  /       \\  |
 \\_/       \\_/
    """)

# Main script for waiting for ROMs and organizing them
def organize_roms():
    config = load_config()  # Load config from the YAML file

    # Folders from config
    unorganized_folder = config.get("unorganized_folder", "/userdata/Dweebinator/unorganized_roms")
    roms_folder = config.get("roms_folder", "/userdata/roms")

    # ROM System Mapping from config
    rom_system_mapping = config.get("rom_system_mapping", {})

    print_ascii_art()

    while True:
        print("Waiting for ROM files to be added to the unorganized folder...")

        # Wait for new ROMs
        new_roms = [f for f in os.listdir(unorganized_folder) if os.path.isfile(os.path.join(unorganized_folder, f))]
        if not new_roms:
            print("No new ROMs found. Waiting for files to be added...")
            time.sleep(10)  # Wait for 10 seconds

            # After 10 seconds, ask if the user wants to add more ROMs
            choice = input("10 seconds passed. Do you want to add more ROMs? (y/n): ")
            if choice.lower() == 'n':
                print("Do you want to proceed with the organization? (y/n): ")
                proceed = input().strip().lower()
                if proceed == 'n':
                    print("Exiting the organization process.")
                    break  # Exit the script
                else:
                    print("Proceeding with organization.")
                    break  # Proceed to the organization process

        # Found ROMs in unorganized folder
        print("Found the following new ROMs in the unorganized folder:")
        for rom in new_roms:
            print(f"- {rom}")

        print("Make sure all files are fully moved to the unorganized folder before proceeding.")
        proceed = input("Do you want to proceed with the organization? (y/n): ").strip().lower()

        if proceed == 'y':
            for rom in new_roms:
                rom_path = os.path.join(unorganized_folder, rom)
                extension = os.path.splitext(rom)[1].lstrip('.')

                # Check for conflicts before moving
                system = check_for_conflicts(rom_path, rom_system_mapping)

                if system:
                    # Determine the appropriate folder and move the ROM
                    move_rom(rom_path, roms_folder, system)

            print("ROMs have been successfully moved and organized!")
            break  # Exit after organizing the ROMs

if __name__ == "__main__":
    organize_roms()
