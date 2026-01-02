"""
COMP.CS.100 Programming 1
Bus‑Time-Table Program.

Given the current time as an integer (e.g.  6 :30 →  630,
16 :20 → 1620) the program prints the departure times of the next
three buses according to a fixed timetable.

Author: ifeoma Nwankwo
"""

# Fixed timetable in ascending order (24‑hour clock, HHMM format)
TIMETABLE = [630, 1015, 1415, 1620, 1720, 2000]


def next_bus_index(now, timetable):
    """
    Return the index of the first departure that is >= `now`.
    If `now` is later than all departures, wrap to index 0.
    """
    for idx, dep in enumerate(timetable):
        if dep >= now:
            return idx
    return 0  # wrap to first departure next day


def print_next_n_buses(start_idx, n, timetable):
    """
    Print the next `n` departures starting at `start_idx`,
    wrapping around the list if necessary.
    """
    size = len(timetable)
    for i in range(n):
        idx = (start_idx + i) % size
        print(timetable[idx])


def main():
    now = int(input("Enter the time (as an integer): "))
    first_idx = next_bus_index(now, TIMETABLE)

    print("The next buses leave:")
    print_next_n_buses(first_idx, 3, TIMETABLE)


if __name__ == "__main__":
    main()
