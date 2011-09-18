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

    ar = []

    for operation in operations:
        dic = ops_dic[operation]
        name = dic['name']
        value = ca.apply_fn(cseg, operation)
        graph = dic['graph']
        if graph == True:
            ar.append({'name': name, 'code': operation, 'value': value,
                       'lvalue': list(value), 'graph': graph})
        else:
            ar.append({'name': name, 'value': value})

    args = {'cseg': list(cseg), 'code': cseg, 'op_dicts': ar}

    return render(request, 'contour_show.html', args)
