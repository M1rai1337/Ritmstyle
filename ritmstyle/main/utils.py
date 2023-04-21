from .forms import *
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect


class Mixin:
    form_class = VisitForm
    template_name = None

    def mixin_get(self, request, *args, **kwargs):
        form = self.form_class()
        kwargs['form'] = form
        kwargs['modal'] = ''
        return render(request, self.template_name, kwargs)

    def mixin_post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/thanks/')

        kwargs['form'] = form
        kwargs['modal'] = 'open'
        return render(request, self.template_name, kwargs)
