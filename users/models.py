from django.db import models

class MyUser(models.Model):
    ####
    # user_id 預設 Primary Key
    # username 預設欄位
    # password 預設欄位
    # first_name
    # last_name
    ####

    # TempUser
    user_name = models.CharField(max_length=20)
    user_account = models.CharField(max_length=20)
    user_password = models.CharField(max_length=256)
    user_create_date = models.DateTimeField()
    # NormalUser
    user_gender = models.NullBooleanField(default=None)
    user_image = models.ImageField(upload_to='static/user_images') # EDIT /static/user_images/FILE.XXX
    user_school = models.CharField(max_length=100)
    user_deparment = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_autobiography = models.CharField(max_length=500)
    user_type = models.CharField(max_length=20)

    # Settings
    is_temp_user = models.BooleanField(default=True) # True: TempUser / False:NormalUser
    is_admin_user = models.BooleanField(default=False) # Or is_staff

    def __str__(self):
        return self.user_name