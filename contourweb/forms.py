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
                   'color': 'b',
                   'graph': True},
    'inversion': {'name': 'Inversion',
                  'color': 'r',
                   'graph': True},
    'translation': {'name': 'Normal form',
                    'color': 'g',
                    'graph': True},
    'prime_form_marvin_laprade': {'name': 'ML Prime form',
                                  'color': 'm',
                                  'graph': True},
    'internal_diagonals': {'name': 'Internal diagonal (1)',
                           'graph': False},
    'reduction_morris': {'name': 'Morris Reduction',
                         'graph': False},
    'adjacency_series_vector': {'name': 'Contour Adjacency Series Vector (CASV)',
                                'graph': False},
    'interval_succession': {'name': 'Contour Interval Succession (CIS)',
                            'graph': False},
    'interval_array': {'name': 'Contour Interval Array (CIA)',
                       'graph': False},
    'class_vector_i': {'name': 'Contour Class Vector I (CCVI)',
                       'graph': False},
    'class_vector_ii': {'name': 'Contour Class Vector II (CCVII)',
                        'graph': False}}


OP_CHOICES = sorted([(op, ops_dic[op]['name']) for op in ops_dic.keys()], key=lambda x: x[1])


class ContourForm(forms.Form):
    contour_points = forms.CharField(max_length=20,
                                     initial='0 2 1 3 4 5',
                                     validators=[validate_cps],
                                     help_text='Input cseg contour points.')

    operation = forms.MultipleChoiceField(choices=OP_CHOICES, widget=forms.CheckboxSelectMultiple)
