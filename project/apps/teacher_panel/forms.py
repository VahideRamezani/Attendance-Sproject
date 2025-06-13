from django import forms
from apps.login.models import classes, students, teachers, subjects, teacher_class_subject, attendance


class TeacherFilterForm(forms.Form):
    class_id = forms.ModelChoiceField(
        queryset=classes.objects.none(),
        required=False,
        label='کلاس',
        empty_label='همه کلاس‌ها',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'onchange': 'this.form.submit()'
        })
    )

    subject_id = forms.ModelChoiceField(
        queryset=subjects.objects.none(),
        required=False,
        label='درس',
        empty_label='همه درس‌ها',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'onchange': 'this.form.submit()'
        })
    )

    def __init__(self, *args, **kwargs):
        self.teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)

        if self.teacher:
            # دریافت کلاس‌ها و درس‌های مربوط به معلم
            teacher_classes = teacher_class_subject.objects.filter(
                teacher_id=self.teacher
            ).select_related('class_id', 'subject_id')

            self.fields['class_id'].queryset = classes.objects.filter(
                class_id__in=teacher_classes.values_list('class_id', flat=True)
            ).distinct().order_by('class_name')

            self.fields['subject_id'].queryset = subjects.objects.filter(
                subject_id__in=teacher_classes.values_list('subject_id', flat=True)
            ).distinct().order_by('subject_name')