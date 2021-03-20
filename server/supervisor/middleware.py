import logging
from .models import Supervisor

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        headers = request.headers
        
        request.sup = None
        if 'Authorization-Sup' in headers:
            try:
                token = headers['Authorization-Sup']
                request.sup = Supervisor.objects.get(token=token)
                print(request.sup)
            except Supervisor.DoesNotExist:
                pass

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response