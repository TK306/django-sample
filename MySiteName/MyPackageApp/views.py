from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import MyPythonPackage as mpp

# Create your views here.


@login_required
def index_view(request):
    print(mpp)
    return render(request, "my-package-app/index.html")


@login_required
def setting_view(request):
    return render(request, "my-package-app/setting.html")


@login_required
def feature1_view(request):
    initial_context = {
        "people": [
            {
                "name": "おのおのおの",
                "org": "代1開発部第9開発科",
                "tag": ["tag1", "tag2"],
                "checked": "",
            },
            {"name": "かの", "org": "総務", "tag": ["tag1"], "checked": ""},
            {"name": "げろげろ", "org": "雑魚", "tag": [], "checked": ""},
        ]
    }  # checkedの情報はいらない
    if request.method == "POST":
        if "tagPushed" in request.POST:
            selectedTag = request.POST["tagPushed"]
            context = initial_context.copy()
            for p in context["people"]:
                if selectedTag in p["tag"]:
                    p["checked"] = "checked"
                else:
                    p["checked"] = ""
            return render(request, "my-package-app/feature1.html", context)
        for c in request.POST.getlist("view_check"):
            print(c)

    return render(request, "my-package-app/feature1.html", initial_context)


@login_required
def feature2_view(request):
    return render(request, "my-package-app/feature2.html")
