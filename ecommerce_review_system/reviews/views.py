from django.contrib import messages
from django.db.models import Avg
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from .forms import ReviewForm
from .models import Product, Review


class ProductListView(View):
   
    def get(self, request):
   
        products = Product.objects.all()
   
        return render(request, 'reviews/product_list.html', {'products': products})


class ReviewListView(View):
   
    def get(self, request, product_id):
   
        product = Product.objects.filter(pk=product_id).first()
   
        if not product:
   
            raise Http404

        reviews = product.reviews.all()
   
        return render(request, 'reviews/review_list.html', {
   
            'product': product,
   
            'reviews': reviews,
        })


class ReviewCreateView(View):
   
    def get(self, request, product_id):
   
        product = Product.objects.filter(pk=product_id).first()
   
        if not product:
            raise Http404

   
        form = ReviewForm()
   
        return render(request, 'reviews/add_review.html', {
   
            'product': product,
   
            'form': form,
   
        })

    def post(self, request, product_id):
   
        product = Product.objects.filter(pk=product_id).first()
   
        if not product:
   
            raise Http404

        form = ReviewForm(request.POST)
   
        if form.is_valid():
   
            review = form.save(commit=False)
   
            review.product = product
   
            review.save()
   
            messages.success(request, 'Your review was added successfully!')
   
            return redirect('review_list', product_id=product.id)

        return render(request, 'reviews/add_review.html', {
   
            'product': product,
   
            'form': form,
        })


class ReviewDeleteView(View):
   
    def post(self, request, review_id):
   
        review = Review.objects.filter(pk=review_id).first()
   
        if not review:
   
            raise Http404

        product_id = review.product_id

        review.delete()

        messages.success(request, 'The review was deleted successfully!')

        return redirect('review_list', product_id=product_id)


class ProductRatingsView(View):

    def get(self, request):
    
        products = Product.objects.annotate(average_rating=Avg('reviews__rating'))
    
        return render(request, 'reviews/product_ratings.html', {'products': products})
