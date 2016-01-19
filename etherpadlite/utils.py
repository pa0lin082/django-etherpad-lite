# -*- coding: utf-8 -*-
__author__ = 'elfo'

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)



from models import PadServer, PadGroup, PadAuthor
from django.conf import settings





def get_current_pad_server():
    if settings.DEBUG:
        return PadServer.objects.get(title='debug server')
    else:
        return PadServer.objects.get(title='production server')



def get_or_create_author(user=None):
    if not user:
        raise Exception('invalid user')
    pad_server = get_current_pad_server()
    pad_author, created = PadAuthor.objects.get_or_create(user=user, server=pad_server)
    return pad_author



def add_user_to_padgroup(padgroup=None, user=None):
    pad_author = get_or_create_author(user=user)
    pad_author.group.add(padgroup)
    pad_author.EtherMap()

    return pad_author


def generate_pad_group_from_room_hash(hash=None):
    if not hash:
        raise Exception('Hash not valid')

    pad_server = get_current_pad_server()

    pad_group, created = PadGroup.objects.get_or_create(server=pad_server, groupName=hash)
    # pad_group.save()

    return pad_group