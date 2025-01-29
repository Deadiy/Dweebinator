# Dweebinator: ROM Organizer

**Dweebinator** is a Python script designed to help users organize their ROM collection into system-specific folders. It automatically identifies new ROM files, categorizes them based on their extensions, and moves them into the appropriate folders for easy access. The script also checks for conflicts when multiple systems share the same file extension and prompts the user for confirmation or auto-selects the system if there's only one match.

---

## Features

- **Automatic Organization**: Moves ROMs into system-specific folders based on their file extension.
- **Conflict Handling**: Detects conflicts when multiple systems use the same file extension and prompts the user for resolution.
- **Clean ROM Names**: Removes special characters and spaces from ROM names for consistent and clean folder structures.
- **Preconfigured for Batocera**: The script is preconfigured to organize ROMs into the Batocera-compatible folder structure.
- **Flexible**: Handles multiple systems and ROM extensions, and it allows for recursive scanning of subfolders.

---

## Installation

1. **Download and Extract**:
   - Unzip the Dweebinator folder.
   - Move the extracted folder to your desired location, for example, `/userdata`.

2. **Access via SSH**:
   - Connect to your system via SSH.

3. **Navigate to the Dweebinator Directory**:
   Ensure you are in the `Dweebinator` directory:

   ```bash
   cd /userdata/Dweebinator/
   ```

---

## Usage

1. **Place ROM Files**:
   Put your unorganized ROM files in the specified **unorganized folder**.

2. **Run the Script**:
   Execute the following command in the `Dweebinator` directory to start the organization process:

   ```bash
   python Dweebinator.py
   ```

3. **Process Confirmation**:
   If new ROMs are found in the **unorganized folder**, the script will list them and prompt you to confirm whether you'd like to proceed with the organization:

   ```bash
   Found the following new ROMs in the unorganized folder:
   - Conker's Bad Fur Day.z64
   - Ben 10 - Protector of Earth (USA).iso

   Make sure all files are fully moved to the unorganized folder before proceeding.
   Do you want to proceed with the organization? (y/n): y
   ```

4. **Conflict Resolution**:
   If the ROM's extension is associated with multiple systems, the script will ask you to choose which system it belongs to:

   ```bash
   Conflict detected for Ben 10 - Protector of Earth (USA).iso with extension .iso
   Which system is this ROM for?
   1. dreamcast
   2. playstation
   3. saturn
   4. psp
   Enter the number corresponding to the system: 4
   ```

5. **ROM Organization**:
   After confirming or auto-assigning the system, the script will move the ROM to the appropriate folder and rename it to ensure the file name is clean and consistent.

6. **Completion**:
   Once all ROMs are successfully moved and organized, the script will show the following confirmation message:

   ```bash
   ROMs have been successfully moved and organized!
   ```

---

## License

This project is licensed under the **GPL-3.0 License** - see the [LICENSE](LICENSE) file for details.
