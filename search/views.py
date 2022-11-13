from django.shortcuts import render
def search(request):
    return render(
        request,
        'search/search_page.html',
    )

def recommend(request):
    return render(
        request,
        'search/recommend.html'
    )

def search_list(request):
    return render(
        request,
        'search/search_list.html'
    )
def search_detail(request):
    return render(
        request,
        'search/search_detail.html'
    )
