import requests
from django.http import HttpResponse


# def simple_middleware(get_response):
#     # Единовременная настройка и инициализация.
#     def middleware(request):
#         # Код должен быть выполнен для каждого запроса
#         # до view
#         response = get_response(request)
#         # Код должен быть выполнен ответа после view
#         return response
#     return middleware

# def timing(get_response):
#     def middleware(request):
#         t1 = time.time()
#         response = get_response(request)
#         t2 = time.time()
#         print(f"TOTAL TIME: {(t2 - t1)}")
#         return response
#     return middleware

class StackOverflow():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        url = 'https://api.stackexchange.com/2.2/search'
        params = {
            'site': 'stackoverflow',
            'order': 'desc',
            'sort': 'votes',
            'pagesize': 3,
            'tagged': 'python;django',
            'intitle': str(exception),
        }
        response = requests.get(url, params=params)
        html = ''
        for question in response.json()['items']:
            html += '<h2><a href="{link}">{title}</a></h2>'.format(**question)
        return HttpResponse(html)