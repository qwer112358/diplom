from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from main.models import Profession, Question, Answer, Tag, Interview, Skill


def base(request):
    return render(request, 'main/base.html')


class Home(ListView):
    model = Profession
    template_name = 'main/index.html'


def home(request):
    professions = Profession.objects.all()
    context = {
        'object_list': professions
    }
    return render(request, 'main/index.html', context)

class QuestionList(ListView):
    model = Question
    template_name = 'main/questions.html'
    context_object_name = 'questions'

    def get_queryset(self):
        profession_slug = self.kwargs['profession_slug']
        self.profession = get_object_or_404(Profession, slug=profession_slug)
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort', 'chance')
        order = self.request.GET.get('order', 'desc')

        # Define sorting options
        sort_options = {
            'chance': 'chance',
            'title': 'title',
            'tag': 'tag__title'
        }

        # Default sorting
        sort_by = sort_options.get(sort, 'chance')
        if order == 'desc':
            sort_by = f'-{sort_by}'

        queryset = Question.objects.filter(profession=self.profession)
        if tag:
            queryset = queryset.filter(tag__title=tag)
        return queryset.order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profession'] = self.profession.title
        context['tags'] = Tag.objects.filter(professions=self.profession)
        return context


class QuestionDetail(DetailView):
    model = Question
    template_name = 'main/question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Mock(ListView):
    model = Interview
    template_name = 'main/mock.html'
    context_object_name = 'interviews'

    def get_queryset(self):
        tag = self.request.GET.get('tag')
        sort = self.request.GET.get('sort', 'title')
        order = self.request.GET.get('order', 'asc')

        # Define sorting options
        sort_options = {
            'title': 'title',
            'profession': 'profession__title',
            'tag': 'tag__title'
        }

        # Default sorting
        sort_by = sort_options.get(sort, 'title')
        if order == 'desc':
            sort_by = f'-{sort_by}'

        queryset = Interview.objects.all()
        if tag:
            queryset = queryset.filter(tag__title=tag)
        return queryset.order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


def practice(request):
    return render(request, 'main/practice/practice.html')


def frontend(request):
    return render(request, 'main/practice/frontend.html')


def python(request):
    return render(request, 'main/practice/python.html')

'''
class RequirementList(ListView):
    model = Skill
    template_name = 'main/mock.html'
    context_object_name = 'interviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skill'] = self.profession.title
        return context
'''


class RequirementList(ListView):
    model = Skill
    template_name = 'main/requirements.html'
    context_object_name = 'skills'

    def get_queryset(self):
        profession_id = self.kwargs.get('profession_id')
        self.profession = get_object_or_404(Profession, id=profession_id)
        return Skill.objects.filter(profession=self.profession)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profession'] = self.profession.title
        return context


class Requirements(ListView):
    model = Profession
    template_name = 'main/requirements.html'


def requirement_list(request, profession_slug):
    if profession_slug in ('python_developer', '1C'):
        return render(request, f'main/requirements/{profession_slug}.html')

    return render(request, f'main/base.html')



