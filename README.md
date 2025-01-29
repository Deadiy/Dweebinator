# Dweebinator: ROM Organizer

**Dweebinator** is a Python script designed to help users organize their ROM collection into system-specific folders. It automatically identifies new ROM files, categorizes them based on their extensions, and moves them into the appropriate folders for easy access. The script also checks for conflicts when multiple systems share the same file extension and prompts the user for confirmation or auto-selects the system if there's only one match.

---

## Features

- **Automatic Organization**: Moves ROMs into system-specific folders based on their file extension.
- **Conflict Handling**: Detects conflicts when multiple systems use the same file extension and prompts the user for resolution.
- **Configurable**: Customizable folder paths and system mappings through a `config.yaml` file.
- **Clean ROM Names**: Removes special characters and spaces from ROM names for consistent and clean folder structures.
- **Flexible**: Handles multiple systems and ROM extensions, and it allows for recursive scanning of subfolders.

---

## Installation

### Prerequisites

- Python 3.6 or higher
- `pyyaml` library to read configuration files

### Steps to Install

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/Dweebinator.git
   cd Dweebinator
   ```

2. **Install Python Dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

   Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Configuration File**:
   Copy the sample configuration file to `config.yaml`:
   ```bash
   cp config.sample.yaml config.yaml
   ```
   Edit `config.yaml` to specify the paths for your **unorganized ROMs** folder and **organized ROMs** folder.

4. **Run the Script**:
   ```bash
   python Dweebinator.py
   ```

---

## Configuration (`config.yaml`)

The configuration file allows you to customize folder paths, ROM system mappings, and other settings.

### Example Configuration

```yaml
# Folders
unorganized_folder: "/userdata/Dweebinator/unorganized_roms"  # Folder for unorganized ROMs
roms_folder: "/userdata/roms"  # Destination folder for organized ROMs

# ROM System Mapping
rom_system_mapping:
  nes: ["nes"]
  sfc: ["snes"]
  smc: ["snes"]
  gba: ["gba"]
  gbc: ["gbc"]
  gb: ["gb"]
  n64: ["n64"]
  z64: ["n64"]
  zip: ["arcade", "neogeo"]
  7z: ["arcade", "neogeo"]
  iso: ["dreamcast", "playstation", "saturn", "psp"]
  # Add more mappings as needed

# Options
recursive: true  # Set to true to search subfolders recursively
checksum_verification: true  # Set to true to enable checksum verification
delete_source_files: false  # Set to true to delete source files after successful move

# Advanced
reboot_args: "" # Optional: Add any additional arguments for the 'reboot' command
```

- **unorganized_folder**: Path to the folder containing unorganized ROM files.
- **roms_folder**: Path to the folder where ROMs will be moved and organized into system-specific subfolders.
- **rom_system_mapping**: A dictionary that maps file extensions to one or more systems. This helps the script identify where to move each ROM.
- **recursive**: If set to `true`, the script will search subfolders within the unorganized folder.
- **checksum_verification**: If set to `true`, the script will verify the integrity of ROM files based on their checksums.
- **delete_source_files**: If set to `true`, the script will delete ROM files from the unorganized folder after they are successfully moved.
- **reboot_args**: Optional: Add any arguments for the 'reboot' command (not used in the current version).

---

## Usage

### Running the Script

1. After configuring `config.yaml`, run the script:
   ```bash
   python Dweebinator.py
   ```

2. The script will scan the **unorganized folder** for new ROM files and list them. If new ROMs are found, it will prompt you to confirm that you want to proceed with organizing them:
   ```bash
   Found the following new ROMs in the unorganized folder:
   - Conker's Bad Fur Day.z64
   - Ben 10 - Protector of Earth (USA).iso

   Make sure all files are fully moved to the unorganized folder before proceeding.
   Do you want to proceed with the organization? (y/n): y
   ```

3. If the extension of a ROM is associated with multiple systems, the script will ask you to choose which system it belongs to:
   ```bash
   Conflict detected for Ben 10 - Protector of Earth (USA).iso with extension .iso
   Which system is this ROM for?
   1. dreamcast
   2. playstation
   3. saturn
   4. psp
   Enter the number corresponding to the system: 4
   ```

4. After confirming or auto-assigning the system, the script will move the ROM to the correct folder under **roms_folder** and rename it in a clean format.

5. Once all ROMs are organized, the script will confirm that the operation is complete:
   ```bash
   ROMs have been successfully moved and organized!
   ```

---

## Example Workflow

1. **Adding New ROMs**:
   Place ROM files (e.g., `.iso`, `.z64`, `.gba`) into the **unorganized folder**.

2. **Running the Script**:
   Launch the script to organize them. The script will check for new files, ask for confirmation, and organize them based on the configuration.

3. **Conflict Resolution**:
   If multiple systems use the same extension, the script will ask you to specify the system.

4. **ROM Organization**:
   The ROMs will be moved to appropriate system folders (e.g., `/userdata/roms/n64`, `/userdata/roms/psp`) with clean, consistent names.

---

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
