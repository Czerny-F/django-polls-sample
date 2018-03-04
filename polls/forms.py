from django.forms import ModelForm
from django.forms.utils import ErrorList
from django.core.exceptions import ValidationError
from .models import Question


class QuestionForm(ModelForm):

    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, instance=None, use_required_attribute=None):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix,
                         empty_permitted, instance, use_required_attribute)

    def is_valid(self):
        print(type(self.instance))
        print(self.instance)
        return super().is_valid()

    def clean(self):
        print(type(self.instance))
        print(self.instance)
        raise ValidationError('no')
        return super().clean()
