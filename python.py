# cross=(3/4)
# print(cross)
# print(round(cross))
# a,b,c=1,2,3
# print(a)
# longstring='''
# hello        52
# asshole
# '''
# print(longstring)
# weather="\tfucku   it\'s \" kind \" \n newyear"
# print(weather)
# name='dansdvm'
# birthyear=2004
# print(f'hi {name} you are {2025-int(birthyear)} years old')
# print (name[1:len(name):2])
# print (name[1::2])
# print(name[::-1])
# print(name[-1])
# print(name[::-2])


# shoping=['reza','ahmad','moein']
# print(shoping[1])
# shoping[1]='mokhtar'
# print(shoping[1])


# matrix_arrays=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix_arrays[1][2])


# from abc import ABC, abstractmethod
# basket = [1, 9, 2, 3, 4, 13, 5, 6, 7]
# basket.append(100)
# newbasket=basket.append(101)      #با اینکه در یک مقدار ذخیره شده بازهم 101 اضافه کرد . حتی بدون پرینت گرفتن هم کار میکند
# print(basket)
# print(newbasket)

# basket.insert(8,49) #به جایگاه 8 عدد 49 رو اضافه میکنه
# print(basket)

# basket.pop() #آخرین کلمه لیست رو حذف میکنه
# print(basket)

# basket.pop(2)  # جای عددی میخواد برای حذف
# print(basket)

# basket.remove(49)  # خود کلمه رو میخواد برای حذف
# print(basket)

# # basket.clear()  کل لیست رو پاک میکنه
# # print(basket)

# newlist=basket.pop(5) # پنجمین عدد لیست رو از بسکت حذف و به نیولیست اضافه کرد
# print(newlist)

# print(basket.index(100)) # جای عددی کلمات در لیست رو میگه

# print(basket.index(6,0,7)) # میگه بین جایگاه عددی 0 تا 7 دنبال 6 بگرد و جاشو بگو

# print(2 in basket)
# print(965 in basket)

# print(basket.count(100)) #میپرسه چن تا 100 در لیست داریم

# basket.sort() #کلمات رو منظم و به ترتیب میکنه
# print(basket)
# print(sorted(basket)) #فقط در همین جمله به صورت یکباره و برای پرینت کار میکنه
# my_list = [(1, 3, 5), (2, 1, 6), (4, 2, 7), (3, 4, 8)]

# # مرتب‌سازی بر اساس عنصر دوم
# sorted_list = sorted(my_list, key=lambda x: x[1])

# print(sorted_list)


# basket.reverse()
# print(basket)

# print(list(range(1,25))) # یه لیست از اعداد 1 تا 24 برات میسازه
# print(list(range(20))) # یه لیست از اعداد 0 تا 20 برات میسازه

# newsentence='  * '.join(['hi','im','danial']) # لیست رو به استرینگ تبدیل میکنه و قبل از جوین هرچی بین اونا باشه بین هرکدوم از کلمات لیست میندازه
# print(newsentence)


# a,b,c=[1,2,3]
# print(b)
# #یه مثال سخت تر 🔽
# a,b,c,*other,d=1,2,3,4,5,6,7,8,9,10
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)
# # تا حرف (سی) قابل فهم است بعد از اون ینی (آدر) رو خودمون نام گذاری کردیم و * به معنای بقیه است و با اومدن (دی) اومد و حرف آخر رو گرفت


# Dictionary-------------------------------------


# لیست: فقط یک‌سری مقادیر پشت‌سر هم
# shopping_list = ['milk', 'bread', 'eggs']       # وقتی از یک لیست استفاده میکنیم مثلا  فقط داده‌ها رو داری و ترتیبی ازشون می‌خوای، مثل نمرات یک کلاس
# print(shopping_list[1])

# دیکشنری: کلید و مقدار
# person = {            # وقتی از دیکشنری استفاده میکنیم مثلا اطلاعات مربوط به یک موضوع رو داری (مثل اطلاعات کاربر، محصول، کتاب) که هر مقدار نیاز به کلید داره / دیکشنری ها با {} کار میکند
#     'name': 'Danial',
#     'age': 21,
#     'country': 'Iran'
# }
# print(person['name'])

# print(person['birthyear'])     # الان تو این مورد سال تولد رو نداریم و باعث شد ارور بگیریم و برنامه کار نکنه. جیکار کنیم؟
# print(person.get('birthyear',2000))   # از (دات‌گت) استفاده می‌کنیم تا ارور نگیریم و اگه کلید نبود، یه مقدار دلخواه خودمون برگرده (2000)

# print('basket' in person)   # آیا بسکت در پرسون وجود داره؟ خیر
# print('iran' in person.keys())  #  آیا در دیکشنری پرسون در قسمت کلیدها ایران وجود داره ؟ خیر
# print('Iran' in person.values()) #  آیا در دیکشنری پرسون در قسمت مقدارها ایران وجود داره ؟ بله

# print(person.items()) #  کل مقادیر دیکشنری رو پرینت میگیره با امکان دسترسی به هر عنصر ولی در صورت پرینت خالی صرفا پرینت گرفته میشه

# person.clear()  #  کل مقادیر دیکشنری رو پاک میکنه
# print(person)

# person2=person.copy()     #با استفاده از کپی مقدار رو کپی کرد و جایی ذخیره کرد که حتی پس از پاک سازی حذف نشد ... در صورتی که از کپی استفاده نمیشد و صرفا یوزر رو در یوزر2 انبار میکردیم پس از پاکسازی پاک میشد
# person.clear()
# print(person)
# print(person2)

# print(person.pop('age'))  #کلید و مقدار هر دو رو پاک میکنه و مقدار رو پرینت میکنه
# print(person)

# print(person.update({'age':24}))   #   مقدار هر کلیدی رو بخوای آپدیت میکنه
# print(person)
# print(person.update({'ages':12}))   #  در صورتی که مقداری که قصد آپدیت داری وجود نداشته باشه یه کلید و مقدار جدید میسازه
# print(person)


# tuples--------------------------------------
#  مثل لیسته ولی ثابته.
# با () می‌سازیم. نمی‌تونیم تغییرش بدیم.
# هرکاری که با لیست و دیکشنری میشه انجام داد با این میشه در صورتی که شامل تغییر نشه
# می‌تونه کلید دیکشنری باشه (برخلاف لیست).


# my_tuple=(1,2,3,4,5)
# print(my_tuple[1])


# set--------------------------------------
# مجموعه‌ای از آیتم‌ها بدون ترتیب و بدون تکرار
#  داخلش نمی‌تونی مقدار تکراری بذاری
#  شبیه لیسته ولی مرتب نیست و آیتم تکراری حذف میشه
#  با {} ساخته میشه
#  شمارش ایندکسی رو ساپورت نمیکنه

# my_set = {1, 2, 2, 3}
# print(my_set)  # $: {1,2,3} ← تکراری حذف شده
# my_set.add(100)
# print(my_set)  #  $: {1, 2, 3, 100}

# my_list=[1,2,3,3,4]
# print(my_list)    # $: [1, 2, 3, 3, 4]
# print(set(my_list))  #  $:{1, 2, 3, 4}

# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,}

# a={1,2}
# b={1,2,3,4}

# print(my_set.difference(your_set))   # آیتم‌هایی که تو مایست هستن ولی تو یورست نیستن.

# print(my_set.discard(5))   #  $None   حذف آیتم از (مایست) اگه نباشه، ارور نمی‌ده.
# print(my_set)   # ${1, 2, 3, 4} عدد 5 حذف شده

# print(my_set.difference_update(your_set))   #  $None  مقدارهای مشترک بین دو ست رو از ست اول حذف می‌کنه
# print(my_set) #  ${1, 2, 3}   اعداد 4و5 حذف شد

# print(my_set.intersection(your_set))   #  ${4, 5}  فقط آیتم‌هایی که توی هر دو ست بودن رو میده
# print(my_set&your_set)   #shortcut

# print(my_set.isdisjoint(your_set))    #  $False    .بررسی می‌کنه که آیا دو ست هیچ اشتراکی ندارن یا نه - اگر چیز مشترک نداشته باشند صحیح و اگر مشترک داشته باشند غلط

# print(my_set.union(your_set))   #   ${1, 2, 3, 4, 5, 6, 7, 8}   دو ست رو با هم ترکیب می‌کنه، بدون آیتم تکراری.
# print(my_set|your_set)   #shortcut

# print(a.issubset(b))  #   $True   آیا همه‌ی اعضای (ای) توی (بی) هست؟
# print(b.issubset(a))  #   $False  آیا همه‌ی اعضای (بی) توی (ای) هست؟

