from django.contrib import admin
#ici, on importe toutes les tables de model necessaires a etre presentees dans l'Admin.
from basic_app.models import User,UserProfileInfo


admin.site.register(UserProfileInfo)
