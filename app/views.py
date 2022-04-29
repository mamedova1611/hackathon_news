from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic, View

from .forms import  CommentForm
from .models import Predpriyatie, News, Tag

class IndexView(generic.ListView):
    model = Predpriyatie
    template_name = 'main.html'
    context_object_name = 'predpriyatie'

class HistoryView(View):
    def get(self, request, pk):
        predpriyatie = Predpriyatie.objects.get(bin_id__contains=pk)
        return render(request, 'history.html', {'predpriyatie': predpriyatie})

class NewsView(View):
    def get(self, request, pk):
        news = News.objects.filter(bin_news__bin_id__contains=pk)
        tags = Tag.objects.all()
        tag = self.request.GET.get('tag')
        if tag:
            news = news.filter(tags__tag=tag)
        search = self.request.GET.get('search')
        if search:
            news = news.filter(title__contains=search)
        if search:
            news = news.filter(content__contains=search)
        return render(request, 'news_list.html', {'news': news, 'tag': tags})


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        news_object = self.get_object()
        context['existing_comments'] = news_object.news.all()
        return context

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.news_id = pk
            comment.save()
            return HttpResponseRedirect(reverse('news_detail', args=[pk]))
        return render(request, 'news_detail.html', {'comment_form': comment_form})

