from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {"insert_content": "Hello i am from thirdapp"}
    return render(request, "thirdapp/index.html", context=my_dict)
