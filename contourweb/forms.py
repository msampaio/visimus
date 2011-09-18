from django import forms
from django.forms.fields import CharField
from django.core.exceptions import ValidationError


def validate_cps(str):

    def cps_type(str):
        try:
            [int(x) for x in str.strip().split()]
        except:
            m1 = u'< {0} > is not a valid contour.'.format(str)
            m2 = u'Please enter valid contour points, like 0 2 1.'
            raise ValidationError(' '.join([m1, m2]))

    def cps_size(lst, maximum, minimum):
        absolute = max(maximum, abs(minimum))
        if absolute > 30:
            m1 = u'The value {0} is very big.'.format(absolute)
            m2 = u'Please enter contour points lower than 30.'
            raise ValidationError(' '.join([m1, m2]))

    def cps_positive(minimum):
        if minimum < 0:
            m1 = u'The value {0} is negative.'.format(minimum)
            m2 = u'Please enter only positive contour points.'
            raise ValidationError(' '.join([m1, m2]))

    cps_type(str)
    lst = [int(x) for x in str.strip().split()]
    maximum = max(lst)
    minimum = min(lst)
    cps_size(lst, maximum, minimum)
    cps_positive(minimum)


ops_dic = {
    'retrograde': {'name': 'Retrograde',
                   'op_type': 'Plot'},
    'inversion': {'name': 'Inversion',
                   'op_type': 'Plot'},
    'translation': {'name': 'Normal form',
                    'op_type': 'Plot'},
    'prime_form_marvin_laprade': {'name': 'ML Prime form',
                                  'op_type': 'Plot'},
    'internal_diagonals': {'name': 'Internal diagonal (1)',
                           'op_type': 'Matrix'},
    'reduction_morris': {'name': 'Morris Reduction',
                         'op_type': 'Comparison'},
    'adjacency_series_vector': {'name': 'Contour Adjacency Series Vector (CASV)',
                                'op_type': 'Friedmann'},
    'interval_succession': {'name': 'Contour Interval Succession (CIS)',
                            'op_type': 'Friedmann'},
    'interval_array': {'name': 'Contour Interval Array (CIA)',
                       'op_type': 'Friedmann'},
    'class_vector_i': {'name': 'Contour Class Vector I (CCVI)',
                       'op_type': 'Friedmann'},
    'class_vector_ii': {'name': 'Contour Class Vector II (CCVII)',
                        'op_type': 'Friedmann'}}


OP_CHOICES = sorted([(op, ops_dic[op]['name']) for op in ops_dic.keys()], key=lambda x: x[1])


class ContourForm(forms.Form):
    contour_points = forms.CharField(max_length=20,
                                     initial='0 2 1 3 4 5',
                                     validators=[validate_cps],
                                     help_text='Input cseg contour points.')

    operation = forms.MultipleChoiceField(choices=OP_CHOICES, widget=forms.CheckboxSelectMultiple)
