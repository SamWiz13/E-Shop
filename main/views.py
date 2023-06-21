from django.shortcuts import render
from django.views import View
from products.models import Product, Category
from django.shortcuts import get_object_or_404



def for_all_pages(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return  context


class IndexView(View):
    def get(self, request):
        products =Product.objects.all()
        
        q =request.GET.get('q')
        if q:
            products = products.filter(title__icontains=q)

        context = {
            'products': products
        
        }

        return render(request, 'index.html', context)


class CategoryView(View):
    def get(self, request, category_name):
        category =get_object_or_404(Category, name = category_name)

        q =request.GET.get('q')
        if q:
            products = products.filter(title__icontains=q)

        products = Product.objects.filter(category = category)
        context = {
            'category': category,
            'products': products
        }

        return render(request, 'category.html', context)