from django.apps import AppConfig
from django.utils.functional import cached_property

class PluginApp(AppConfig):
    name = 'pretix_shaticketoutputpdf'
    verbose_name = 'SHA PDF ticket output'

    class PretixPluginMeta:
        name = 'SHA PDF ticket output'
        author = 'Martin Gross, the pretix team'
        description = 'This plugin allows you to print out tickets as PDF files - with the addition of SHA-related tax-stuff'
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA

    @cached_property
    def compatibility_errors(self):
        errs = []
        try:
            import reportlab  # NOQA
        except ImportError:
            errs.append("Python package 'reportlab' is not installed.")
        return errs


default_app_config = 'pretix_shaticketoutputpdf.PluginApp'
