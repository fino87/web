from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.contrib import auth
from forms import AskForm, AnswerForm, SignUpForm, LoginForm
from models import Question, Answer


def test(request, *args, **kwargs):
        return HttpResponse('OK')

@require_GET
def newQuestions(request):
    questions = Question.objects.order_by('-id')[:]
    (page, paginator) = myPaginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'qa/newQuestions.html', {
        'questions': page.object_list,
    })

@require_GET
def popularQuestions(request):
    questions = Question.objects.order_by('-rating')[:]
    (page, paginator) = myPaginate(request, questions)
    paginator.baseurl = '/popular/?page='
    return render(request, 'qa/newQuestions.html', {
        'questions': page.object_list,
    })

def questionById(request, qId):
    question = get_object_or_404(Question, id=qId)
    answers = Answer.objects.filter(question_id=qId)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if request.user is not None:
            form._user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AnswerForm(initial={'question': qId})
    return render(request, 'qa/questionById.html', {
                  'question': question,
                  'answers': answers[:],
                  'form': form
    })

def myPaginate(request, qs):
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return (page, paginator)


def askQuestion(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if request.user is not None:
            form._user = request.user
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, "qa/askNewQuestion.html", {
        "form": form
    })


@require_POST
def answerQuestion(request):
    form = AnswerForm(request.POST)
    if request.user is not None:
        form._user = request.user
    if form.is_valid():
        answer = form.save()
        return HttpResponseRedirect(answer.question.get_url())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = SignUpForm()
    return render(request, "qa/signUp.html", {
        "form": form
    })

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = LoginForm()
    return render(request, "qa/login.html", {
        "form": form
})


