from django.contrib import admin

from .models import Product, Review


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ('review_date',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image')
    search_fields = ('name',)
    inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'reviewer_name', 'rating', 'review_date')
    list_filter = ('rating', 'review_date')
    search_fields = ('reviewer_name', 'product__name')
