class GetTenant:

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        for k, v in request.META.items():
            print(f"{k}: {v}")
        print('----')
        print(request.META["QUERY_STRING"])
        request.META["QUERY_STRING"] = "/homepage"
        print('----')
        print(request.META["QUERY_STRING"])
        response = self.get_response(request)
        print('-----**------**-----')
        print(response)
        return response
