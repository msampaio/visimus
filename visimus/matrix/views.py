from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from visimus.matrix import music
from visimus.matrix.forms import RowForm


def main_page(request):
    return render(request, 'main_page.html', {})


def matrix_form(request):
    if request.method == "POST":
        form = RowForm(request.POST)
        if form.is_valid():
            request.session['row'] = form.cleaned_data['row']
            request.session['notes'] = form.cleaned_data['notes']
            return HttpResponseRedirect('/matrix/show/')
    else:
        form = RowForm(initial={'row': "4  5  7  1  6  3  8  2 11  0  9 10",
                                'notes': "6 3 8"})

    args = {'form': form}
    return render(request, 'matrix-form.html', args)


def matrix_show(request):
    row = request.session['row']
    notes = request.session['notes']
    notes_clean = [int(n) for n in notes.split()]
    row_clean = [int(n) for n in row.split()]
    matrix = music.row_matrix(row_clean)
    positions = music.row_matrix_search(matrix, notes_clean)
    positions_column = music.column_matrix_search(matrix, notes_clean)
    consecutive = music.is_consecutive(positions)
    cons_column = music.is_consecutive(positions_column)
    matrixpos = zip(matrix, positions, consecutive)
    args = {'row': row, 'matrixpos': matrixpos, 'cons_column': cons_column}
    return render(request, 'show_matrix.html', args)
