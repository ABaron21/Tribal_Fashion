from django.shortcuts import render

# Create your views here.


def view_shopping_bag(request):
    template = 'shopping_bag/view_bag.html'
    return render(request, template)
