from django.dispatch import Signal, receiver
from django.template.loader import get_template
from django.urls import resolve

from pretix.base.signals import register_ticket_outputs
from pretix.control.signals import html_head


@receiver(register_ticket_outputs, dispatch_uid="output_shapdf")
def register_ticket_outputs(sender, **kwargs):
    from .ticketoutput import PdfTicketOutput
    return PdfTicketOutput


@receiver(html_head, dispatch_uid="shaticketoutputpdf_html_head")
def html_head_presale(sender, request=None, **kwargs):
    url = resolve(request.path_info)
    if url.namespace == 'plugins:pretix_shaticketoutputpdf':
        template = get_template('pretix_shaticketoutputpdf/control_head.html')
        return template.render({
            'request': request
        })
    else:
        return ""


register_fonts = Signal()
"""
Return a dictionaries of the following structure. Paths should be relative to static root.

{
    "font name": {
        "regular": {
            "truetype": "….ttf",
            "woff": "…",
            "woff2": "…"
        },
        "bold": {
            ...
        },
        "italic": {
            ...
        },
        "bolditalic": {
            ...
        }
    }
}
"""


def get_fonts():
    f = {}
    for recv, value in register_fonts.send(0):
        f.update(value)
    return f
