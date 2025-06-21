from django.contrib.auth.decorators import  user_passes_test

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_data_admin, login_url='login')(view_func)
 