from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
import os.path
from .models import Sheet

class SheetListView(TemplateView):
    template_name = 'sheets/list.html'

    def get_context_data(self, **kwargs):
        context = super(SheetListView, self).get_context_data(**kwargs)
        sheets = Sheet.objects.all().order_by('title')
        context['sheets'] = sheets
        return context

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title', '')
        # file = request.POST.get('file', '')
        Sheet.objects.create(title=title, file_name='child.pdf', number_of_pages=2)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class SheetView(TemplateView):
    template_name = 'sheets/view.html'

    def get(self, request, *args, **kwargs):
        sheet = Sheet.objects.get(pk=kwargs['pk'])
        filename, extension = os.path.splitext(sheet.file_name)
        directory = '/media/sheets/' + filename + '/'
        images = []
        for i in range(0, sheet.number_of_pages):
            images.append(directory + str(i) + '.jpg')
        context = self.get_context_data(**kwargs)
        context['sheet'] = sheet
        context['images'] = images
        return self.render_to_response(context)