# print(a.issuperset(b))   #   $False    آیا (ای) شامل همه آیتم‌های (بی) هست؟
# print(b.issuperset(a))   #   $True     آیا (بی) شامل همه آیتم‌های (ای) هست؟


# conditional logic ------------------------------------------

# is_old=False
# is_licenced=True

# if is_old:
#     print('you are old enough to drive')
# elif is_licenced:
#     print('you can drive')   #$
# else:
#     print('fuck you')
# print('yes daddyyyy')    #   این فاصله خیلی مهمه در پایبتون، اگر انداره بالایی بود فاصله جز (الس) حساب میشد


# TRUTHY AND FALSY VALUES------------------------------------------

#  Truthy چیه؟
# مقدارهایی که وقتی توی شرط بیاریشون، پایتون اونا رو صحیح حساب می‌کنه.
# همه مقادیری که فکرشو کنی صحیح هستن بجز مقادیر زیر
# False - None - 0, 0.0 - "" (رشته خالی) - [] - () - {} - set() - range(0)
# در صورت استفاده از مقادیر بالا فالس خواهد بود

# name = ("max")
# if name:  # یعنی اگه اسم خالی نباشه
#     print("Welcome!") $
# else:
#     print("Name can't be empty.")
# مثالی بسیار ساده، شرطی گذاشته شد جهت اسم گذاری اگر مقدار خالی باشد فالس میشود و الس اجرا میشود


# TURNERY OPERATOR----------------------------------------------------

# یه روش کوتاه و سریع برای نوشتن شرط‌هاست که تو یه خط انجام می‌شه
# value_if_true if condition else value_if_false    اگر شرط صحیح باشه (ولیو ایف تورو) احرا میشه- اگر شرط غلط باشه (ولیو ایف الس) اجرا میشه

#  مثال
# age = 18
# status = "Adult" if age >= 18 else "Child"
# print(status)  # خروجی: Adult
# در این مثال اگر سن 18 یا بیشتر بود (آدالت) و اگر کمتر از 18 بود (چایلد) اجرا میشد


# short circuiting / Logical operators-------------------------------------------------------

# is_stupid=True
# is_dumb=True

# if is_dumb and is_dumb:       # اگر هر دو صحیح بودن اجرا میشه کد پایین، حتی اگر یکیشون غلط باشه (الس) اجرا میشه
#     print('you are a fucktard')       # $ you are a fucktard
# else:
#     print('idk what you are')

# is_stupid5=True
# is_dumb5=False

# if not is_dumb5:  # میگه اگر (ایزدام) فالس بود فلان کارو کن
#     print('hell yeah')   #  $hell yeah

# if is_dumb5 or is_stupid5:    # حتی اگر یکیشون هم صحیح باشه مثدار اصلی برگردونده میشه، اگر هردو غلط باشن (الس) اجرا میشه
#     print('you are almost a fucktard')
# else:
#     print('idk what you are')


# Comparison Operators------------------------------------------------------
# ==  → مساوی بودن (آیا دو مقدار برابرن؟)
# is  → آیا این دو متغیر دقیقاً به یک آبجکت یکسان توی حافظه اشاره می‌کنن یا نه
# !=  → جواب رو برعکس نشون میده مثال 3 = 3 رو میزنه فالس
# >   → آیا سمت چپ بزرگتره؟
# <   → آیا سمت راست بزرگتره؟
# >=  → آیا سمت چپ بزرگتر یا مساویه؟
# <=  → آیا سمت راست بزرگتر یا مساویه؟
# مثال
# if (3<=4):
#     print('fuckyou')  #  $fuckyou

# تفاوت بین (ایز و ==)
# a = [1, 2, 3]
# b = [1, 2, 3]
# a == b  #  $True   ✅ (مقدار یکیه)
# a is b  #  $False ❌ (دو تا لیست جدا تو حافظه‌ان)


# LOOPS----------------------------------------------------------------------
#  حلقه‌ها در پایتون به ما اجازه میدن که یک بلاک کد رو چندین بار اجرا کنیم بدون اینکه اون کد رو چند بار بنویسیم.

# حلقه تو در تو (nested loop)

# for item in (1, 2, 3):    # 3 بار تکرار
#     for x in ['a', 'b']:   # هر بار، این حلقه 2 بار اجرا میشه
#         print(item, x)   # نمایش مقدار فعلی از هر حلقه
# $ خروجی
# 1 a
# 1 b
# 2 a
# 2 b
# 3 a
# 3 b


# dictionaries in loop -------------------------------
# person = {'name': 'Ali',
#           'age': 22,
#           'job': 'student'}

# for item in person:   # فقط کلیدها  پرینت می‌شن:
#     print(item)
#         #$
#         # name
#         # age
#         # job

# for value in person.values():   # فقط مقدارها
#     print(value)
#         #$
#         #Ali
#         #22
#         #student

# for item in person.items():     #  کل آیتم‌ها (key + value)
#     print(item)
#         #$
#         #('name', 'Ali')
#         #('age', 22)
#         #('job', 'student')

# for key1, value1 in person.items():   #   کلید و مقدار جدا جدا
#     print(key1, "→", value1)
#         #$
#         #name → Ali
#         #age → 22
#         #job → student


# Accumulation pattern / counter-------------------
# جمع کردن مقادیر در یک لیست با استفاده از لوپ
# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0

# for item in my_list:
#     counter = counter + item

# print(counter)


# range-----------------
# این تابع یک توالی از اعداد تولید می‌کنه
# for num in range(5):    # $ از عدد ۰ تا ۴ (۵ شامل نمی‌شه) یکی‌یکی پرینت بگیر
#     print(num)

# مثال های دیگر

# for i in range(2, 7):
#     print(i)
# $ 2 3 4 5 6

# for i in range(0, 11, 2):
#     print(i)
# $ 0 2 4 6 8 10

# for i in range(10, 0, -1):    #شمارش معکوس از 10 تا 1
#     print(i)
# $ 10 9 8 7 6 5 4 3 2 1


# enumerate-------------------------------------
#  یه تابع توکار پایتون هست که وقتی داری روی یه لیست یا مجموعه‌ای از آیتم‌ها حلقه می‌زنی، شماره (ایندکس) اون آیتم‌ها رو هم همراه با خودش می‌ده
# for index, item in enumerate(['a', 'b', 'c']):
#     print(index, item)
#       $0 a
#        1 b
#        2 c

# چرا استفاده کنیم؟
# اگه بخوایم به یه لیست حلقه بزنیم و همزمان هم شماره‌ هر آیتم (ایندکس) رو داشته باشیم، معمولاً اینجوری باید بنویسیم
# for i in range(len(my_list)):
#     print(i, my_list[i])

# ولی این تایع خیلی تمیز تره

# for i, val in enumerate(my_list):
#     print(i, val)

# روش پیدا کردن فقط یک ایندکس رو هم داره که با ایف کار میکنه


# while-----------------------------------------------
# حلقه وایل تا وقتی که شرطش درسته (ترو)، کدهای داخلش رو پیاپی اجرا می‌کنه.
# وقتی شرط فالس بشه ، حلقه تموم میشه

# i=1
# while i<=10:     #  این شرط میگه تا زمانی که (آی) کوچکتر یا مساوی 10 هست ، (آی) پرینت گرفته شود
#     print(i)    #  عدد یک بدون وقفه پرینت گرفته خواهد شد


# i = 1
# while i <= 10:   #   این مثال هم دقیقا مثل مثال بالاس
#     print(i)
#     i += 1    #  ولی با این کد پس از هربار حلقه زدن یک به (آی) اضافه میشود و پس از بالا رقتن عدد (آی) و رسیدن به 10 شرط غلط و پرینت گیری متوقف خواهد شد
#    $
#    1
#    2
#    3
#    4
#    5
#    6
#    7
#    8
#    9
#    10


# i = 1             #  مانند کد بالا با این تفاوت که
# while i <= 10:    #  گفته شده اگر (آی) مساوی 5 شد بریک اتقاق بیوفته
#     print(i)
#     if i == 5:
#         break     #  بریک باعث میشه فورس‌وار حلقه متوقف بشه حتی اگه شرط صحیح باشه
#     i += 1


# i = 1
# while i < 4:
#     print(i)      #   وقتی حلقه به پایان طبیعی خودش برسه (بدون بریک)، بلوک الس اجرا میشه.
#     i += 1
# else:
#     print("تموم شد")
#       $
#       1
#       2
#       3
#    تموم شد

