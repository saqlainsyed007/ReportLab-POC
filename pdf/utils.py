import os
import preppy
import StringIO
from rlextra.rml2pdf import rml2pdf
from core.settings import RML_DIR
from core.settings import RML_STATIC_DIR


def create_fund_report():
    template_file = preppy.getModule(os.path.join(RML_DIR, 'report.prep'))
    context = {}
    context['name'] = '<span>Syed Saqlain</span>'
    context['company'] = 'Gale Creative Agency Pvt Ltd'
    context['RML_DIR'] = RML_DIR
    context['RML_STATIC_DIR'] = RML_STATIC_DIR
    context['line_chart_data'] = get_line_chart_data()
    context['line_plot_data'] = get_line_plot_data()
    context['bar_chart_categories'] = get_bar_chart_data()['categories']
    context['bar_chart_values'] = get_bar_chart_data()['values']
    context['pie_chart_labels'] = get_pie_chart_data()['labels']
    context['pie_chart_data'] = get_pie_chart_data()['data']
    rml = template_file.getOutput(context)

    buf = StringIO.StringIO()
    rml2pdf.go(rml, outputFileName=buf)

    return buf.getvalue()


def get_line_chart_data():
    return [[('20120101', -12), ('20120201', 43), ('20120301', 21), ('20120401', -39), ('20120501', 64), ('20120601', 46), ('20120701', 98), ('20120801', 67)],
            [('20120101', 9), ('20120201', -72), ('20120301', 43), ('20120401', 77), ('20120501', -13), ('20120601', 53), ('20120701', 21), ('20120801', 45)]]


def get_line_plot_data():
    return [[('20120101', -12), ('20120201', 43), ('20120301', 21), ('20120401', -39), ('20120501', 64), ('20120601', 46), ('20120701', 98), ('20120801', 67)],
            [('20120101', 9), ('20120201', -72), ('20120301', 43), ('20120401', 77), ('20120501', -13), ('20120601', 53), ('20120701', 21), ('20120801', 45)]]


def get_bar_chart_data():
    return {
        'categories': ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8', 'cat9', 'cat10'],
        'values': [[5, 1, -10, 16, 13, 19, 8, 15, -4, 9], [6, 2, 3, 6, 9, 11, 16, 11, 19, 14]]
    }


def get_pie_chart_data():
    return {
        'labels': ['label1', 'label2', 'label3', 'label4', 'label5', 'label6'],
        'data': [12, 32, 28, 64, 43, 225]
    }
