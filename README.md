# NASA Attendee List to Mailchimp Converter
This script helps you convert a NASA attendee list (CSV file) into a format suitable for import into Mailchimp. It performs the following actions:

- Prompts you to select the CSV file containing the attendee list.
- Splits the "Name" column into separate "First Name" and "Last Name" columns.
- Fills missing values with empty strings.
- Removes unnecessary columns not required by Mailchimp.
-Saves the transformed data as a new CSV file with a timestamped name in your chosen output directory.

## How to Use:

1. Download the Script: Download the script (a single executable file) from the releases section of this repository.
2. Run the Executable: Double-click the downloaded file to run the script.
- On some systems, you might need to right-click and choose "Run" or its equivalent depending on your operating system.
3. Select Files: The script will prompt you to select the following:
- Input CSV: Choose the CSV file containing the NASA attendee list.
- Output Directory: Specify the folder where you want to save the converted CSV file.
4. Wait for Completion: The script will process the file and notify you when it's finished. The converted file will be saved in your chosen output directory with a timestamped name.

## Requirements:

This script requires Python 3 to be installed on your system. You can check by running python --version or python3 --version in your terminal.
- If you don't have Python 3 installed, you can download it from https://www.python.org/downloads/.

## Additional Notes:

- This script assumes the input CSV file has a column named "Name" containing attendee full names.
- You can review the source code of the script within this repository if you're interested in the technical details.

## Disclaimer:

This script is provided as-is without warranty of any kind. Please ensure your data is backed up before using this script.