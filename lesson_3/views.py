from os import path
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.views import View
from django.template import loader


FILE_PATH = path.join(path.realpath(path.dirname(__file__)), 'static', 'lesson_3', 'Tymofii.jpg')


class MyView(View):

    def get(self, request):
        if request.GET.get('type') == "file":
            return FileResponse(open(FILE_PATH, "rb+"))
        elif request.GET.get('type') == "json":
            return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
        elif request.GET.get('type') == "redirect":
            return HttpResponseRedirect("http://127.0.0.1:8000/admin")
        else:
            return HttpResponseNotAllowed("You shall not pass!!!")

    def post(self, request):
        print(request.POST)
        return HttpResponse("This is POST")


def root(request):
    # return HttpResponse("<button>Some Button</button>")
    """
    test_template = loader.get_template(template_name="templates_example.html")
    test_template_list = loader.select_template(template_name_list=["test", "templates_example.html"])
    HttpResponse(test_template.render())
    test_template = loader.render_to_string("templates_example.html",
                                            context={
                                                "str": "Test String",
                                                "int": 12
                                            })
    HttpResponse(test_template)
    :param request:
    :return:
    """
    return render(request, "root.html")


def text(request):
    return HttpResponse("This is text from backend to user interface")


def file(request):
    return FileResponse(open(FILE_PATH, "rb+"))


def redirect(request):
    return HttpResponseRedirect("http://google.com")


def not_allowed(request):
    return HttpResponseNotAllowed("You shall not pass!!!")


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