# pass & continue-----------------------------
# وقتی نمی‌خوای هنوز کاری انجام بدی ولی ساختار کد خالی نباشه
# for i in range(5):
#     pass  # اینجا فعلاً کاری نمی‌کنم ولی بعداً شاید بنویسم
# فقط برای اینکه خطای سینتکس نگیری


# 0

# picture=[
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]
# ]

# for pic in picture:
#     for pixels in pic:
#       if (pixels==0):
#         print(' ', end='') # برای خطی اجرا شدن که نه اینکه زیر هم اجرا بشه
#       else:
#          print('*',end='') # برای خطی اجرا شدن که نه اینکه زیر هم اجرا بشه
#     print(' ')     #  برای رفتن به لاین بعدی


# functions------------------------------------------
# یه تیکه کده که یک کار مشخص انجام میده و میتونیم هروقت خواستیم صداش کنیم و ازش استفاده کنیم
# مثال
# def say_hello():
#     print('hello fucker')

# say_hello()       # هرمقدار کد زیر دف باشه با صدا زدنش اجرا میشه

# #invoke مثال با
# def say_helloo(name,emoji):
#     print(f'hello {name} fucker {emoji}')

# say_helloo('reza','😂')

# default parameters مثال با
# def say_fuckyou(name='tom',emoji="😈"):
#     print(f'hey {name} fuck you {emoji}')

# say_fuckyou()    #برای زمانی هست هست که مقداری وارد نمیشه و یه مقدار دیفالت رو وارد میکنه خودش - یجورایی برای محکم کاریه
# say_fuckyou('jake',) # هرمقداریم وارد کنی جایگزین مقدار دیفالت میکنه

# # keyword arguments مثال با
# def say_bye(name,emoji):
#     print(f'bye {name}{emoji}')
# say_bye(name='andrew',emoji='💩')    #برای زمانی که نمیدونی مثلا اول نیم هست یا اموجی سرهمین میتونی دستی وارد کنی - ولی به صورت کلی کد رو کثیف میکنه


# return------------------------------------------------------
# return چند مثال از
# def sumnubers(num1,num2):
#     return num1+num2
# print(sumnubers(3,5))


# def length_of_string(word):
#     return len(word)
# print(length_of_string('hello'))


# def check_even_odd(num):
#     if (num % 2==0):
#         return('even')
#     else:
#         return('odd')
# print(check_even_odd(13))
# # نسخه تمیز تر کد بالا ----
# def check_even_odd(num):
#     return num % 2==0
# print(check_even_odd(50))

# args-----------------
# وقتی تعداد ورودی‌های تابع مشخص نیست
# با *آرگز هر چندتا عدد یا مقدار دلخواهم باشه می‌فرستم
# توی تابع مثل یک لیست باهاش رفتار میشه

# import time


# def add(*args):
#     return sum(args)


# print(add(1, 2, 3))   # $ 6
# print(add(10, 20))    # $ 30

# kwargs---------------
# وقتی بخوای ورودی‌ها اسم‌دار باشن مثل( کلید = مقدار)
# kwargs استفاده میشه از
# توی تابع مثل یک دیکشنری باهاش رفتار میشه

# def say_hi(**kwargsss):
#     for key, value in kwargsss.items():
#         print(f"{key}: {value}")

# say_hi(name="Danial", age=24)
# خروجی:
# name: Danial
# age: 24


# args & kwargs یه مثال ترکیبی از

# def info(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)

# info(1, 2, 3, name="Danial", job="Programmer")
# خروجی:
# Args: (1, 2, 3)
# Kwargs: {'name': 'Danial', 'job': 'Programmer'}

#  تمرین-------------------------------بدست آوردن بزرگترین عدد زوج
# evennumbers=[]
# def highest_even(*num):
#     for i in (num):
#         if i%2==0:
#          evennumbers.append(i)
#     highest=max(evennumbers)
#     return highest
# print(highest_even(*[2,5,9,8,14,21,7]))


# scope rules -----------------------------------
# 1- start with local
# 2- parent local?
# 3- global
# 4- built in python functions

# global مثال از------------
# اگر بخوای داخل تابع، یه متغیر جهانی رو تغییر بدی باید ازش استفاده کنی
# x = 5

# def change():
#     global x
#     x = 10


# change()
# print(x)  # خروجی: 10

# nonlocal مثال از---------
# برای توابع تو در تو استفاده می‌شه، وقتی بخوای متغیر تابع مثلا (اوتر) رو تغییر بدی


# def outer():
#     msg = "hi"

#     def inner():
#         nonlocal msg
#         msg = "bye"
#     inner()
#     print(msg)


# outer()  # خروجی: bye


# OOP ----------------------------------------------------------------------
# 📦 Encapsulation → قفل کردن داده‌ها / فقط با در درست وارد شو
# 👪 Inheritance → بچه‌ها ویژگیای پدر/مادر رو می‌گیرن
# 🌀 Polymorphism → یه اسم → رفتارهای مختلف
# 🎭 Abstraction → فقط چیزای مهم دیده می‌شن، بقیه مخفی

# Encapsulation -------------
# 🧴 یعنی مخفی کردن جزئیات داخلی یک کلاس و کنترل دسترسی به اون‌ها
# از خراب شدن داده‌ها جلوگیری می‌کنه

# class Person:
#     def __init__(self, name):
#         self.__name = name  # __ یعنی خصوصی

#     def get_name(self):
#         return self.__name

# inheritance ----------------
# ارث‌بری یعنی یک کلاس، قابلیت‌ها (متدها و ویژگی‌ها)‌ی کلاس دیگری را به ارث می‌برد
# کد تکراری نمی‌نویسی
# ساختار سازمان‌یافته ایجاد می‌کنی
# تغییرات رو راحت‌تر مدیریت می‌کنی

#         مثال
# فرض کن یه کلاس حیوان داریم که کلی ویژگی عمومی داره

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")

#     def speak(self):
#         print("Animal sound")

# # # حالا ما سگ و گربه داریم. اینا هم غذا می‌خورن (پس خوردن مشترکه)
# # # ولی صدای متفاوتی دارن (پس صداشون متفاوته)


# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says: Woof!")


# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says: Meow!")

# # # اگه کلاس والد (حیوان) متدی مثل (خوردن) داره که مشترکه
# # # و ما تو کلاس فرزند (گربه - سگ) نمی‌خوایم اون متد رو تغییر بدیم
# # # نیازی نیست دوباره بنویسیمش. فقط صداش می‌زنیم


# dog = Dog('rex')
# dog.eat()   # از کلاس حیوان (ارث‌بری شده)
# dog.speak()  # از کلاس سگ (بازنویسی شده)

# Polymorphism -----------------------
# یعنی متدها با یک اسم، ولی رفتارهای مختلف در کلاس‌های مختلف
# نوشتن کد عمومی و قابل انعطاف

# class Cat:
#     def speak(self):
#         print("Meow")

# class Dog:
#     def speak(self):
#         print("Woof")

# for animal in [Dog(), Cat()]:
#     animal.speak()

# Abstraction -------------------------
# یعنی فقط بخش‌های مهم از اطلاعات نشون داده می‌شن، جزئیات پنهان می‌شن
# تمرکز روی کاری که باید انجام بشه، نه چطور انجام می‌شه

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass


# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")
# ---------------------

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title         # ویژگی عنوان
#         self.author = author       # ویژگی نویسنده
#         self.year = year           # ویژگی سال انتشار

#     def update_year(self, new_year):
#         self.year = new_year       # تغییر سال انتشار

#     def info(self):
#         print(f'{self.title} book created in {self.year} by {self.author}')


# # ساخت یک آبجکت از کلاس Book
# book1 = Book('Good Vibes Good Life', 'Vex King', 2018)
# book1.info()  # چاپ اطلاعات اولیه

# # آپدیت سال انتشار
# book1.update_year(2020)
# book1.info()  # چاپ اطلاعات بعد از آپدیت

# یه مثال دیگه

# class movie:
#     def __init__(self, tittle, director, year):
#         self.title = tittle
#         self.director = director
#         self.year = year

#     def update_title(self, new_title):
#         self.title = new_title

#     def update_director(self, new_director):
#         self.director = new_director

#     def update_year(self, new_year):
#         self.year = new_year

#     def info(self):
#         print(f'{self.title} {self.year} directed by {self.director}')


# movie1 = movie('interstellar', 'nolan', 2012)
# movie1.update_year(2016)
# movie1.info()


# class methods -----------------------
# یه متد آمادست برای زمانی ک اطلاعات قرار نیست کاستوم باشه و یه چیزیه که زیاد استفاده میشه و کافیه صداش بزنی تا اطلاعات رو بده

