class GetTenant:

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        # print('----')
        # print(request.META["QUERY_STRING"])
        # request.META["QUERY_STRING"] = "/homepage"
        request.META["MY_META_VAR"] = "testing my custom meta var"
        # print('----')
        # print(request.META["MY_META_VAR"])
        response = self.get_response(request)
        # print('-----**------**-----')
        # print(response)
        # print('----')
        # for k, v in request.META.items():
        #     print(f"{k}: {v}")
        # print('----')
        return response
