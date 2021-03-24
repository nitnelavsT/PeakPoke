from django.views.generic import TemplateView, CreateView


class HomeView(TemplateView):
    template_name = 'common/home.html'