from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from search.models import Beer
from django.views.decorators.csrf import csrf_exempt
import logging

logger = logging.getLogger('tipper')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())



@csrf_exempt
def search(request):
    if request.method == 'GET':
        return render(request, "search/search_page.html")

    else:
        logger.info("=================search")
        logger.info(request.POST)
        beer_list = Beer.objects.all()  ###
        search = request.POST.get('search', '')
        search_list = []
        search_list = beer_list.filter(
            Q(name__icontains=search) |
            Q(brewery__icontains=search) |
            Q(country__icontains=search)
        )
        return render(request, "search/search_list.html", {'search_list': search_list, 'search': search})


@login_required
def search_detail(request, pk):
    search_detail = Beer.objects.get(id=pk)
    return render(request, "search/search_detail.html", {
        "search_details": search_detail,
    })


# 실행 불가. ###의 beer_list를 print 해 보았으나 beer(1), beer(2) 등의 object 형태로 구현
# 그래서 접근이 불가한 걸까?
## print(search) X, html에서 search와 search_list가 없다는 걸 보면... 담기지 않은 게 아닐까?
###로그에서 나타낸 검색 값은 무엇을 의미하는 건지?
def recommend(request):
    return render(
        request,
        'search/recommend.html'
    )


@login_required
def search_list(request):
    return render(
        request,
        'search/search_list.html'
    )
