"""
Script for transforming and saving a NASA attendee list for Mailchimp integration.

This script performs the following tasks:

1. Prompts the user to select a CSV file containing the NASA attendee list.
2. Transforms the data in the selected CSV file to prepare it for Mailchimp import.
    - Splits the 'Name' column into 'First Name' and 'Last Name' columns.
    - Fills missing values with empty strings.
    - Drops unnecessary columns.
3. Saves the transformed data to a new CSV file in the user-specified output directory.

This script utilizes the following functions:

- create_output_path: Generates a timestamped filename with the specified format.
- transform_download_mailchimp: Transforms the DataFrame for Mailchimp integration.
- convert_and_save: Reads a CSV, transforms the data, and saves it to a new CSV file.
- upload_and_output_csv: Drives the user interaction and calls the conversion function.

Coded by: Tim Andes

"""

import os
import datetime
import pytz
import pandas as pd
from tkinter import filedialog

def create_output_path(filename, format):
    """
    Generates a formatted output path for a file.

    This function creates a filename with a timestamp prefix and a specified format extension.

    Args:
        filename: The base filename (without extension).
        format: The file format extension (e.g., "csv", "xlsx").

    Returns:
        A string representing the complete output path with format:
            YYYY-MM-DD-filename.format
    """
    utc_now = datetime.datetime.now(pytz.utc)
    datestamp = utc_now.strftime("%m-%d-%Y")

    return f"{datestamp}-{filename}.{format}"

def transform_download_mailchimp(dataframe):
    """
    Transforms a DataFrame for Mailchimp integration.

    This function takes a DataFrame and performs the following transformations:

    1. Splits the 'Name' column into 'First Name' and 'Last Name' columns.
    2. Fills missing values with empty strings.
    3. Drops unnecessary columns.

    Args:
        dataframe: The input DataFrame.

    Returns:
        The transformed DataFrame.
    """
    dataframe[['First Name', 'Last Name']] = dataframe['Name'].str.split(' ', 1, expand=True)
    dataframe.fillna("", inplace=True)
    dataframe.drop(columns=['Created At', 'Status', 'Name', 'Location', 'Team Name', 'Project Submitted'], inplace=True)

    return dataframe

def convert_and_save(pdf_file_path, output_dir, format="csv"):
    """
    Converts and saves a CSV file to a specified format.

    Reads a CSV file from the specified path, transforms the data using the `transform_download_mailchimp` function, and saves the transformed data to the specified output directory with the given format.

    Args:
        pdf_file_path: The path to the input CSV file.
        output_dir: The path to the output directory.
        format: The desired output format (default is "csv").

    Returns:
        None
    """
    df = pd.read_csv(pdf_file_path)
    file = transform_download_mailchimp(df)
    output_file_name = create_output_path("mailchimp", format)

    file.to_csv(os.path.join(output_dir, output_file_name))

# select input and ouput file paths
def upload_and_output_csv():
    """
    Prompts the user to select an input CSV file and an output directory.

    This function uses a file dialog to allow the user to choose an input CSV file and an output directory.
    It then calls the `convert_and_save` function to process the selected file and save the transformed data.

    Returns:
    None
    """
    pdf_file_path = filedialog.askopenfilename(
        title="Select a the NASA attendee list (CSV)...",
        filetypes=[('CSV Files', '*.csv')]
    )

    output_dir = filedialog.askdirectory(
        title="Select your destination folder..."
    )

    # execute transformation    
    if pdf_file_path and output_dir:
        # create filename and save
        convert_and_save(pdf_file_path, output_dir)
        print(f"CSV to Image Conversion Complete. Saved to {output_dir}")
    else:
        print("Please select both a CSV file and an output directory.")

if __name__ == "__main__":
    upload_and_output_csv()