import os
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django_asgi_app = get_asgi_application()

from shop.models import *

item1 = Item.objects.create(name='sabiz', price=35)
item2 = Item.objects.create(name='kurut', price=55)
item3 = Item.objects.create(name='nan', price=55)
item4 = Item.objects.create(name='alma', price=80)
item5 = Item.objects.create(name='piaz', price=42)
item6 = Item.objects.create(name='kolbasa', price=235)
item7 = Item.objects.create(name='byshtak', price=63)
item8 = Item.objects.create(name='jumurtka', price=12)
item9 = Item.objects.create(name='cofee', price=85)
item10 = Item.objects.create(name='murch', price=15)


item1.purchases.create(name='Жаннат', age=34)
item2.purchases.create(name='Жаннат', age=34)
item3.purchases.create(name='Айдай', age=32)
item4.purchases.create(name='Азат', age=29)
item5.purchases.create(name='Алмаз', age=35)
item6.purchases.create(name='Айдай', age=32)
item7.purchases.create(name='Азат', age=29)
item8.purchases.create(name='Алмаз', age=35)
item9.purchases.create(name='Жаннат', age=34)
item10.purchases.create(name='Азат', age=29)
item1.purchases.create(name='Айдай', age=32)
item10.purchases.create(name='Айдай', age=32)
item7.purchases.create(name='Алмаз', age=35)
item10.purchases.create(name='Азат', age=29)
item5.purchases.create(name='Алмаз', age=35)
item6.purchases.create(name='Азат', age=29)

