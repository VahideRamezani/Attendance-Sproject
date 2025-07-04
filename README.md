# 🏫 سیستم حضور و غیاب هنرستان سمپاد سعدی

سامانه‌ای ساده برای مدیریت حضور و غیاب دانش‌آموزان، توسعه‌یافته با **Django** و **Tailwind CSS**. این پروژه هنوز در حال توسعه است و برخی قابلیت‌ها مانند پنل مدیریت (ادمین) هنوز اضافه نشده‌اند.

🎯 **هدف فعلی**  
امکان ثبت وضعیت حضور و غیاب توسط معلم، مشاهده‌ی لیست وضعیت هر کلاس، و بارگذاری گواهی (مثل مرخصی) توسط دانش‌آموز.



## 🧠 درباره‌ی پروژه

این سیستم به‌گونه‌ای طراحی شده که معلم‌ها به‌سادگی بتوانند وضعیت حضور دانش‌آموزان را ثبت و بررسی کنند. همچنین دانش‌آموزان می‌توانند گواهی‌های مربوط به غیبت خود را بارگذاری کنند.

📌 *نکته*:  
پروژه هنوز کامل نشده و امکانات مدیریتی (ادمین) در حال پیاده‌سازی است. کاربرد فعلی فقط برای تعامل بین معلم و دانش‌آموز در نظر گرفته شده است.



## 💻 تکنولوژی‌های استفاده‌شده

- **Back-end**: Django (پایتون)  
- **Front-end**: HTML / Tailwind CSS  + JavaScript



## 🚀 نحوه‌ی راه‌اندازی پروژه
1. کلون کردن مخزن:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2. ایجاد محیط مجازی و فعال‌سازی آن:


```bash
python -m venv venv
source venv/bin/activate     # در لینوکس یا مک
venv\Scripts\activate        # در ویندوز
```
3. نصب وابستگی‌ها:



```bash
pip install -r requirements.txt
```
4. اعمال مهاجرت‌های پایگاه‌داده:



```bash
python manage.py migrate
```
5. اجرای سرور توسعه:



```bash
python manage.py runserver
```
6. حالا می‌تونید به پروژه از طریق آدرس زیر در مرورگر دسترسی پیدا کنید:


```bash
http://127.0.0.1:8000/
```

## 👥 اعضای تیم
👤 وحیده رمضانی – توسعه‌ی فرانت‌اند و بک‌اند

👤 رسپینا جوادی مقدم – طراحی بک‌اند

👤 نرگس راشدی – طراحی ui/ux 

👤 ستایش محمدی – بخشی از طراحی ui/ux ، طراحی دیتابیس
