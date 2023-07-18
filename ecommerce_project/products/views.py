from django.shortcuts import render


# Create your views here.
def productsDetail(request):
    return render(request, "productdetail.html")