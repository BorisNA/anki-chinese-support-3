# Copyright © 2012 Roland Sieker <ospalh@gmail.com>
# Copyright © 2012 Thomas TEMPÉ <thomas.tempe@alysse.org>
# Copyright © 2017-2019 Joseph Lorimer <joseph@lorimer.me>
# Copyright © 2020 Joe Minicucci <https://joeminicucci.com>
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

from collections import defaultdict
from json import dump, load
from os.path import dirname, exists, join, realpath

from aqt import mw


class ConfigManager:
    def __init__(self):
        self._load_config()
        mw.addonManager.setConfigUpdatedAction(__name__, lambda *_: self._config_updated_handler())

    def _load_config(self):
        self.config = mw.addonManager.getConfig(__name__)

    def _config_updated_handler(self):
        self._load_config()

    def __setitem__(self, key, value):
        self.config[key] = value

    def __getitem__(self, key):
        return self.config[key]

    def update(self, d):
        self.config.update(d)

    def save(self):
        mw.addonManager.writeConfig(__name__, self.config)

    def get_fields(self, groups=None):
        if not groups:
            groups = list(self.config['fields'])
        fields = []
        for g in groups:
            if g in self.config['fields']:
                fields.extend(self.config['fields'][g])
        return fields

    def get_config_scalar_value(self, keyName):
        return self.config[keyName] if keyName in self.config else None
