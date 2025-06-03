from django import forms
from captcha.fields import CaptchaField, CaptchaTextInput


class SLoginForm(forms.Form):
    st_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-1 md:py-3 text-lg border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder': 'کد ملی خود را به طور کامل وارد کنید'}))
    st_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-1 md:py-3 text-lg border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder': 'رمز عبور شما همان کد ملی شما می باشد'}))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={
        'class': 'w-full sm:w-3/5 md:w-2/3 lg:w-3/4 xl:w-3/4 px-4 py-3 text-lg border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90 text-right',
        'placeholder': 'کد امنیتی',
        'style': 'direction: rtl; text-align: right;',
        'direction': 'rtl',
    }))


class TLoginForm(forms.Form):
    teacher_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'col-span-9 px-4 py-2 md:py-3 text-lg border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder': 'کد پرسنلی خود را به طور کامل وارد کنید'}))
    teacher_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'col-span-9 px-4 py-2 md:py-3 text-lg border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder': 'رمز عبور شما همان کد پرسنلی شما می باشد'}))
    captcha = CaptchaField(widget=CaptchaTextInput(
        attrs={}))
