from django import forms

class UserTypeChoiceForm(forms.Form):
    user_type = forms.fields.ChoiceField(
        choices = (
            ('All', '選択なし'),
            ('Admin', '管理者'),
            ('User', '一般ユーザ')
        ),
        required=True,
        widget=forms.widgets.Select
    )

    def __init__(self, *args, **kwargs):
        selected_option = kwargs.pop('selected_option', None)
        super().__init__(*args, **kwargs)
        self.fields['user_type'].widget.attrs.update({'class': 'custom-select'})
        if selected_option:
            self.fields['user_type'].initial = selected_option
