import sys

# Function to read the contents of a file and return a list of lines.
def read_file(filename):
    """
    Reads the contents of a file and returns a list of lines.

    Parameters:
    - filename (str): The name of the file to be read.

    Returns:
    list: A list containing the lines of the file.

    Raises:
    FileNotFoundError: If the specified file is not found, an error is raised, and the program exits.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print(f'Cannot open "{filename}"!')
        sys.exit(1)

# Function to analyze a list of lines representing cat visits in a house.
def analyze_file(file_lines):
    """
    Analyzes a list of lines representing cat visits.

    Parameters:
    - file_lines (list): A list containing lines of a file with cat visit data.

    Returns:
    tuple: A tuple containing the following elements:
        - cat_visits (int): The number of visits by the cat labeled as 'OURS'.
        - other_cats (int): The number of visits by other cats labeled as 'THEIRS'.
        - total_time_in_house (int): The total time spent by the 'OURS' cat in the house (in minutes).
        - durations (list): A list containing the durations of each visit by the 'OURS' cat (in minutes).
    """
    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    durations = []

    for line in file_lines:
        if line.strip() == 'END':
            break

        parts = line.strip().split(',')
        cat_type, entry_time, exit_time = parts

        entry_time = int(entry_time)
        exit_time = int(exit_time)

        if cat_type == 'OURS':
            cat_visits += 1
            total_time_in_house += exit_time - entry_time
            durations.append(exit_time - entry_time)
        elif cat_type == 'THEIRS':
            other_cats += 1

    return cat_visits, other_cats, total_time_in_house, durations

def format_time(minutes):
    """
    Convert a given duration in minutes into a formatted string representation.

    Parameters:
    - minutes (int): The total duration in minutes to be formatted.

    Returns:
    str: A formatted string representing the input duration as 'hours Hours, minutes Minutes'.
    """

    hours = minutes // 60
    minutes = minutes % 60
    return f'{hours} Hours, {minutes} Minutes'

# Function to execute the main logic of the program.
def main():
    """
    Reads a log file, analyzes cat visit data, and prints the analysis results.

    This function serves as the main entry point for the program.

    Command Line Arguments:
    - sys.argv[0]: The name of the script.
    - sys.argv[1]: The filename of the log file to be analyzed.

    Prints:
    - Cat visits count.
    - Other cats count.
    - Total time the 'OURS' cat spent in the house.
    - If there are cat visits, it also prints average, longest, and shortest visit durations.
    """
    if len(sys.argv) != 2:
        print('Missing command line argument!')
        sys.exit(1)

    filename = sys.argv[1]
    file_lines = read_file(filename)

    cat_visits, other_cats, total_time, durations = analyze_file(file_lines)

    print(f'\nLog File Analysis\n{"="*18}\n')
    print(f'Cat Visits: {cat_visits}')
    print(f'Other Cats: {other_cats}\n')
    print(f'Total Time in House: {format_time(total_time)}\n')

    if cat_visits > 0:
        average_duration = sum(durations) / len(durations)
        longest_duration = max(durations)
        shortest_duration = min(durations)

        print(f'Average Visit Length: {int(average_duration)} Minutes')
        print(f'Longest Visit:        {longest_duration} Minutes')
        print(f'Shortest Visit:       {shortest_duration} Minutes')

# This conditional statement checks whether the current script is the main program
# and not being imported as a module. If it is the main program, it calls the
# main() function, providing a clear entry point for execution.
if __name__ == "__main__":
    main()
