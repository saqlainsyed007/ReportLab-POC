# from django.shortcuts import render
from django.http import HttpResponse
from .utils import create_fund_report


# Create your views here.
def generate_pdf(self):
    # create pdf
    pdf = create_fund_report()
    # generate response
    response = HttpResponse(pdf, content_type="application/pdf")
    # 'inline' to open pdf. Use 'attachment' to download
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    outfilename = 'report.pdf'
    open(outfilename, 'wb').write(pdf)
    return response
