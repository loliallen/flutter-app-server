import logging
from .models import User

class PsycologistMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        headers = request.headers
        
        request.psy = None
        if 'Authorization-Psy' in headers:
            try:
                token = headers['Authorization-Psy']
                request.psy = User.objects.get(token=token)
                print(request.psy)
            except User.DoesNotExist:
                pass

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response