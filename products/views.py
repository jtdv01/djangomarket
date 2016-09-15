from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
# Create your views here.


def detail_slug_view(request,slug=None):
    try:
        product = get_object_or_404(Product,slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()

    template = "detail_slug_view.html"
    context = {
        "object": product
    }
    return render(request,template,context)


def detail_view(request,object_id=None):
    if object_id is not None:
        product = get_object_or_404(Product,id=object_id)
        # try:
        #     product = Product.objects.get(id=object_id)
        # except Product.DoesNotExist:
        #     product = None

        template = "detail_view.html"
        context = {
            "object": product
        }
        return render(request,template,context)
    else:
        raise Http404

    # if request.user.is_authenticated():
    #     product = Product.objects.all().first()
    #
    #     template = "detail_view.html"
    #     context = {
    #         "title":"foo",
    #         "product": product
    #     }
    # else:
    #     template = "not_found.html"
    #     context = {}
    # return render(request,template,context)


def list_view(request):
    template = "list_view.html"
    queryset = Product.objects.all()
    context ={"queryset":queryset}
    return render(request,template,context)
