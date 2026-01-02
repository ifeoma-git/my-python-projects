"""
COMP.CS.100 Programming 1
Read genres and tv-series from a file into a dict.
Print a list of the genres in alphabetical order
and list tv-series by given genre on user's command.

Author: Ifeoma Nwankwo
"""

def read_file(filename):
    """
    Reads and saves the series and their genres from the file.

    :param filename: Name of the file to read series and genres from.
    :return: A dictionary where keys are genres and values are sets of series names.
    """
    genre_dict = {}

    try:
        file = open(filename, mode="r")

        for row in file:
            name, genres = row.rstrip().split(";")
            genres = genres.split(",")

            for genre in genres:
                genre = genre.strip()
                if genre not in genre_dict:
                    genre_dict[genre] = set()
                genre_dict[genre].add(name.strip())

        file.close()
        return genre_dict

    except ValueError:
        print("Error: rows were not in the format name;genres.")
        return None

    except IOError:
        print("Error: the file could not be read.")
        return None


def main():
    filename = input("Enter the name of the file: ")
    genre_data = read_file(filename)

    if genre_data is None:
        return

    # Print genres in alphabetical order
    print("Available genres are: " + ", ".join(sorted(genre_data.keys())))

    while True:
        genre = input("> ")

        if genre == "exit":
            return

        if genre in genre_data:
            for series in sorted(genre_data[genre]):
                print(series)
        # If genre is not found or has no series, print nothing.


if __name__ == "__main__":
    main()
