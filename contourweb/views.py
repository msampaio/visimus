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
            request.session['contour_1'] = form.cleaned_data['contour_1']
            request.session['contour_2'] = form.cleaned_data['contour_2']
            request.session['operation'] = form.cleaned_data['operation']
            return HttpResponseRedirect('/contour/show/')
    else:
        form = ContourForm()

    args = {'form': form}

    return render(request, 'contour_form.html', args)


def contour_show(request):
    contour_1 = request.session['contour_1']
    contour_2 = request.session['contour_2']
    operations = request.session['operation']

    cseg1 = cc.Contour([int(x) for x in contour_1.strip().split()])
    cseg2 = cc.Contour([int(x) for x in contour_2.strip().split()])

    op_arg = []

    for operation in operations:
        dic = ops_dic[operation]
        name = dic['name']
        value1 = ca.apply_fn(cseg1, operation)
        value2 = ca.apply_fn(cseg2, operation)
        op_type = dic['op_type']
        op_arg.append({'op_name': name, 'op_code': operation, 'op_type': op_type,
                       'op_value_repr1': value1, 'op_value1': list(value1),
                       'op_value_repr2': value2, 'op_value2': list(value2)})

    args = {'cseg1': list(cseg1), 'code1': cseg1,
            'cseg2': list(cseg2), 'code2': cseg2,
            'op_dicts': op_arg}

    return render(request, 'contour_show.html', args)
