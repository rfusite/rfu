from django.contrib.flatpages.models import FlatPage
from ckeditor.fields import RichTextField


class RichTextFlatPage(FlatPage):
    rich_content = RichTextField()
