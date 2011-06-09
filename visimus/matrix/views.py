from django.shortcuts import render_to_response, render


def main_page(request):
    return render(request, 'main_page.html', {})


def matrix(request):
    return render(request, 'matrix.html')
