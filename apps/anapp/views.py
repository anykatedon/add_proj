from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'anapp/index.html', {})


def add(request):
    val1 = int(request.GET["num1"], 0)
    val2 = int(request.GET["num2"], 0)

    # return render(request, 'anapp/result.html', {'res': (val1+val2)})
    return render(request, 'anapp/index.html', {'res': (val1+val2)})
