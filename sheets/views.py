from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Sheet
import os.path

class SheetListView(TemplateView):
    template_name = 'sheets/list.html'

    def get(self, request, *args, **kwargs):
        sheets = Sheet.objects.all().order_by('title')
        context = self.get_context_data(**kwargs)
        context['sheets'] = sheets
        return self.render_to_response(context)

class SheetView(TemplateView):
    template_name = 'sheets/view.html'

    def get(self, request, *args, **kwargs):
        sheet = Sheet.objects.get(pk=kwargs['pk'])
        filename, extension = os.path.splitext(sheet.file_name)
        directory = 'sheets/archive/' + filename + '/'
        images = []
        for i in range(0, sheet.number_of_pages):
            images.append(directory + str(i) + '.jpg')
        context = self.get_context_data(**kwargs)
        context['sheet'] = sheet
        context['images'] = images
        return self.render_to_response(context)