# class book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages

#     @classmethod
#     def short_story(cls):
#         return cls('short_story', 50)

#     def info(self):
#         print(f'{self.title} has {self.pages} pages')


# book1 = book.short_story()
# print(book1.pages)
# book2 = book('fuck', 110)
# print(book2.pages)
# book2.info()

# یه مثال دیگه -----------------

# class movie:
#     def __init__(self, title, duration):
#         self.title = title
#         self.duration = duration

#     @classmethod
#     def shortfilm(cls, title):
#         return cls(title, 40)

#     def show(self):
#         print(f"Movie: {self.title}, Duration: {self.duration} minutes")


# movie1 = movie.shortfilm('interstellar')
# movie1.show()


# isinstance ----------------------
# بررسی اینکه یه آبجکت از یه کلاس خاص ساخته شده یا نه
# مثال --
# class Animal:
#     pass


# class Dog(Animal):
#     pass


# dog1 = Dog()

# if isinstance(dog1, Animal):    # آیا داگ1 نوه حیوان است؟
#     print("Yes, dog1 is an Animal")   # این اجرا میشه

# ✅ طریقه صحیح صدا زدن
# print(isinstance(dog1, Animal))     # $ true


# super() ----------------
# به ما اجازه می‌ده به کلاس والد (پدر) دسترسی داشته باشیم
# معمولاً برای صدا زدن متدهای کلاس پدر از کلاس فرزند استفاده می‌شه
# مثال

# class user:
#     def __init__(self, email):
#         self.email = email

#     def sign_in(self):
#         print('logged in')


# class wizard(user):
#     def __init__(self, name, power, email):
#         super().__init__(email)
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attackinhg with power of {self.power}')


# wizard1 = wizard('fucker', 50, 'wizardfu@gmail.com')
# wizard1.sign_in()
# wizard1.attack()
# print(wizard1.email)

# در این مثال چرا نتونستیم ایمیل را هم مثل ساین این پرینت بگیریم ؟
# چون ایمیل باید یچیز وارد میکردیم و اینینیت داشت و باید این روش بالا انجام شود


# multiple inheritance -----------------
# یعنی یک کلاس، از بیش از یک کلاس به صورت همزمان ارث‌بری کنه
# مثال ساده
# class Father:
#     def speak(self):
#         print("I'm the father.")


# class Mother:
#     def cook(self):
#         print("I'm the mother.")


# class Child(Father, Mother):
#     pass


# child1 = Child()
# child1.speak()  # از Father به ارث برده
# child1.cook()   # از Mother به ارث برده

# اینجا کلاس بچه هم از پدر و هم از مادر ارث برده و می‌تونه به هردو متد دسترسی داشته باشه

# مثال ترکیبی
# class Wizard:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         return (f'attack with power of {self.power}')


# class Archer:
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrows = arrows

#     def attack2(self):
#         return (f'attack with {self.arrows} arrows')


# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Wizard.__init__(self, name, power)
#         Archer.__init__(self, name, arrows)


# hb = HybridBorg("Gandalf", 100, 50)
# print(hb.name)     # از ویزارد یا آرچر فرقی نداره چون هردو نام رو ست کردن
# print(hb.power)    # از Wizard
# print(hb.arrows)   # از Archer
# print(hb.attack2())


# class animal:
#     def eating(self):
#         return ('eating...')


# class cat(animal):
#     pass


# class dog(animal):
#     pass


# def is_this_dog(input):
#     if isinstance(input, dog):
#         print('yes its a damn dog')
#     else:
#         print('not a damn dog')


# animal1 = dog()
# animal2 = cat()
# is_this_dog(animal1)
# is_this_dog(animal2)


# class user:
#     def __init__(self, email):
#         self.email = email


# class admin(user):
#     def __init__(self, email):
#         super().__init__(email)

#     def sign_in(self):
#         return (f'{self.email} has signed in')

#     def access(self):
#         return ('admin access granted')


# user1 = admin('rezagolzar@gmail.com')
# print(user1.sign_in())
# print(user1.access())


# class user:
#     def __init__(self, email='none', password='none', login_stat=False):
#         self.email = email
#         self.__password = password
#         self.login_stat = login_stat

#     def login(self, input):
#         if input == self.__password:
#             self.login_stat = True
#         else:
#             self.login_stat = False
#         return(self.login_stat)


# user1 = user('nonego@gmail.com', 123456)
# user1.login(123456)
# user1.login(12345675)


# ---------

# class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def employee_info(self):
#         return (f'name : {self.name} , role : {self.role()} , salary : {self.salary}')

#     def role(self):
#         return ('fucker')


# class manager(employee):
#     def role(self):
#         return ("manager")


# class developer(employee):
#     def role(self):
#         return ('developer')


# emp1 = manager('sara', 150)
# print(emp1.employee_info())
# unknown_employee = employee('sara', 10)
# print(unknown_employee.employee_info())


# Pure Function -------------------
# خروجی فقط به ورودی بستگی داره
# هیچ تغییری در بیرون از خودش ایجاد نمی‌کنه

# map -----------------------------------------------
# مثال
# def square(x):
#     return x * x


# numbers = [1, 2, 3, 4, 5]

# squared = list(map(square, numbers))

# print(squared)  # [1, 4, 9, 16, 25]

# # همون مثال بدون مپ با استفاده از حلقه
# squared = []
# for num in numbers:
#     squared.append(square(num))

# print(squared)  # [1, 4, 9, 16, 25]


# filter ----------------------------------------------
# تابع فیلتر برای فیلتر کردن عناصر یک ایتربل (مثل لیست یا تاپل) استفاده میشه
# اون فقط عناصری رو نگه می‌داره که شرطی که بهش دادی صحیح بشه

# def is_even(x):
#     return x % 2 == 0


# numbers = [1, 2, 3, 4, 5, 6]

# evens = list(filter(is_even, numbers))

# print(evens)  # [2, 4, 6]


#  بدون استفاده از فیلتر (روش سنتی با حلقه)
# evens = []
# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)

# print(evens)  # [2, 4, 6]


# zip ----------------------------------------------
# تابع زیپ دو یا چند ایتربل (مثل لیست، تاپل، ...) رو به صورت جفت‌جفت کنار هم قرار می‌ده
# names = ['Ali', 'Sara', 'Nima']
# scores = [90, 85, 78]

# zipped = zip(names, scores)
# print(list(zipped))


# reduce -------------------------------------------
# مقدارهای یک لیست رو با یک تابع ترکیب می‌کنه و به یک مقدار نهایی می‌رسه
# from functools import reduce


# def add(x, y):
#     return x + y


# numbers = [1, 2, 3, 4, 5]

# total = reduce(add, numbers)
# print("nums sum:", total)  # خروجی: 15

# مثال سخت تر
# پیدا کردن بزرگ‌ترین عدد در لیست
# from functools import reduce

# def maximum(x, y):
#     return x if x > y else y

# nums = [5, 8, 2, 11, 3]

# max_num = reduce(maximum, nums)
# print("largest num:", max_num)  # خروجی: 11


# lambda -----------------------------------------------
# یک راه کوتاه برای تعریف یک تابع ساده (معمولاً یک خطی) هست، بدون اینکه نیاز به اسم داشته باشه
# تابع معمولی:
# def square(x):
#     return x**2

# ---
# همون با lambda:


# def square(x): return x**2


# print(square(5))  # 25

# از لامبدا میشه با مپ، ریدیوس، فیلتر و... استفاده کرد
# numbers = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)  # [2, 4, 6, 8]


# my_list = [5, 4, 3]
# squred = list(map(lambda inp: inp**inp, my_list))
# print(squred)


# Comprehensions -------------------------------------------------------------
# یه روش کوتاه و تمیزه برای ساختن لیست‌ها، دیکشنری‌ها و ست‌ها به‌صورت سریع و خوانا

# List Comprehension-----------
# مثال ساده
# nums = [1, 2, 3, 4, 5]
# squares = [n**2 for n in nums]
# print(squares)  # 👉 [1, 4, 9, 16, 25]
# مثال با شرط
# even_squares = [n**2 for n in nums if n % 2 == 0]
# print(even_squares)  # 👉 [4, 16]

# Dictionary Comprehension----------
# dicts = {
#     'a': 2,
#     'b': 3
# }
# mydicts = {k1: v1**2 for k1, v1 in dicts.items()}
# print(mydicts)

# Set Comprehension-------------
# nums = [1, 2, 2, 3]
# unique_squares = {n**2 for n in nums}
# print(unique_squares)  # 👉 {1, 4, 9}

