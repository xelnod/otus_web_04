from otus04.renderer import render
from otus04.router import route


def application(env, start_response):
    url = env.get('REQUEST_URI')
    func = route(url)
    if callable(func):
        start_response('200 OK', [('Content-Type', 'text/html')])
        return func(env)
    else:
        start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
        return render('templates/404.html')
