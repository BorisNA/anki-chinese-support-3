# Copyright © 2024 Boris Nazaroff
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


from unittest.mock import MagicMock, Mock, patch

from chinese.fill import (
    bulk_fill_all,
    bulk_fill_transcript
)

from tests import Base, get_empty_col

# FIXME: ? move to the __init__ or shared

from anki.collection import Collection

def add_chinese_model(col : Collection) -> dict:
    m = col.models.current()
    m2 = col.models.copy(m)

    for f in ['Hanzi', 'Color', 'Pinyin', 'English', 'Sound']:
        fm = col.models.new_field(f)
        col.models.add_field(m2, fm)

    col.models.save( m2 ) # !!!
    return m2


class BulkFill(Base):
    # Issue Gustaf-C#83
    def test_bulk_fill_card_without_hanzi(self):
        col = get_empty_col()
        m2 = add_chinese_model(col)

        notes = []

        note = col.new_note( col.models.by_name("Basic") )
        col.addNote(note)
        notes.append( note.id )

        note = col.new_note( m2 )
        note["Hanzi"] = "上海"
        col.addNote(note)
        notes.append( note.id )
        note_id = note.id

        self.assertEqual(col.note_count(), 2)

        with patch ( "chinese.fill.mw.col" ) as mcol:
            mcol.find_notes = Mock( return_value=notes )
            mcol.get_note = Mock( side_effect=col.get_note )
            mcol.update_note = Mock( side_effect=col.update_note )
            mcol.models = Mock( field_names = Mock( side_effect=col.models.field_names ) )

            # FIXME: test all other bulk fills
            bulk_fill_all()
            self.assertEqual( col.get_note( note_id )["Pinyin"],
                              '<span class="tone4">shàng</span>'
                              '<span class="tone3">hǎi</span> <!-- shang hai -->')
