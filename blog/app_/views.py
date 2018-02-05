from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index_page(request):
    return HttpResponse("Hello world")


def detail_page(request, page_id: str):
    """详情页面
    """
    return HttpResponse(page_id)