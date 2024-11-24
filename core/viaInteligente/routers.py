from rest_framework import routers, views
from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.reverse import reverse


class CustomRouter(routers.DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(CustomRouter, self).__init__(*args, **kwargs)
        self.extra_links = OrderedDict()

    def add_extra_route(self, prefix, view_name):
        self.extra_links[prefix] = view_name

    def get_api_root_view(self, api_urls=None):
        routes = OrderedDict()
        list_name = self.routes[0].name

        for prefix, viewset, basename in self.registry:
            routes[prefix] = list_name.format(basename=basename)

        routes.update(self.extra_links)

        class APIRoot(views.APIView):
            _ignore_model_permissions = True
            exclude_from_schema = True

            def get(self, request, *args, **kwargs):
                ret = OrderedDict()
                namespace = request.resolver_match.namespace
                for prefix, view_name in routes.items():
                    if namespace:
                        view_name = namespace + ':' + view_name
                    ret[prefix] = reverse(
                        view_name,
                        args=args,
                        kwargs=kwargs,
                        request=request,
                        format=kwargs.get('format')
                    )
                return Response(ret)

        return APIRoot.as_view()
