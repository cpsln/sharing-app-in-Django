from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError
import sys
from .models import Permissions



FILE_UPLOADER = "uploader"
FILE_DOWNLOADER = "downloader"

def setup_user_groups(stdout_stream):
    # Create the required groups
    uploader_group, uploader_group_created = __create_group(FILE_UPLOADER, stdout_stream)
    downloader_group, downloader_group_created = __create_group(FILE_DOWNLOADER, stdout_stream)

    # Create permission for uploading files
    __create_group_permission(  codename='can_upload_files',
                                name='Can Upload Files',
                                content_type=ContentType.objects.get_for_model(Permissions),
                                group=uploader_group,
                                stdout_stream=stdout_stream)
        # Create permission for downloading files
    __create_group_permission(  codename='can_download_files',
                                name='Can Download Files',
                                content_type=ContentType.objects.get_for_model(Permissions),
                                group=downloader_group,
                                stdout_stream=stdout_stream)


def __create_group(group_name, stdout_stream):
    if stdout_stream != None:
        stdout_stream.write("Creating group {}...\n".format(group_name))
    return Group.objects.get_or_create(name=group_name)


def __create_group_permission(codename, name, content_type, group, stdout_stream):
    if stdout_stream != None:
        stdout_stream.write("Creating permission {}.{}...\n".format(content_type, codename))
    the_permission, created = Permission.objects.get_or_create(codename=codename, name=name, content_type=content_type)
    if stdout_stream != None:
        stdout_stream.write("Assigning permission {}.{} to group {}...\n".format(content_type, codename, group.name))

    group.permissions.add(the_permission)