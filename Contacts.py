"""
COMP.CS.100 Programming 1
A program that reads a CSV file with semicolon-separated values.
Author: Ifeoma Nwankwo
"""

def read_file(filename):
    """
    Reads a CSV file with semicolon-separated values, where
    the first line contains column headers. Returns a dictionary
    where each key is from the first column, and each value is
    another dictionary mapping column headers to corresponding values.

    :param filename: str - name of the input CSV file
    :return: dict - nested dictionary of contact information
    """
    data = {}

    with open(filename, "r") as file:
        # Read the first line and extract headers
        headers = file.readline().strip().split(";")

        # Process each subsequent line
        for line in file:
            parts = line.strip().split(";")

            # The first value is the outer key
            key = parts[0]

            # Create a dict for this line, pairing headers with values
            # If some columns are missing, fill with empty strings
            values = {}
            for i, header in enumerate(headers):
                # If parts doesn't have a value for this header, assign empty string
                values[header] = parts[i] if i < len(parts) else ""

            # Store the inner dict in the outer dict by key
            data[key] = values

    return data