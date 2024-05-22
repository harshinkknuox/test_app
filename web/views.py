from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView, TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from web.models import User
from .forms import UserAddForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.

class IndexView(ListView):
    model = User
    template_name = 'web/index.html'
    context_object_name = 'users'

class AddUserView(CreateView):
    model = User
    template_name = 'web/add_user.html'
    form_class = UserAddForm
    success_url = reverse_lazy('web:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        context['users'] = users
        return context


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            users = User.objects.all()
            context = {'users': users}
            user_list_html = render_to_string('web/user_list.html', context)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'user_list_html': user_list_html})
            else:
                return HttpResponse(user_list_html)
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
            else:
                return self.form_invalid(form)


class UserDetailView(DetailView):
    model= User
    template_name = 'web/user_detail.html'
    context_object_name = 'user_detail'


#return JsonResponse({'success': True, 'user_list_html': user_list_html})

# def post(self, request):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         users = User.objects.all()
    #         context = {'users': users}
    #         user_list_html = render_to_string('web/user_list.html', context)
    #     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    #         print('***'*10)
    #         return JsonResponse({'success': False, 'errors': form.errors})
    #     return HttpResponse(user_list_html)