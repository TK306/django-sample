from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index_view(request):
    return render(request, "my-package-app/index.html")


@login_required
def setting_view(request):
    return render(request, "my-package-app/setting.html")


@login_required
def feature1_view(request):
    return render(request, "my-package-app/feature1.html")


@login_required
def feature2_view(request):
    return render(request, "my-package-app/feature2.html")
