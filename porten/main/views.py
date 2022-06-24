from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Network, Main, Our
from django.core.paginator import Paginator
from django.conf import settings


def index(request):
    template = 'main/index.html'
    categories = Category.objects.all().order_by('-date_update')
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    ours = Our.objects.all()
    list_category = []
    for category in categories:
        list_category.append(category)
    category = list_category[1]
    category_2 = list_category[0]
    products_category = Product.objects.all().filter(category__slug=category.slug)
    paginator_category = Paginator(products_category, 3)
    page_number_category = request.GET.get('page')
    page_object_category = paginator_category.get_page(page_number_category)
    networks = Network.objects.all()
    list_network = []

    for net in networks:
        list_network.append(net)
    if len(list_network) >= 3:
            telegram = list_network[0]
            instagram = list_network[1]
            facebook = list_network[2]
    else:
            telegram = '##'
            instagram ='##'
            facebook = '##'
    main = Main.objects.all()
    context = {
        'categories': categories,
        'page_object': page_object,
        'category': category,
        'products_category': products_category,
        'page_object_category': page_object_category,
        'category_2': category_2,
        'telegram': telegram,
        'instagram': instagram,
        'facebook': facebook,
        'main': main,
        'ours': ours,
    }
    return render(request, template, context)


def category_detail(request, category_slug):
    template = 'main/category_detail.html'
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.all().filter(category__slug=category.slug)
    categories = Category.objects.all()
    networks = Network.objects.all()
    ours = Our.objects.all()

    list_network = []
    for net in networks:
        list_network.append(net)
    if list_network[0] and list_network[1] and list_network[2]:
        telegram = list_network[0]
        instagram = list_network[1]
        facebook = list_network[2]
    else:
        telegram = '##'
        instagram = '##'
        facebook = '##'
    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'telegram': telegram,
        'instagram': instagram,
        'facebook': facebook,
        'ours': ours,

    }
    return render(request, template, context)


def products(request):
    template = 'main/category_detail.html'
    products = Product.objects.all()
    categories = Category.objects.all()
    networks = Network.objects.all()
    ours = Our.objects.all()

    list_network = []
    for net in networks:
        list_network.append(net)
    if list_network[0] and list_network[1] and list_network[2]:
        telegram = list_network[0]
        instagram = list_network[1]
        facebook = list_network[2]
    else:
        telegram = '##'
        instagram = '##'
        facebook = '##'
    context = {
        'products': products,
        'categories': categories,
        'telegram': telegram,
        'instagram': instagram,
        'facebook': facebook,
        'ours': ours,
    }
    return render(request, template, context)


def categories(request):
    template = 'main/categories.html'
    categories = Category.objects.all()
    paginator = Paginator(categories, 8)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    networks = Network.objects.all()
    ours = Our.objects.all()

    list_network = []
    for net in networks:
        list_network.append(net)
    if list_network[0] and list_network[1] and list_network[2]:
        telegram = list_network[0]
        instagram = list_network[1]
        facebook = list_network[2]
    else:
        telegram = '##'
        instagram = '##'
        facebook = '##'
    context = {
        'categories': categories,
        'page_object': page_object,
        'telegram': telegram,
        'instagram': instagram,
        'facebook': facebook,
        'ours': ours,
    }
    return render(request, template, context)


def product_detail(request, category_slug, product_id):
    template = 'main/product_detail.html'
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    networks = Network.objects.all()
    ours = Our.objects.all()

    list_network = []
    for net in networks:
        list_network.append(net)
    if list_network[0] and list_network[1] and list_network[2]:
        telegram = list_network[0]
        instagram = list_network[1]
        facebook = list_network[2]
    else:
        telegram = '##'
        instagram = '##'
        facebook = '##'
    context = {
        'categories': categories,
        'category': category,
        'product': product,
        'telegram': telegram,
        'instagram': instagram,
        'facebook': facebook,
        'ours': ours,
    }
    return render(request, template, context)

