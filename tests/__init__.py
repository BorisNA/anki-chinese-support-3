# Copyright © 2018-2019 Joseph Lorimer <joseph@lorimer.me>
#
# This file is part of Chinese Support 3.
#
# Chinese Support 3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Chinese Support 3 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Chinese Support 3.  If not, see <https://www.gnu.org/licenses/>.

from gettext import NullTranslations
from json import load
from logging import getLogger
from tempfile import mkdtemp
from unittest import TestCase
from unittest.mock import MagicMock, patch
from os import path, pardir
import os
import shutil
import tempfile

from anki.collection import Collection as aopen

network_integration = False

NullTranslations().install()

# FIXME: Find a better solution for this
modules = {
    # anki is needed for bulk fill
    # 'anki': MagicMock(),
    # 'anki.stdmodels': MagicMock(),
    'anki.template': MagicMock(),
    # 'anki.notes': MagicMock(),
    'anki.find': MagicMock(),
    'anki.hooks': MagicMock(),
    'anki.lang': MagicMock(),
    'anki.stats': MagicMock(),
    'anki.template.hint': MagicMock(),
    'anki.utils': MagicMock(),
    'aqt': MagicMock(),
    'aqt.editor': MagicMock(),
    'aqt.utils': MagicMock(),
    'aqt.qt': MagicMock(),
}

if network_integration:
    media_dir = mkdtemp()
else:
    media_dir = 'collection.media'
    modules['gtts'] = MagicMock()
    modules['gtts.tts'] = MagicMock()
    modules['requests'] = MagicMock()

patch.dict('sys.modules', modules).start()

configDir = path.join(path.abspath(path.join(path.dirname(path.abspath(__file__)), pardir)), "chinese")
with open(path.join(configDir, "config.json"), encoding='utf-8') as config_fd:
    config = load(config_fd)

patch('aqt.mw.addonManager.getConfig', lambda a: config).start()
patch('aqt.mw.col.media.dir', MagicMock(return_value=media_dir)).start()


class Base(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.logger = getLogger()
        self.logger.setLevel('DEBUG')

## From anki code: pylib/shared/tests.py

# Creating new decks is expensive. Just do it once, and then spin off
# copies from the master.
_emptyCol: str | None = None


def get_empty_col():
    global _emptyCol
    if not _emptyCol:
        (fd, path) = tempfile.mkstemp(suffix=".anki2")
        os.close(fd)
        os.unlink(path)
        col = aopen(path)
        col.close(downgrade=False)
        _emptyCol = path
    (fd, path) = tempfile.mkstemp(suffix=".anki2")
    shutil.copy(_emptyCol, path)
    col = aopen(path)
    return col

