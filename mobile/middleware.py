from datetime import datetime, date
from django.shortcuts import render,redirect


class AgentMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('agent'):
            return redirect('enter_login')
        response = self.get_response(request)
        return response
