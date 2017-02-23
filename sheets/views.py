from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os.path
from .models import Sheet
from .utility import convert_pdf_to_image
from .utility import count_images_in_dir

class SheetListView(TemplateView):
    template_name = 'sheets/list.html'

    def _check_title_and_pdf_file(self, title, pdffile):
        return True

    def _process_and_save_pdf_file(self, pk, pdffile):
        ok = True
        try:
            newdir = os.path.join(settings.SHEETS_MEDIA_ROOT, str(pk))
            os.mkdir(newdir)
            fs = FileSystemStorage(location=newdir)
            filename = fs.save(pdffile.name, pdffile)
            newfile = os.path.join(newdir, filename)
            convert_pdf_to_image(newfile, newdir)
            fs.delete(newfile)
        except:
            ok = False
        return ok

    def get_context_data(self, **kwargs):
        context = super(SheetListView, self).get_context_data(**kwargs)
        sheets = Sheet.objects.all().order_by('title')
        context['sheets'] = sheets
        return context

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title', '')
        pdffile = request.FILES['pdffile']
        if (self._check_title_and_pdf_file(title, pdffile)):
            newsheet = Sheet.objects.create(title=title)
            self._process_and_save_pdf_file(newsheet.pk, pdffile)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class SheetView(TemplateView):
    template_name = 'sheets/view.html'

    def get(self, request, *args, **kwargs):
        sheet = Sheet.objects.get(pk=kwargs['pk'])
        dir = os.path.join(settings.SHEETS_MEDIA_ROOT, str(sheet.pk))
        images = []
        for i in range(count_images_in_dir(dir)):
            images.append('/media/sheets/' + str(sheet.pk) + '/' + str(i) + '.jpg')
        context = self.get_context_data(**kwargs)
        context['sheet'] = sheet
        context['images'] = images
        return self.render_to_response(context)
