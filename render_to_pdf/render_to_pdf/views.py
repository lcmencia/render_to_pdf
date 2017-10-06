from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf #created in step 4

from django.template.loader import get_template
class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        context = {
             "invoice_id": 123,
             "customer_name": "Abel Ledezma",
             "amount": 1399.99,
             "today": "Today",
         }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")