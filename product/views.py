from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductReview
from .cart import Cart

# Create your views here.


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')


def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1
        cart = Cart(request)
        cart.add(product_id, quantity, True)

    return redirect('cart_view')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)

    return redirect('cart_view')


def cart_view(request):
    cart = Cart(request)
    return render(request, 'product/cart_view.html', {
        'cart': cart
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)  # url representation

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')
        review_image = request.POST.get('review_image', request.FILES)

        if content:
            reviews = ProductReview.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.review_image = review_image
                review.save()
            else:
                review = ProductReview.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    review_image=review_image,
                    created_by=request.user
                )
            return redirect('product_detail', slug=slug)

    return render(request, 'product/product_detail.html', {
        'product': product
    })