# چند نمونه تمرین ----------------------------
# nums = [2, 5, 7, 10]
# newnums = [x**2 for x in nums]
# newnums2 = list(map(lambda x: x**2, nums))
# print(newnums)
# print(newnums2)
# -------------------
# newlist = [x for x in newnums if x > 25]
# newlist2 = list(filter(lambda x: x > 25, newnums2))
# print(newlist)
# print(newlist2)
# -------------------
# names = ['Ali', 'Sara', 'Reza']
# scores = [18, 20, 17]
# newlist3 = list(zip(names, scores))
# newlist4 = [(k1, v2) for k1, v2 in zip(names, scores)]
# print(newlist3)
# print(newlist4)
# -------------------
# nums = [1, 2, 3, 4, 5, 6]
# newnums = [x for x in nums if x % 2 == 0]
# print(newnums)
# -------------------
# nums = [1, 2, 3, 4, 5]
# newnums = [x*3 for x in nums if not x % 2 == 0]
# print(newnums)
# -------------------
# nums = [18, 19, 11]
# names = ['ali', 'sara', 'reza']
# gen = [(name, num) for name, num in zip(names, nums)]
# result = list(map(lambda x: 'passed' if x >= 18 else 'failed', nums))
# final = list(zip(names, result))
# print(final)
# -------------------
# from functools import reduce
# nums = [3, 5, 7, 9]
# newnums = reduce(lambda x, y: x+y, nums)
# print(newnums)


# decorators --------------------------------------------
# def my_decorator(func):
#     print('decorator executed')

#     def wrapper():
#         print('in wrapper')
#         func()
#         print('out of wrapper')

#     return wrapper


# @my_decorator
# def say_hi():
#     print('hi')


# say_hi()
# ---------------


# from time import time


# def timer(func):
#     def wrapper():
#         start = time()
#         func()
#         end = time()
#         print("execute time", end - start, "second")
#     return wrapper


# @timer
# def process():
#     for i in range(100000):
#         print(i*3)


# process()
# ----------------------

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('start fucking')
#         func(*args, **kwargs)
#         print('im done')
#     return wrapper


# @decorator
# def moans(inp):
#     print(f'yes {inp}')


# moans('ahhhhhhhh')
# ------------------------------------------------------------------------------------------------------
# یه تابع بنویس
# نام تابع رو چاپ کنه
# ورودی هارو چاپ کنه
# زمان اجرای تابع رو اندازه بگیره
# خروجی تابع رو هم نمایش بده

# from time import time


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         timer1 = time()
#         print(f'starting {func.__name__} function...')
#         result = func(*args, **kwargs)
#         print(result)
#         print('finished')
#         timer2 = time()
#         timeco = timer2-timer1
#         print(f'it took {timeco} to execute {func.__name__} function')
#         return
#     return wrapper


# @decorator
# def power(x, y):
#     print(f'inputs are {x, y}')
#     return x ** y


# power(10, 3)

# کد من 👆
# کد هوش مصنوعی 👇

# from time import time


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         timer1 = time()
#         print(f'Starting {func.__name__} function...')
#         print(f'Inputs: {args}')

#         result = func(*args, **kwargs)

#         print(f'Output: {result}')
#         timer2 = time()
#         timeco = timer2 - timer1
#         print(f'Execution time: {timeco:.4f} seconds')
#         print('Finished.\n')
#         return result
#     return wrapper


# @decorator
# def power(x, y):
#     return x ** y


# power(10, 3)


# error handling ---------------------------------------------------------------------
# 1. try
# کدی که احتمال داره خطا بده

# 2. except
# اگه خطایی رخ بده، این بلاک اجرا میشه

# 3. else
# اگر هیچ خطایی رخ نده، این اجرا میشه

# 4. finally
# در هر صورت چه خطا باشه چه نباشه، این اجرا میشه (برای تمیزکاری یا پیام‌های پایانی)
# بستن فایل‌ها
# قطع اتصال به دیتابیس


# while True:
#     try:
#         num = int(input("enter a number "))
#         result = 10 / num
#     except ZeroDivisionError:
#         print("🚫 cant devide by zero")
#     except ValueError:
#         print("🚫 please enter a valid number")
#     else:
#         print(f"✅ result: {result}")
#         break  # ✅ وقتی موفق شدی، از حلقه بیا بیرون
#     finally:
#         print("🔁 tring to execute")

# generators------------------------------------------------------------------------------------
# ژنراتورها در پایتون توابعی هستن که مقدارها رو به‌صورت یکی‌یکی و به‌صورت تنبل تولید می‌کنن، یعنی همه‌ی مقادیر رو هم‌زمان در حافظه نگه نمی‌دارن.
# به جای ریترن از ییلد استفاده می‌کنن
# مثال ها


# def simple_gen():
#     for i in range(1, 6):
#         yield i

# for num in simple_gen():
#     print(num)
# -----------------------------------
# def even_numbers():
#     for i in range(0, 10, 2):
#         yield i

# gen = even_numbers()

# print(next(gen))  # 0
# print(next(gen))  # 2
# print(next(gen))  # 4
# print(next(gen))  # 6
# print(next(gen))  # 8
# print(next(gen))  # خطا میده چون دیگه مقداری نیست

# ----------------------------------
# def fibonacci_generator():
#     a, b = 0, 1
#     count = 0
#     while count < 21:
#         yield a
#         a, b = b, a + b
#         count += 1


# for num in fibonacci_generator():
#     print(num)

# همین مثال به شکلل دیگه

# def fib(number):
#     a=0
#     b=1
#     for i in range(number):
#         yield a
#         tempo=a
#         a=b
#         b=tempo+b


# for x in fib(21):
#     print(x)
# ----------------------------------


# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)

# # generator function


# def passed_students(students):
#     for student in students:
#         if student.average() >= 12:
#             yield student


# students_list = []

# while True:
#     name = input("Enter student name (or type 'exit' to finish): ")
#     if name.lower() == 'exit':
#         break

#     try:
#         count = int(input("Enter number of grades: "))
#     except ValueError:
#         print("Number of grades must be an integer.")
#         continue

#     grades = []
#     for i in range(count):
#         while True:   #چرا این خط بالای خط بالایی نیومد؟
#             try:
#                 grade = float(input(f"Grade {i+1}: "))
#                 grades.append(grade)
#                 break          #اینجا چرا از کانتینیو استفاده نشد؟
#             except ValueError:
#                 print("Please enter a valid number for the grade.")

#     # Add the student after collecting grades
#     student = Student(name, grades)      #این خط و خط پایینی رو اصلا منطقش رو نفهمیدم
#     students_list.append(student)

# # sort students by average descending
# sorted_students = sorted(
#     students_list, key=lambda s: s.average(), reverse=True)      # اینجام از لمبدا به بعد نفهمیدم

# # show passed students
# print("\n--- Passed Students ---")
# for s in passed_students(sorted_students):
#     print(f"{s.name} - Average: {s.average():.2f}")


# class bank_account:
#     def __init__(self, owner, balance,passw):
#         self.owner = owner
#         self.balance = balance
#         self.passw=passw

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount


# name = input('enter your name: ')
# mojoodi = float(input('enter your balance:'))
# while True:
#     password=int(input('create and enter your password: '))
#     passwordd=int(input('enter your password again'))
#     if password==passwordd:
#         break
#     else:
#         print('passwords not same!')
# transaction_count = int(input('how many transaction you wanna do? '))
# person = bank_account(name, mojoodi,password)
# for i in range(transaction_count):
#     asker = input('what kind of tranaction you wanna do? ')
#     if asker == 'withdraw':
#         passcheck=int(input('enter your password'))
#         if passcheck==password:
#             asker1 = float(input('enter the amount you want to withdraw: '))
#             person.withdraw(asker1)
#         else:
#             print('wrong password')

#     elif asker == 'deposit':
#         passcheck2=int(input('enter your password'))
#         if passcheck2==password:
#             asker2 = float(input('enter the amount you want to deposit: '))
#             person.deposit(asker2)
#         else:
#             print('wrong password')
#     else:
#         print('fuck you')
# print(f' owner: {person.owner} - last balance: {person.balance:.2f}')


# class BankAccount:
#     def __init__(self, owner, balance, password):
#         self.owner = owner
#         self.balance = balance
#         self.password = password

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"{amount} withdrawn. New balance: {self.balance}")
#         else:
#             print("Insufficient funds!")

#     def check_password(self, passw):
#         return self.password == passw


# class Bank:
#     def __init__(self):
#         self.accounts = []

