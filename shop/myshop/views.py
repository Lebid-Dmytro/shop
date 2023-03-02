from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from cart.forms import CartAddProductForm
from .forms import CommentForm

from .models import Category, Product


def product(request, category_slug=None):
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


def detail(request, id):
    product = Product.objects.get(pk=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def add_comment(request, id):
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        form = form.save(commit=False)
        if request.POST.get('parent', None):
            form.parent_id = int(request.POST.get('parent'))
        form.product_id = id
        form.save()
        return redirect('/')

