from django import forms


class SLoginForm(forms.Form):
    st_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-1 md:py-3 text-lg border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90' ,
        'placeholder':'کد ملی خود را به طور کامل وارد کنید' }))
    st_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full px-4 py-1 md:py-3 text-lg border border-gray-300 rounded-2xl focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white/90',
        'placeholder' : 'رمز عبور شما همان کد ملی شما می باشد'}))
