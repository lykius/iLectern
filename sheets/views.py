from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
import os.path
from .models import Sheet
from .forms import SheetForm

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
        directory = '/media/sheets/' + filename + '/'
        images = []
        for i in range(0, sheet.number_of_pages):
            images.append(directory + str(i) + '.jpg')
        context = self.get_context_data(**kwargs)
        context['sheet'] = sheet
        context['images'] = images
        return self.render_to_response(context)

class SheetFormView(SuccessMessageMixin, FormView):
    template_name = 'sheets/add.html'
    form_class = SheetForm
    success_url = reverse_lazy('list')
    success_message = 'Sheet was added successfully'

    def form_valid(self, form):
        self._save_sheet(form)
        return super(SheetFormView, self).form_valid(form)

    def _save_sheet(self, form):
        self.object = form.save(commit=False)
        # load and process pdf file
        self.object.title = 'titolo' # test
        self.object.file_name = 'file' # test
        self.object.number_of_pages = 45 # test
        self.object.save()
