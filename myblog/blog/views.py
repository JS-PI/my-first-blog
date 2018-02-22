from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html',
                  {
                      'name': ''
                  })

def post_detail(request, id):
    return HttpResponse('blog post_detail 뷰 호출하고 {}번 글을 보여주겠습니다.'.format(id))
