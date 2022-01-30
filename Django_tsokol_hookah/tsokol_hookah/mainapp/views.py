from django.shortcuts import render


def mainpage(request):
    return render(request, 'mainapp/mainpage.html')


# def about(request):
#     return render(request, 'mainapp/about.html')
