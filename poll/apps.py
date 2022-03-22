from django.apps import AppConfig


# Credits - please note this code is sourced from the 
# Official Django documentation on poll tutorials and
# is fully acknowledged & accredited in readme
class PollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'poll'
