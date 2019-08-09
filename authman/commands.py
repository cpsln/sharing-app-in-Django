from django.contrib.auth.models import Group
from django.db import DatabaseError


def add_users_to_group(user_account, group_name):
    try:
        group = Group.objects.get(name=group_name)
        group.user_set.add(user_account)
        return True
    except DatabaseError as e:
        print ("DatabaseError:", e)
        return False
    except Exception as e:
        print ("Exception:", e)
        return False
    pass