"""--------------------------------------------------------

file: ex1_David_Sapir_Shimson_Polak.py

Written by:
David Sapir, id = 208917351, login = davidsa
Shimson Polak, id = , login =

Program Description:
A program that will read and analyze a file of a medical
database that is written in a format Of SQL commands and
convert to CVS format.

--------------------------------------------------------"""


def open_file(file_name):
    """ Open an external file for reading """
    return open(file_name, 'r')


def create_cvs_files():
    """ Runs over the SQL and creates a cvs files."""
    # Runs over the lines in the SQL and searches for the key words
    # CREATE TABLE and INSERT INTO and acts accordingly.
    for line in my_file:
        if "CREATE TABLE" in line:
            create_line = line.split()
            key_values = get_table_data(my_file)
        elif "INSERT INTO" in line:
            create_file(my_file, create_line[2].replace('`', ''), key_values, line)


def create_file(m_file, file_name, key_values, line_insert_data):
    """ Creates an external file with the needed data. """
    external_file = open(file_name+".csv", 'w')
    external_file.write(key_values + '\n')
    list_data = get_insert_line(line_insert_data).split("),(")
    for i in list_data:
        external_file.write(i + '\n')


def get_insert_line(line):
    """"""
    for i in range(len(line)):
        if line[i] == '(':
            line = line[i + 1:-3]
            break
    return line


def get_table_data(m_file) -> str:
    """ Reads and returns the currents table data."""
    sentences = ""
    curr_line = m_file.readline().split()
    while "`" in curr_line[0]:
        sentences += curr_line[0].replace('`', '') + ","
        curr_line = m_file.readline().split()

    return sentences[:len(sentences) - 1]


if __name__ == "__main__":
    my_file = open_file("demo.sql")
    create_cvs_files()
