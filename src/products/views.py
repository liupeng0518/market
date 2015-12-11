# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, RequestContext, Http404, render, HttpResponseRedirect
from django.template.defaultfilters import slugify
<<<<<<< HEAD

=======
>>>>>>> develop
from django.forms.models import modelformset_factory
from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm

<<<<<<< HEAD

=======
>>>>>>> develop
# Create your views here.

def list_all(request):
    # products = Product.objects.all()
    products = Product.objects.filter(active=True)

    return render_to_response("products/all.html", locals(), context_instance=RequestContext(request))
<<<<<<< HEAD
=======

>>>>>>> develop
    # render实现
    # return render(request, "products/all.html", locals())


def add_product(request):

    form = ProductForm(request.POST or None)

    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.slug = slugify(form.cleaned_data['title'])
        product.active = False
        product.save()
        return HttpResponseRedirect('/products/%s' % (product.slug))

    return render_to_response("products/edit.html", locals(), context_instance=RequestContext(request))


def manage_product_image(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except:
        product = False

    if request.user == product.user:
        queryset = ProductImage.objects.filter(product__slug=slug)
        ProductImageFormset = modelformset_factory(
            ProductImage, form=ProductImageForm, extra=0, can_delete=True)
        formset = ProductImageFormset(
            request.POST or None, request.FILES or None, queryset=queryset)
        form = ProductImageForm(request.POST or None)

        if formset.is_valid():
            for form in formset:
                instance = form.save(commit=False)
                instance.save()
            if formset.deleted_forms:
                formset.save()

        return render_to_response("products/manage_images.html", locals(), context_instance=RequestContext(request))

    else:
        raise Http404


def edit_product(request, slug):
    instance = Product.objects.get(slug=slug)
    if request.user == instance.user:
        form = ProductForm(request.POST or None, instance=instance)

        if form.is_valid():
            product_edit = form.save(commit=False)
            product_edit.save()
        return render_to_response("products/edit.html", locals(), context_instance=RequestContext(request))

    else:
        raise Http404


def single(request, slug):
    # product = Product.objects.all()[0]
    product = Product.objects.get(slug=slug)

    # if request.user == product.user:
    #     categories = product.category_set.all()

    #     context = {
    #         "product": product,
    #         "categories": categories,
    #         "edit": True,
    #     }
    # else:
    #     context = {
    #         "product": product,
    #     }

    images = product.productimage_set.all()

    categories = product.category_set.all()
    context = {
        "product": product,
        "categories": categories,
        "edit": True,
        "images": images,
    }

    return render_to_response("products/single.html", context, context_instance=RequestContext(request))
