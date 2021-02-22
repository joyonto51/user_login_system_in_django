from django.utils.deprecation import MiddlewareMixin



class LibraryMiddleware(MiddlewareMixin):

    def process_request(self, request):
        response = self.get_response(request)
        # print("Hello, Jayanta")
        return response
