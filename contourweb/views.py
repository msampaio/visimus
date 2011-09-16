from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from forms import ContourForm
from forms import ops_dic
import contour.contour as cc
import contour.plot as cp
import contour.auxiliary as ca


def main_page(request):
    return render(request, 'main_page.html', {})


def contour_form(request):
    if request.method == "POST":
        form = ContourForm(request.POST)
        if form.is_valid():
            request.session['contour'] = form.cleaned_data['contour_points']
            request.session['operation'] = form.cleaned_data['operation']
            return HttpResponseRedirect('/contour/show/')
    else:
        form = ContourForm()

    args = {'form': form}

    return render(request, 'contour_form.html', args)


def contour_show(request):
    cont = request.session['contour']
    operations = request.session['operation']

    cseg = cc.Contour([int(x) for x in cont.strip().split()])

    args = {'cseg': cseg}
    graph = [[cseg, 'k', 'Original']]

    ar = []
    for op in operations:
        dic = ops_dic[op]
        value = ca.apply_fn(cseg, op)
        if dic['graph'] == True:
            graph.append([value, dic['color'], dic['name']])
        ar.append([dic['name'], value])

    cp.contour_lines_save_django(*graph)

    args = {'cseg': cseg, 'op_dicts': ar}

    return render(request, 'contour_show.html', args)