#     def create_account(self, owner, balance, password):
#         account = BankAccount(owner, balance, password)
#         self.accounts.append(account)
#         print(f"Account created for {owner} with balance {balance}")

#     def find_account(self, owner):
#         for acc in self.accounts:
#             if acc.owner == owner:
#                 return acc
#         return None

#     def deposit(self, owner, password, amount):
#         acc = self.find_account(owner)
#         if acc and acc.check_password(password):
#             acc.deposit(amount)
#         else:
#             print("Account not found or wrong password.")

#     def withdraw(self, owner, password, amount):
#         acc = self.find_account(owner)
#         if acc and acc.check_password(password):
#             acc.withdraw(amount)
#         else:
#             print("Account not found or wrong password.")

#     def transfer(self, from_owner, from_pass, to_owner, amount):
#         from_acc = self.find_account(from_owner)
#         to_acc = self.find_account(to_owner)
#         if from_acc and to_acc and from_acc.check_password(from_pass):
#             if from_acc.balance >= amount:
#                 from_acc.withdraw(amount)
#                 to_acc.deposit(amount)
#                 print(f"Transferred {amount} from {from_owner} to {to_owner}")
#             else:
#                 print("Not enough balance for transfer.")
#         else:
#             print("Transfer failed. Check accounts or password.")

#     def show_all(self):
#         for acc in self.accounts:
#             print(f"Owner: {acc.owner}, Balance: {acc.balance}")


# # منوی اصلی
# bank = Bank()
# while True:
#     print("\n1. Create account")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Transfer")
#     print("5. Show all accounts")
#     print("6. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         name = input("Enter owner name: ")
#         balance = float(input("Enter initial balance: "))
#         password = input("Set a password: ")
#         bank.create_account(name, balance, password)

#     elif choice == "2":
#         name = input("Enter account owner: ")
#         password = input("Enter password: ")
#         amount = float(input("Enter amount to deposit: "))
#         bank.deposit(name, password, amount)

#     elif choice == "3":
#         name = input("Enter account owner: ")
#         password = input("Enter password: ")
#         amount = float(input("Enter amount to withdraw: "))
#         bank.withdraw(name, password, amount)

#     elif choice == "4":
#         from_owner = input("Enter your account name: ")
#         from_pass = input("Enter your password: ")
#         to_owner = input("Enter recipient account name: ")
#         amount = float(input("Enter amount to transfer: "))
#         bank.transfer(from_owner, from_pass, to_owner, amount)

#     elif choice == "5":
#         bank.show_all()

#     elif choice == "6":
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice, try again.")


# --------------------------------------------------------


# class bankaccount:
#     def __init__(self, owner, balance, password):
#         self.owner = owner
#         self.balance = balance
#         self.password = password

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f'new balance: {self.balance}')
#         else:
#             print('not enough balance')

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'new balance: {self.balance}')

#     def checkpass(self, passw):
#         return passw == self.password


# class Bank:
#     def __init__(self):
#         self.accounts = []

#     def create_account(self, name, balance, password):
#         account = bankaccount(name, balance, password)
#         self.accounts.append(account)
#         print(
#             f' account created ! owner name: {name} balance: {balance} password: {len(password) * '*'}')

#     def find_account(self, inp):
#         for i in self.accounts:
#             if i.owner == inp:
#                 return i
#         return None

#     def withdraw(self, owner, amount, password):
#         acc = self.find_account(owner)
#         if acc and acc.checkpass(password):
#             acc.withdraw(amount)
#         else:
#             print('something wrong with account or password')

#     def deposit(self,owner,amount,password):
#         acc=self.find_account(owner)
#         if acc and acc.checkpass(password):
#             acc.deposit(amount)
#         else:
#             print('something wrong with account or password')

#     def transfer(self,fromacc,frompass,toacc,amount):
#         acc=self.find_account(fromacc)
#         acc2=self.find_account(toacc)
#         if acc and acc2 and acc.checkpass(frompass):
#             if amount<=acc.balance:
#                 acc.withdraw(amount)
#                 acc2.deposit(amount)
#                 print(f'amount: {amount} transferd from {acc.owner} to {acc2.owner} succesfully !')
#             else:
#                 print('not enough balance')

#         else:
#             print('something wrong with accounts or password')

#     def showall(self):
#         for i in self.accounts:
#             print(f"Owner: {i.owner}, Balance: {i.balance}")

# bank=Bank()
# while True:
#     print("\n1. Create account")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Transfer")
#     print("5. Show all accounts")
#     print("6. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice==1:
#         name=input('enter your name: ')
#         balance=float(input('enter your balance: '))
#         while True:
#             password=input('create your password: ')
#             passcheck=input('enter the password again: ')
#             if password==passcheck:
#                 break
#             else:
#                 print('passwords not same')
#         bank.create_account(name,balance,password)

#     elif choice==2:
#         name=input('enter account owner: ')
#         amount=float(input('enter amount: '))
#         password=input('enter password: ')
#         bank.deposit(name,amount,password)

#     elif choice==3:
#         name=input('enter account owner: ')
#         amount=float(input('enter amount: '))
#         password=input('enter password: ')
#         bank.withdraw(name,amount,password)

#     elif choice==4:
#         fromac=input('enter the source account: ')
#         fromp=input('enter source password: ')
#         toac=input('enter destination account: ')
#         amount=float(input('enter the amount: '))
#         bank.transfer(fromac,fromp,toac,amount)

#     elif choice==5:
#         bank.showall()

#     elif choice == 6:
#         print("Goodbye!")
#         break

#     else:
#         print("Invalid choice, try again.")

# modules & packages  -----------------------------------------------------------------------------------

# module:
# هر فایل پایتون خودش یه ماژول حساب میشه
# math_utils.py مثلاً اگه یه فایل بسازی به اسم

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# یه ماژول هست math_utils.py این فایل
# کنی import توی فایل دیگه می‌تونی اینو

# import math_utils

# print(math_utils.add(3, 4))  # 7
# ---------
# Package:
# وقتی چند تا ماژول رو توی یه پوشه می‌ذاری، اون پوشه میشه پکیج


# یه مثال با ایف
# math_utils.py فایل

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# print("math_utils module is loaded!")

# if __name__ == "__main__":
#     # This part runs only if we run THIS file directly
#     print("Running math_utils directly...")
#     print(add(2, 3))
#     print(sub(5, 2))

# main.py  فایل

# import math_utils

# print("Inside main.py now!")
# result = math_utils.add(10, 20)
# print("Result:", result)


# Case 1: Run math_utils.py مورد 1
# math_utils module is loaded!
# Running math_utils directly...
# 5
# 3

# Case 2: Run main.py مورد 2
# math_utils module is loaded!
# Inside main.py now!
# Result: 30

# رو مستقیم اجرا کردی هم کدهای بیرون ایف اجرا شدنmath_utils.py وقتی
# و هم کدهای داخل ایف (محاسبات اد و ساب)

# When you run main.py → since math_utils was only imported, the codes outside the if statement in math_utils were executed
# (that "module is loaded!"), but the codes inside the if statement were not executed.


# built in modules -------------------------------------------------
# داره که همراهش نصب می‌شن. اینا ابزارهایی هستن که نیاز نیست دانلود کنی یا جداگانه بسازی، فقط کافیه ایمپورت کنی و استفاده کنی. (built-in modules) پایتون خودش یه عالمه ماژول آماده
# مثال ریاضیات

# import math
# print(math.sqrt(16))     # ریشه دوم = 4.0
# print(math.factorial(5)) # فاکتوریل = 120
# print(math.pi)           # عدد پی = 3.1415926535...

# مثال رندوم

# import random
# print(random.randint(1, 10))   # یه عدد تصادفی بین 1 و 10
# print(random.choice(['a', 'b', 'c'])) # یکی رو شانسی انتخاب می‌کنه


# .....و


# sys.argv ------------------------------
# یک لیست است که شامل آرگومان‌های خط فرمانی است که به اسکریپت پایتون ارسال می‌شود
# این لیست به شما اجازه می‌دهد تا ورودی‌هایی را که هنگام اجرای برنامه از خط فرمان وارد می‌شوند، دریافت کنید

# import sys

# # sys.argv[0] = اسم فایل
# # sys.argv[1] = عدد اول
# # sys.argv[2] = عملگر (+ یا - یا * یا /)
# # sys.argv[3] = عدد دوم

# num1 = int(sys.argv[1])
# op = sys.argv[2]
# num2 = int(sys.argv[3])

