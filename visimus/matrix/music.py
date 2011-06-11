def transposition(notes, index):
    return [(n + index) % 12 for n in notes]


def inversion(notes, index=0):
    return [(index - n) % 12 for n in notes]


def transposition_startswith(notes, start_note):
    return transposition(notes, start_note - notes[0])


def inversion_first_note(notes):
    """Use 1st note as index"""
    
    return inversion(notes, 2 * notes[0])


def rotate(item):
    return item[1:] + item[:-2]


def interval_class(note):
    n = note % 12
    return n if n <= 6 else 12 - n


def intervals(notes):
    return [interval_class(y - x) for x,y in zip(notes, rotate(notes)[:-1])]


def row_matrix(row):
    return [transposition_startswith(row, n) for n in inversion_first_note(row)]


def row_matrix_search(matrix, notes):
    return [[row.index(note) for note in notes] for row in matrix]


def column_matrix_search(matrix, notes):
    return [[row.index(note) for note in notes] for row in zip(*matrix)]


def is_consecutive(positions):
    return [True if all([x == 1 for x in intervals(pos)]) else False for pos in positions]
