from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse


class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())

        return render(request, 'login.html', {"message":"Please login first"})

    def post(self, request, *args, **kwargs):
        super(CustomLoginView, self).post(self,request, *args, **kwargs)

        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())

        return HttpResponseRedirect(reverse('login'))