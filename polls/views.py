from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Question
'''
每个视图必须要做的只有两件事：返回一个包含被请求页面内容的 HttpResponse 对象，
或者抛出一个异常，比如 Http404 
所有的视图都要添加到polls.urls模块里,只要添加几个url()函数调用
'''
# Create your views here.
#索引界面
'''
一个快捷函数： render()
直接载入模板(不再需要template=...)，填充上下文，再返回由它生成的 HttpResponse 对象」是一个非常常用的操作流程。
于是 Django 提供了一个快捷函数，我们用它来重写 index() 视图：
'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]#显示最新的五个问题
    #template = loader.get_template('polls/index.html')#载入polls/index.html模板文件
    context = {#并向它传递一个上下文context
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

'''
一个快捷函数： get_object_or_404()
尝试用 get() 函数获取一个对象，如果不存在就抛出 Http404 错误也是一个普遍的流程。
Django 也提供了一个快捷函数，下面是修改后的详情 detail() 视图代码：
'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

