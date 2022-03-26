from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Article, Comment
from .forms import CommentForm


# Create your views here.
# Function based view for landing page:
def landing_page(request):
    """
    Function Based view for displaying landing page to users
    """
    return render(request, 'landing_page.html')


# Credits: Website Views adapted from Code Insitute Django Blog lesson
# Added annotation to queryset to enable comment totals on index.html template
class ArticleList(generic.ListView):
    """
    Article List Class Based View for displaying current article inventory
    """
    model = Article
    queryset = Article.objects.filter(status=1).order_by(
        '-created_on').annotate(comment_count=Count('comments__article'))
    template_name = 'index.html'
    paginate_by = 6

# Credits: Website Views adapted from Code Insitute Django Blog lesson


class ArticleDetail(View):
    """
    Article Detail Class Based View for displaying selected article's detail
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Get method to pull in comments, likes and article content detail
        """
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(
            approved=True).order_by('created_on')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        template = "article_detail.html"

        context = {
            "article": article,
            "comments": comments,
            "commented": False,
            "liked": liked,
            "comment_form": CommentForm()
        }

        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        """
        Post method to add comments and likes
        """
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(
            approved=True).order_by('created_on')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()

        template = "article_detail.html"

        context = {
            "article": article,
            "comments": comments,
            "commented": True,
            "liked": liked,
            "comment_form": CommentForm()
        }

        return render(request, template, context)


class ArticleLike(View):
    """
    Article Like Class Based View for managing the like an unlike actions
    """
    def post(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))
