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


import anki.notes
from anki.collection import Collection
from chinese.fill import (
    bulk_fill_all,
    bulk_fill_transcript,
    bulk_fill_defs,
    bulk_fill_hanzi,
    bulk_fill_usage,
    bulk_fill_classifiers,
    bulk_fill_frequency,
    bulk_fill_silhouette,
    bulk_fill_sound
)
from unittest.mock import Mock, patch
from tests import Base, get_empty_col


def add_chinese_model(col: Collection) -> dict:
    m = col.models.current()
    m2 = col.models.copy(m)

    for f in ['Hanzi', 'Color', 'Pinyin', 'English', 'Sound',
              'Examples', 'Classifier', 'Frequency', 'Silhouette']:
        fm = col.models.new_field(f)
        col.models.add_field(m2, fm)

    col.models.save(m2)  # !!!
    return m2


def _clear_note(col: Collection, ni: anki.notes.NoteId) -> None:
    n = col.get_note(ni)
    for k in n.keys():
        if k != "Hanzi":
            n[k] = ""
    col.update_note(n, skip_undo_entry=True)


class BulkFill(Base):

    # Issue BorisNA#4
    def test_bulk_fill_empty_col(self):
        col = get_empty_col()
        self.assertEqual(col.note_count(), 0)

        with patch('chinese.fill.mw.col') as mcol, \
                patch('chinese.sound.AudioDownloader') as msound, \
                patch('chinese.fill.sleep'):
            mcol.find_notes = Mock(return_value=[])
            mcol.get_note = Mock(side_effect=col.get_note)
            mcol.update_note = Mock(side_effect=col.update_note)
            mcol.models = Mock(field_names=Mock(side_effect=col.models.field_names))
            msound.return_value.download = Mock(return_value='mocked.mp3')

            bulk_fill_all()
            bulk_fill_transcript()
            bulk_fill_hanzi()
            bulk_fill_defs()
            bulk_fill_usage()
            bulk_fill_classifiers()
            bulk_fill_frequency()
            bulk_fill_silhouette()
            bulk_fill_sound()


    # Issue Gustaf-C#83
    def test_bulk_fill_card_without_hanzi(self):
        col = get_empty_col()
        m2 = add_chinese_model(col)

        notes = []

        note = col.new_note(col.models.by_name("Basic"))
        col.addNote(note)
        notes.append(note.id)

        note = col.new_note(m2)
        note["Hanzi"] = "猫"
        col.addNote(note)
        notes.append(note.id)
        note_id = note.id

        self.assertEqual(col.note_count(), 2)

        with patch('chinese.fill.mw.col') as mcol, \
                patch('chinese.sound.AudioDownloader') as msound, \
                patch('chinese.fill.sleep'):
            mcol.find_notes = Mock(return_value=notes)
            mcol.get_note = Mock(side_effect=col.get_note)
            mcol.update_note = Mock(side_effect=col.update_note)
            mcol.models = Mock(field_names=Mock(side_effect=col.models.field_names))
            msound.return_value.download = Mock(return_value='mocked.mp3')

            bulk_fill_all()
            self.assertEqual(col.get_note(note_id)["Pinyin"],
                             '<span class="tone1">māo</span> <!-- mao -->')

            _clear_note(col, note_id)
            bulk_fill_transcript()
            self.assertNotEqual(col.get_note(note_id)["Pinyin"], '')
            bulk_fill_hanzi()
            self.assertNotEqual(col.get_note(note_id)["Color"], '')

            _clear_note(col, note_id)
            bulk_fill_defs()
            self.assertNotEqual(col.get_note(note_id)["English"], '')

            _clear_note(col, note_id)
            bulk_fill_usage()
            self.assertNotEqual(col.get_note(note_id)["Examples"], '')

            _clear_note(col, note_id)
            bulk_fill_classifiers()
            self.assertNotEqual(col.get_note(note_id)["Classifier"], '')

            _clear_note(col, note_id)
            bulk_fill_frequency()
            self.assertNotEqual(col.get_note(note_id)["Frequency"], '')

            _clear_note(col, note_id)
            bulk_fill_silhouette()
            self.assertNotEqual(col.get_note(note_id)["Silhouette"], '')

            _clear_note(col, note_id)
            bulk_fill_sound()
            self.assertNotEqual(col.get_note(note_id)["Sound"], '')
