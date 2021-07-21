from django.contrib import admin
from .models import Company,Category,Product,Dealer_Details
from django.contrib.auth.models import Group


# Admin Action Functions
# def change_rating(modeladmin, request, queryset):
#     queryset.update(rating = 'e')

# Action description
# change_rating.short_description = "Mark Selected Products as Excellent"

# ModelAdmin Class # DataFlair
class ProductA(admin.ModelAdmin):
    model = Product
    list_display = ('item_code', 'item', 'get_company', 'get_product_category','purchase_rate','mrp_rate','wholesale_rate')
    list_filter = ('product_category', )
    fieldsets = (
      ('Standard info', {
          'fields': ('item_code','item','company','product_category','purchase_rate','mrp_rate','wholesale_rate',)
      }),      
   )
    readonly_fields=('item_code',)
    # actions = [change_rating]
    def get_company(self, obj):
        return obj.company.company_name
        # print(obj.company.company_name)
    # get_company.short_description = 'company'
    # get_company.admin_order_field = 'book__author'
    def get_product_category(self, obj):
        return obj.product_category.catagory

# DataFlair
admin.site.register(Product, ProductA)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Dealer_Details)
admin.site.unregister(Group)

# DataFlair # Changing Admin header
admin.site.site_header = "Purchase Module"
