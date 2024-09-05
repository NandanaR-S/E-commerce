from django.contrib import admin
from userapp.models import UserModel,UserAddress,Cart,OrderDetails,ReviewDetails
from adminapp.models import AdminModel,CategoryDetails,ProductDetails,Productimages

admin.site.register(UserModel)
admin.site.register(UserAddress)
admin.site.register(Cart)
admin.site.register(OrderDetails)
admin.site.register(ReviewDetails)
admin.site.register(AdminModel)
admin.site.register(CategoryDetails)
admin.site.register(ProductDetails)
admin.site.register(Productimages)


