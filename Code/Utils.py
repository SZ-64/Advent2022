def read_file_as_lines(name):
    """ Opens the specified file for reading and returns each line as a string. """
    f = open(name, "r")
    return f.read().split('\n')


def read_file_as_ints(name):
    """ Opens the specified file for reading and returns each line as an int. """
    return [int(x) for x in read_file_as_lines(name)]


def read_line_as_csv(name):
    """ Reads a file (one line) as a list of comma seperated values (ints). """
    return [int(x) for x in read_file_as_lines(name)[0].split(',')]


def seek_until_blank_line(lines):
    """
    Iterates over a list of strings until it finds a blank line and returns what it has seen.
    Will continue from where it left off until the next item or end of list if called again.
    """
    cur_body = []
    for item in lines:
        if item != '':
            cur_body.append(item)
        else:
            yield cur_body
            cur_body = []
