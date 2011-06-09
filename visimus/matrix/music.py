def transposition(notes, index):
    return [(n + index) % 12 for n in notes]


def inversion(notes, index=0):
    return [(index - n) % 12 for n in notes]


def transposition_startswith(notes, start_note):
    return transposition(notes, start_note - notes[0])


def inversion_first_note(notes):
    """Use 1st note as index"""
    
    return inversion(notes, 2 * notes[0])


def row_matrix(row):
    return [transposition_startswith(row, n) for n in inversion_first_note(row)]
