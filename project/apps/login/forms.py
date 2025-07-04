from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class SLoginForm(forms.Form):
    st_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-1 md:py-3 text-lg border border-gray-300 md:rounded-2xl rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder': 'کد ملی خود را به طور کامل وارد کنید'}))
    st_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-1 md:py-3 text-lg border border-gray-300 md:rounded-2xl rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
            'placeholder': 'رمز عبور شما همان کد ملی شما می باشد',
        })
    )
    captcha = CaptchaField(
        widget=CaptchaTextInput(attrs={
            'class': 'px-4 py-2 md:py-3 text-lg border border-gray-300 md:rounded-2xl rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90 w-full',
            'placeholder': 'کد امنیتی را وارد کنید',
        })
    )

class TLoginForm(forms.Form):
    teacher_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-span-9 px-4 py-2 md:py-3 text-lg border border-gray-300 md:rounded-2xl rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder': 'کد پرسنلی خود را به طور کامل وارد کنید'}))
    teacher_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'col-span-9 px-4 py-2 md:py-3 text-lg border border-gray-300 md:rounded-2xl rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder': 'رمز عبور شما همان کد پرسنلی شما می باشد'}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={
        'class': 'w-full px-4 py-2 md:py-3 text-lg border border-gray-300 md:rounded-2xl rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder': 'کد امنیتی را وارد کنید',
    }))

