
# Copy the "Address" folder into your aps

Projects > Address

# Copy the "Template/Address" folder into your Template folder (Only Address Folder)

Template > Address > (all_template_File)

# import views into aps.url

from .Address.address_view import import_district, import_upazila, import_union, import_village, updated_database


# Create url for views
    path('all/hiden/field/', updated_database, name='updated_database'),
    path('all/hiden/field/update_district/', import_district, name='district'),
    path('all/hiden/field/update_upazila/', import_upazila, name='upazila'),
    path('all/hiden/field/update_union/', import_union, name='union'),
    path('all/hiden/field/update_village/', import_village, name='village'),
    
    
    
# call all models from tour aps

from aps.Address.models_address import Division, District, Upazila, Union, PostOffice, Village

(here "aps" is my existing aps)
