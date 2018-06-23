from django.http import HttpResponseRedirect
from django.templatetags.static import static


def favicon(request):
    return HttpResponseRedirect(static('web/img/favicon.ico'))
