from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from portfolio.forms import ContactForm
from portfolio.models import Post, MyWork, Biography, Skill, Testimonial, About


class PortfolioView(ListView):
    model = Post
    form_class = ContactForm
    initial = {'key': 'value'}
    paginate_by = 4
    template_name = 'home.html'

    @staticmethod
    def get_my_video():
        return MyWork.objects.all()

    @staticmethod
    def get_biography():
        return Biography.objects.all()

    @staticmethod
    def get_skills():
        return Skill.objects.all()

    @staticmethod
    def get_testimonials():
        return Testimonial.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(initial=self.initial)
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Новая заявка с сайта rusina.my-cv.xyz'

            recipients = ['titov.nikita.work@gmail.com']
            try:
                send_mail(subject, first_name + " " + last_name + "\n\n" + message + "\n\n" + email,
                          'titov.nikita.uber@yandex.ru', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class PortfolioDetailView(DetailView):
    model = Post
    about = About
    template_name = 'post_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.get(pk=1)
        return context


class AboutDetailView(ListView):
    model = About
    template_name = 'about_me.html'
