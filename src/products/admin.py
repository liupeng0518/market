# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Product, Category, ProductImage, Tag, CategoryImage


class CategoryImageInline(admin.TabularInline):
    model = CategoryImage


class TagInline(admin.TabularInline):
    prepopulated_fields = {"slug": ('tag',)}
    extra = 1
    model = Tag


class ProductImageInline(admin.TabularInline):
    extra = 1
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'description', 'current_price', 'order', 'categories', 'live_link')

    # 外键关联
    inlines = [TagInline, ProductImageInline]

    # search_fields可以根据传进去的字段进行搜索
    search_fields = ['title', 'description', 'price',
                     'category__title', 'category__description', 'tag__tag']

    # list_filter会在右侧添加一个filter sidebar，可以快捷的进行过滤
    list_filter = ['price', 'timestamp', 'updated']

    # 设置预填充字段
    prepopulated_fields = {"slug": ('title',)}

    # fields = ['title', 'slug', ]
    # 只读字段
    readonly_fields = ['categories', 'live_link', 'timestamp', 'updated']

    class Meta:
        model = Product

    def current_price(self, obj):
        if obj.sale_price > 0:
            return obj.sale_price
        else:
            return obj.price

    def categories(self, obj):
        cat = []
        for i in obj.category_set.all():
            link = "<a href='/admin/products/category/" + \
                str(i.id) + "'>" + i.title + "</a>"
            cat.append(link)
        return ", ".join(cat)

    categories.allow_tags = True

    def live_link(self, obj):

        # link = "<a href='/products/" + str(obj.id) + "'>" + obj.title + "</a>"
        link = "<a href='/products/" + obj.slug + "'>" + obj.title + "</a>"

        return link

    live_link.allow_tags = True

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    inlines = [CategoryImageInline]

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)
