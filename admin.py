from django.contrib import admin
# Register your models here.
#admin mai model register karna hota hai

from home.models import Contact,Cart,Product,CartItem#import kar bhai models ko lol
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(CartItem)
