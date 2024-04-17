from django.contrib import admin
from .models import Products,Order
# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ANNA Shopping"
admin.site.index_title = "Manage Anna Shop"




class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")


    change_category_to_default.short_description='Default Category'
    list_display = ('title','price','discounted_price','category','description','image')
    search_fields = ('title','category',)
    actions = ('change_category_to_default',)
    #for only displaying certain fields in product/hiding other fields
    fields = ('title','price',)
    #for making certain fields editable 
    list_editable = ('price','category',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)