# if op == "+":
#     result = num1 + num2
# elif op == "-":
#     result = num1 - num2
# elif op == "*":
#     result = num1 * num2
# elif op == "/":
#     result = num1 / num2
# else:
#     result = "Invalid operator!"

# print("Result:", result)


# # اجرا در ترمینال
# # فرض کن اسم فایل هست
# python calc.py 10 + 5


# collections module -------------------------------------------------

# Counter-----------
# برای شمردن تعداد تکرار عناصر استفاده میشه

# from collections import Counter

# mylist = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# counter = Counter(mylist)
# print(counter)

# Counter({'apple': 3, 'banana': 2, 'orange': 1})      خروجی

# یا می‌تونی به شکل دیکشنری استفاده کنی

# print(counter['apple'])  # 3
# print(counter.most_common(1))  # [('apple', 3)]

# defaultdict ----------
# شبیه دیکشنری معمولی هست، ولی وقتی کلید وجود نداشت، به‌جای خطا یه مقدار پیش‌فرض برمی‌گردونه

# from collections import defaultdict

# d = defaultdict(int)  # مقدار پیش‌فرض int یعنی 0
# d['a'] += 1
# d['b'] += 2

# print(d['a'])
# print(d['c'])  # چون c وجود نداره، پیش‌فرض 0 برمی‌گردونه

# OrderedDict ---------
# یه دیکشنری هست که ترتیب اضافه شدن کلیدها رو حفظ می‌کنه
# از پایتون 3.7 به بعد، دیکشنری عادی هم به طور پیش‌فرض ترتیب رو نگه می‌داره، ولی  امکانات بیشتری مثل داره.)

# from collections import OrderedDict

# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3

# print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# od.move_to_end('a')  # کلید 'a' میره آخر
# print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])


# pdb -------------------------------------------------------------------------------------------------


# بهت اجازه میده کد رو خط به خط اجرا کنی، متغیرها رو چک کنی، وسط اجرا بایستی، دستورات رو تغییر بدی و راحت بفهمی مشکل کجاست


# - ** a →** پارامترهای تابع را نشان می‌دهد (همان عدد اول و عدد دوم)

# - ** n →** به خط بعدی می‌رود

# - ** c →** ادامه می‌دهد تا نقطه‌ی توقف بعدی

# - ** w →** محل اجرای برنامه را نشان می‌دهد

# → s وارد توابع می‌شه


# import pdb

# def add(a, b):
#     pdb.set_trace()  # توقف اینجا
#     return a + b

# x = add(5, 7)
# print(x)


# دستورات داخل ترمینال
# (Pdb) a
# a = 5
# b = 7
# (Pdb) n
# -- خط بعد اجرا میشه --
# (Pdb) p a+b
# 12
# (Pdb) c
# 12


# file I/O -----------------------------------------------------------------------------------------------------
# نوشتن در فایل

# with open("my_file.txt", "w") as f:  # دفتر جدید باز می‌کنم
#     f.write("hello world")              # تو دفتر می‌نویسم

# "my_file.txt" → اسم دفتره (فایلیه که ساخته میشه)

# "w" → یعنی  (نوشتن)

# f.write("hello world") → تو فایل نوشتی "سلام دنیا"

# خواندن از فایل

# with open("my_file.txt", "r") as f:  # دفترمو باز می‌کنم
#     content = f.read()              # کل متنشو می‌خونم
#     print(content)                  # نشونم بده


# اگه بخوای بار دوم چیزی اضافه کنی ولی نوشته قبلی پاک نشه، از "آ(حرف اول انگلسی)" استفاده می‌کنی

# "r" = فقط بخون

# "w" = بنویس (پاک کن و از اول بنویس)

# "a" = اضافه کن به آخرش

# "rb" / "wb" = برای فایلای غیرمتنی مثل عکس


# regular expressions ------------------------------------------------------------------------------------------------------------------


# search → می‌گرده ببینه اون متن توی [جایی که میخوای] هست یا نه
#  اگر پیدا کنه، یه آدرس میده (مثلاً از کجای متن شروع شده)

# findall → همه جاهایی که این متن تو ??? بوده رو لیست می‌کنه.

# fullmatch → فقط وقتی قبول می‌کنه که کل متن دقیقاً همونی باشه که تو نوشتی

# match → فقط اول متن رو چک می‌کنه

# مثال -----------

# import re
# pattern = re.compile(r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$")
# password = 'heLLo123@'
# if pattern.fullmatch(password):
#     print(f'{password} is ok')
# else:
#     print('fuck you')

# مثال ------------

# می‌خوایم پسوردی رو قبول کنیم که
# حداقل ۸ کاراکتر باشه ،حداقل ۱ عدد داشته باشه ،حداقل ۱ حرف بزرگ داشته باشه ،حداقل ۱ علامت خاص داشته باشه


# import re

# # الگوی پسورد
# pattern = re.compile(r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$")

# passwords = ["hello123", "Hello123", "Hello123!", "short!A1"]

# for pw in passwords:
#     if pattern.fullmatch(pw):
#         print(f"{pw} ✅ Valid password")
#     else:
#         print(f"{pw} ❌ Invalid password")


# unit test -----------------------------------------------------------------------------------------------------------------------------
# یونیت تست یعنی تست کردن تیکه‌های کوچیک (تابع یا کلاس) از برنامه‌مون، جدا جدا
# -----
# calculator.py مثال کامل کدی که میخوایم تست کنیم مثلا از فایل


# def add(a, b):
#     return a + b

# def divide(a, b):
#     if b == 0:
#         raise ValueError("Division by zero!")
#     return a / b

# test_calculator.py حالا ذاخل پوشه تست

# import unittest
# import calculator   # فایل اصلی رو ایمپورت می‌کنیم

# class TestCalculator(unittest.TestCase):

#     def setUp(self):
#         print("شروع تست...")


#     def test_add(self):
#         result = calculator.add(2, 3)
#         self.assertEqual(result, 5)         # اگر درست باشه اوکی بده
#         self.assertNotEqual(result, 10)     # اگر 10 نبود اوکی بده

#     def test_divide(self):
#         result = calculator.divide(10, 2)
#         self.assertEqual(result, 5)
#         self.assertIsInstance(result, float)  # اگر فلوت بود اوکی بده

#     def test_divide_by_zero(self):
#         # اینجا انتظار داریم ValueError بیاد
#         self.assertRaises(ValueError, calculator.divide, 10, 0)

#     def tearDown(self):
#         print("پایان تست.")

# if __name__ == "__main__":
#     unittest.main()


# چیزایی که واقعا بیشتر استفاده میشن:

# assertEqual → مقایسه‌ی نتیجه‌ها

# assertTrue / assertFalse → درست/غلط بودن شرط

# assertIsInstance → چک کردن نوع داده یا خطا

# assertRaises → چک کردن خطاها

# setUp و tearDown → آماده‌سازی و تمیزکاری


# pillow library
# مثال
# from PIL import Image, ImageDraw, ImageFont

# # 1. باز کردن عکس
# img = Image.open("test.jpg")

# # 2. تغییر اندازه (مثلا کوچیک کردن به 300x300)
# small_img = img.resize((300, 300))

# # 3. نوشتن متن روی عکس
# draw = ImageDraw.Draw(small_img)

# # انتخاب فونت (باید فایل فونت مثل arial.ttf توی پوشه باشه)
# font = ImageFont.truetype("arial.ttf", 30)

# # نوشتن متن
# draw.text((10, 10), "My Watermark", fill="red", font=font)

# # 4. ذخیره عکس جدید
# small_img.save("final_image.jpg")

# print("✅ عکس ساخته شد!")


# خلاصه

# Image.open, save → پایه

# resize, crop, rotate, convert → خیلی پرکاربرد

# ImageDraw → متن و شکل روی عکس

# ImageFilter → افکت‌ها

# paste → ترکیب عکس‌ها

# thumbnail → کوچک کردن عکس بدون فشرده شدن تصویر


# مثال

# import sys
# import os
# from PIL import Image

# # گرفتن ورودی‌ها از ترمینال
# image_folder = sys.argv[1]   # پوشه ورودی
# output_folder = sys.argv[2]  # پوشه خروجی

# # اگه پوشه خروجی وجود نداشت بسازش
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # حلقه روی همه فایل‌ها در پوشه ورودی
# for filename in os.listdir(image_folder):
#     img = Image.open(f'{image_folder}/{filename}')   # باز کردن عکس
#     clean_name = os.path.splitext(filename)[0]       # گرفتن اسم بدون پسوند
#     img.save(f'{output_folder}/{clean_name}.png', 'png')  # ذخیره به PNG

# print("all done!")


