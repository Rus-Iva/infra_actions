from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Для первого коммита.'
                        'Теперь свой воркфлоу.')


def second_page(request):
    return HttpResponse('А это вторая страница')
