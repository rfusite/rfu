from django.forms.widgets import Select
from django.utils.html import format_html


class ImagePatternSelect(Select):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs)

    def render_option(self, selected_choices, option_value, option_label):
        if option_value:
            img_html = format_html('<img src="/static/pattern/{}" style="height: 50px; width: auto; margin-right: 10px;" />', option_value)
            return format_html('<option value="{}"{}>{}{}</option>',
                               option_value,
                               (' selected="selected"' if option_value in selected_choices else ''),
                               img_html,
                               option_label)
        else:
            return super().render_option(selected_choices, option_value, option_label)
