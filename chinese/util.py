# Copyright 2012 Thomas TEMPÉ <thomas.tempe@alysse.org>
# Copyright 2017-2018 Joseph Lorimer <luoliyan@posteo.net>
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html

from re import sub


def no_hidden(text):
    return sub(r'<!--.*?-->', '', text)


def no_sound(text):
    """Remove Anki [sound:xxx.mp3] tag.

    If it isn't removed, it can be duplicated.
    """
    return sub(r'\[sound:.*?]', '', text)