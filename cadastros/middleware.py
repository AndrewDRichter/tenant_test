class GetTenant:

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        print(request)
        response = self.get_response(request)
        print('-----**------**-----')
        print(response)
        return response
