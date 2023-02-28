from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from cart.forms import CartAddProductForm
from .forms import CommentForm

from .models import Category, Product


class ProductView(View):
    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()

        search_query = request.GET.get('search', '')

        if search_query:
            products = Product.objects.filter(available=True and Q(name__icontains=search_query) | Q(description__icontains=search_query))
        else:
            products = Product.objects.filter(available=True)

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop/product/list.html',
                      {
                          'category': category,
                          'categories': categories,
                          'products': products
                      })


class ProductDescriptionView(View):
    def get(self, request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        cart_product_form = CartAddProductForm()
        return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


class AddComments(View):
    '''Відгуки'''
    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.product_id = product
            form.save()
        return redirect(f'/{pk}')