# sending email ---------------------------------------------------------------------------

# import smtplib
# from email.message import EmailMessage

# EMAIL_ADDRESS = "your_email@gmail.com"
# EMAIL_PASSWORD = "your_app_password"   # پسورد ۱۶ رقمی اپ

# msg = EmailMessage()
# msg['Subject'] = "سلام از پایتون 🚀"
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = "friend@gmail.com"
# msg.set_content("این یک تست ایمیل با پایتون هست.")

# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)

# print("ایمیل با موفقیت ارسال شد ✅")
# -------

# با متن قابل تغییر

# import smtplib
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path

# # خواندن فایل HTML
# html = Template(Path("index.html").read_text(encoding="utf-8"))

# # ساخت ایمیل
# email = EmailMessage()
# email["from"] = "Andrei Neagoie"
# email["to"] = "example@gmail.com"   # گیرنده ایمیل
# email["subject"] = "You won 1,000,000 dollars!"

# # ست کردن محتوای اچتی ام ال به ایمیل
# email.set_content(
#     html.substitute({"name": "TinTin"}), subtype="html"
# )

# # اتصال به سرور SMTP و ارسال
# with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#     smtp.ehlo()   #اختیاری
#     smtp.starttls()
#     smtp.login("your_email@gmail.com", "your_app_password")
#     smtp.send_message(email)
#     print("✅ Email sent successfully!")


# کد داخل html
# <!doctype html>
# <html>
#   <body>
#     <h1>Hello ${name}!</h1>
#     <p>This is a test HTML email.</p>
#   </body>
# </html>


# password checker project ---------------------------------------------------------------------------------------------------------------------------------------

#!/usr/bin/env python3
# checkmypass.py - check if a password appears in "Have I Been Pwned" pwned-passwords
# usage: python checkmypass.py        (then type password hidden)
#        python checkmypass.py mypass

# import hashlib
# import requests
# import hmac
# import sys
# from getpass import getpass

# API_URL = "https://api.pwnedpasswords.com/range/"


# def request_api_data(first5: str, timeout: float = 10.0) -> str:
#     """Send request to HIBP range API for the given first5 SHA1 chars."""
#     url = API_URL + first5
#     headers = {"User-Agent": "checkmypass/1.0 (python)"}
#     try:
#         res = requests.get(url, headers=headers, timeout=timeout)
#     except requests.RequestException as e:
#         raise RuntimeError(
#             f"Network error when contacting HIBP API: {e}") from e

#     if res.status_code != 200:
#         raise RuntimeError(f"Error fetching {url}: status {res.status_code}")
#     return res.text


# def get_password_leaks_count(hashes_text: str, tail_to_check: str) -> int:
#     """Parse API response and return how many times the tail was seen (0 if not)."""
#     tail_to_check = tail_to_check.upper()
#     for line in hashes_text.splitlines():
#         if not line:
#             continue
#         parts = line.split(":")
#         if len(parts) != 2:
#             continue
#         hash_suffix, count = parts[0].strip(), parts[1].strip()
#         if hmac.compare_digest(hash_suffix.upper(), tail_to_check):
#             try:
#                 return int(count)
#             except ValueError:
#                 return 0
#     return 0


# def pwned_api_check(password: str) -> int:
#     """Return number of times password appeared in breaches (0 if not)."""
#     if not isinstance(password, str):
#         raise TypeError("password must be a string")
#     sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
#     first5, tail = sha1password[:5], sha1password[5:]
#     hashes_text = request_api_data(first5)
#     return get_password_leaks_count(hashes_text, tail)


# def main():
#     if len(sys.argv) > 1:
#         password = sys.argv[1]
#     else:
#         password = getpass("Enter password to check (input hidden): ")

#     try:
#         count = pwned_api_check(password)
#     except RuntimeError as e:
#         print("Error:", e)
#         sys.exit(2)

#     if count:
#         print(
#             f"WARNING: This password was found {count} times in data breaches. Do NOT use it.")
#     else:
#         print("Good: This password was NOT found in the pwned database (still use a strong unique password).")


# if __name__ == "__main__":
#     main()




# ------------------------------


# # نسخه ساده برای فهمِ ایده‌ی کلی
# import hashlib
# import requests
# from getpass import getpass

# BASE = "https://api.pwnedpasswords.com/range/"

# def request_first5(first5):
#     """از API می‌پرسه و متنِ جواب رو برمی‌گردونه."""
#     url = BASE + first5
#     r = requests.get(url, timeout=10)   # timeout فقط برای جلوگیری از انتظار نامحدود
#     return r.text

# def count_leaks(hashes_text, tail):
#     """آیا tail (باقی SHA1) در متن هست؟ اگه هست چند بار؟"""
#     tail = tail.upper()
#     for line in hashes_text.splitlines():
#         if not line:
#             continue
#         parts = line.split(":")
#         if parts[0].upper() == tail:
#             return int(parts[1])
#     return 0

# def check_password(password):
#     """پسورد رو SHA1 می‌کنه و با API چک می‌کنه."""
#     sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
#     first5, tail = sha1[:5], sha1[5:]
#     text = request_first5(first5)
#     return count_leaks(text, tail)

# # اجرا
# pw = getpass("Password: ")
# n = check_password(pw)
# if n:
#     print("این رمز قبلاً لو رفته:", n, "بار — استفاده نکن.")
# else:
#     print("این رمز در پایگاه پویند پیدا نشد.")



# TWITTER API ----------------------------------------------------------------------------------------------------------------

# import tweepy
# import time

# # اینجا باید کلیدها و توکن‌های خودت از API توییتر رو بذاری
# consumer_key = "YOUR_CONSUMER_KEY"
# consumer_secret = "YOUR_CONSUMER_SECRET"
# access_token = "YOUR_ACCESS_TOKEN"
# access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# # احراز هویت
# auth = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret, access_token, access_token_secret
# )
# api = tweepy.API(auth)

# user = api.me()
# print("Logged in as:", user.name)


# # هندل کردن محدودیت نرخ (Rate Limit)
# def limit_handler(cursor):
#     while True:
#         try:
#             yield cursor.next()
#         except tweepy.RateLimitError:
#             print("Rate limit reached. Sleeping for 5 minutes...")
#             time.sleep(300)  # صبر کردن ۵ دقیقه


# # عبارت جستجو
# search_string = "Andrei Neagoie"
# numbersOfTweets = 2

# # جستجو و لایک کردن توییت‌ها
# for tweet in limit_handler(
#     tweepy.Cursor(api.search_tweets, search_string).items(numbersOfTweets)
# ):
#     try:
#         tweet.favorite()
#         print("I liked that tweet:", tweet.text)
#     except tweepy.TweepError as e:
#         print("Error:", e.reason)
#     except StopIteration:
#         break


# web scrapping -------------------------------------------------------------------------------------------------------------------------------

# برنامه‌نویسی برای «خواندن» محتوای صفحات وب و گرفتن داده‌های مورد نیاز (مثل عنوان، قیمت، متن مقاله، لینک‌ها و غیره)

# import requests
# from bs4 import BeautifulSoup

# url = "https://example.com"
# headers = {"User-Agent": "Mozilla/5.0 (compatible; MyBot/0.1)"}
# res = requests.get(url, headers=headers, timeout=10)
# res.raise_for_status()  # اگر وضعیت 200 نبود خطا میده

# soup = BeautifulSoup(res.text, "html.parser")  # یا "lxml"
# title = soup.find("title").get_text(strip=True)
# print("Title:", title)

# # مثال گرفتن همه مقالات با CSS selector
# for article in soup.select("article.post"):
#     headline = article.select_one("h2").get_text(strip=True)
#     link = article.select_one("a")["href"]
#     print(headline, link)



#برای صفحات مدرن جاوااسکریپتی از پلی رایت استفاده میشه


# beautiful soup کلاس های مهم 
# find() اولین تگی که با شرایطت (مثل اسم تگ یا کلاس) جور در میاد رو برمی‌گردونه
# find_all() همه‌ی تگ‌هایی که با شرایط جور در میان رو به صورت لیست برمی‌گردونه
# select() با سی اس اس سلکتور کار می‌کنه، یعنی مثل استایل‌نویسی در سی اس اس
# select_one() مثل سلکت() هست ولی فقط اولین مورد رو برمی‌گردونه
# .text فقط متن خام داخل یک تگ رو می‌گیره (بدون تگ‌های اچ تی ام ال)
# .get_text() مثل .تکست هست ولی می‌تونی مشخص کنی فاصله‌ها چطور باشن یا متن فرزندان هم اضافه بشه