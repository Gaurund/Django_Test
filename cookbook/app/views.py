from django.shortcuts import render


# Create your views here.

def index(request):
    template_name = "app/index.html"

    context = {
        'title': 'Проба пера. Видоплясов'
    }

    return render(
        request,
        template_name,
        context
    )