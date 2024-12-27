# Chinese Support 3

This is a [fork](https://github.com/BorisNA/anki-chinese-support-3) of the [Chinese Support 3](https://github.com/Gustaf-C/anki-chinese-support-3) addon, which in turn was also a fork from [original](https://github.com/ttempe/chinese-support-addon) Chinese Support add-on and its [redux version](https://github.com/luoliyan/chinese-support-redux).

Its goal is fixing open bugs and improving Anki 23/24 compatibility. No major changes are planned.

Current release is [0.17.1-RB-1](#0171-RB-1) "reborn". It is not available on the ankiweb, but can be downloaded from [Releases](https://github.com/BorisNA/anki-chinese-support-3/releases) page and installed manually. It is **highly recommended** to disable the old addon before loading the new one. 

Upon install it will try to intelligently load the saved config from the old addon. This action is performed once, on the first run. You can delete `meta.json` in the addon folder to rerun it, but it will revert all changes in the new addon prior to re-importing. 

To uninstall disable it first (see known issues in the [Release](#0171-RB-1) description)

## Chinese Support 3 description (original)

Chinese Support 3 is an Anki 23.10-compatible version of the [original](https://github.com/ttempe/chinese-support-addon) Chinese Support add-on and its [redux version](https://github.com/luoliyan/chinese-support-redux). I have tested it on 2.1.66 which seems to work, no testing has been done on earlier versions though. It offers a number of features that streamline the process of creating flashcards for learning Chinese. Some of the features had stopped working, and after taking my time to get these back going I thought that I might as well publish it for others to use.

Please note that the add-on is still in beta and is sometimes shipped in an unstable state. Please upgrade with each new release and report any issues on GitHub. The automated test suite is a work-in-progress, so I still rely heavily on user reports to supplement my own manual testing.

## Important Notes

- The templates can be found under 'Choose Note Type' -> 'Manage' -> 'Add'
- **If you have previously downloaded corrupted TTS sound files with the redux addon, these need to be removed and downloaded again for the sound to work.**
- If you find that a field is not filling at all, please check [config.json](https://github.com/luoliyan/chinese-support-redux/blob/master/chinese/config.json) for the complete list of valid field names. For those migrating from an older version of the add-on, you will need to rename any definition fields to `English`, `German` or `French`, depending on what you want.
- If tone colours are not showing, ensure that the styling section of the template contains the following CSS:

```css
.tone1 {color: red;}
.tone2 {color: orange;}
.tone3 {color: green;}
.tone4 {color: blue;}
.tone5 {color: gray;}
```

## Features

- Automatic field filling
  - Translation (from built-in dictionary; supports English, German and French)
  - Romanisation (supports [Pīnyīn (拼音)](https://en.wikipedia.org/wiki/Pinyin) and Cantonese [Jyutping (粵拼)](https://en.wikipedia.org/wiki/Jyutping))
  - Mandarin Audio (fetched from Google or Baidu)
  - Traditional (繁體字) and simplified (簡體字) characters
  - [Bopomofo (ㄅㄆㄇㄈ)](https://en.wikipedia.org/wiki/Bopomofo), also known as Zhuyin (注音)
  - [Rubies](https://www.w3schools.com/tags/tag_ruby.asp) (small-print transcription placed above characters)
  - Frequency (from “very basic” to “obscure”) - based on [anki-chinese-word-frequency](https://github.com/ernop/anki-chinese-word-frequency)
  - Usage Sentence Examples - Chinese/English sentence pairs from [Tatoeba](https://tatoeba.org/)
- Automatic tone change of auto filled pinyin (hanzi field must be populated)
  - E.g. fen1kai1 -> *Tab* -> fēnkāi (won't replace existing tones)
- Tone colours (applied to characters, romanisation and Bopomofo)
- Built-in note types (Basic and Advanced)

## Status

I do occasionally run into problems with the addon, but so far I have been able to solve all of them by at worst restarting Anki. For the time being I plan to only release minor maintenence updates, but I do have more features in mind when I have more time available.

The vast majority of features have been successfully ported, and the add-on is in a usable state, albeit with some definite rough edges.

The add-on is still in beta. By this I mean “it works, but I wouldn’t trust it with my children”. Expect occasional issues, and please make a back-up before trying it. I use it myself and haven't experienced data loss, but _your_ mileage may vary.

Please report any issues [here](https://github.com/Gustaf-C/anki-chinese-support/issues) on GitHub. Feature requests are also welcome. Pull requests even more so.

If you are new to the Chinese Support add-on, the wiki from the previous version is still relevant ([here](https://github.com/ttempe/chinese-support-addon/wiki)).

## Usage

The core feature of the add-on is the automatic field filling. To take advantage of this, you need to have an Anki note type with the appropriate fields (e.g., `Hanzi`, `English`, `Pinyin`, `Sound`). See `config.json` for a list of valid field names.

If you don't already have such a note type, the easiest approach is to use one of the built-in models. Two types are installed automatically: Basic and Advanced. The only important difference is that the Advanced model shows more information.

To use the field-filling features:

1. Add a new note to Anki (press *a*)
2. Create (manage -> add) and select `Chinese (Basic)` or `Chinese (Advanced)` as the note type
3. Enable Chinese Support 3 for this note type (click `汉字`)
4. Enter a word (e.g., 電話) into the `Hanzi` field (sentences will also work)
5. Press *Tab*
6. The remaining fields should then be populated automatically

<br>

## Screenshots

![Screenshot #1](https://raw.githubusercontent.com/Gustaf-C/anki-chinese-support/master/screenshots/add-card.png)

![Screenshot #2](https://raw.githubusercontent.com/Gustaf-C/anki-chinese-support/master/screenshots/view-card.png)

<br>

## Support

If you encounter any issues, the best way to have these addressed is to [raise them on GitHub](https://github.com/Gustaf-C/anki-chinese-support/issues). Feature requests are welcome, with the caveat that all good things take time. Pull request to fix any issues are even more welcome.

## Known Issues

Please see the bug tracker on [GitHub](https://github.com/BorisNA/anki-chinese-support/issues) and for original add-on on [Upstream GitHub](https://github.com/Gustaf-C/anki-chinese-support/issues).

## Changelog

### 0.17.1-RB-1
This is mainly a bugfix release. Get it at [Releases](https://github.com/BorisNA/anki-chinese-support-3/releases) page
- **Features**
  - New option `lowercase_ruby` is added to the config. If set to `True` (default), then pinyin will be converted to lowercase when generating rubies. It is useful if you have pre-filled pinyin, especially in sentences or names.
  - Implemented standard Anki config. Default values are stored in `config.json` and user changes - in `meta.json`. Fixes losing user changes in 'Tools/Addons/Config'
 
- **Bugfixes**
  - Fix always colorizing uppercase pinyin as tone-5 (Gustaf-C#83) 
  - Fix crashes if processed deck contains notes without any "hanzi" field (Gustaf-C#83)
  - Fix crashes if no desk was selected (#4)
  - Fix incorrect reporting of processed notes (#5)

- **Release known issues**
  - Bulk operations progress is not shown (changes in Anki 23/24), operations appears to be frozen until it completes (see #6)
  - No undo on bulk fill and in-editor colorization (see #6)
  - Dictionary database inside the addon is kept locked, causing errors on addon removal and preventing addon update/uninstall (#8). If you want to uninstall it, disable it first, reload Anki and unistall (or just start it with the Shift key)
  
---
**>> original Chinese Support 3 releases**

### 0.XX.X

- **Bugfixes**
  - Fix colorization of fields in editor (known issue: visual bug in editor with Anki 23.12.1 and earlier)

### 0.17.1

- **Bugfixes**
  - Fix for Baidu TTS

### 0.17.0

- **Features**
  - Improved clarity for when 汉字 button is clicked
  - No longer append classifier and alternates to definitions, use the appropriate fields instead
  - Introduced separate fields for simplified and traditional classifiers
- **Bugfixes**
  - Allow using addon in both add note and browse windows at the same time (known issue: button will not update between windows)
  - Fixed crash after switching profile
  - Final b and r will no longer be deleted from definitions
  - Fixed a crash if trying to autofill an emoji
  - Fixed 汉字 button sometimes not showing whether the addon is actually activated

### Redux to 0.16.0

Note that this is the **last update for 2.1.66**.

- **Features**
  - Updated for Qt6
  - Stop automatically creating the model decks, still available as template
  - Added bulk fill frequency
  - Simplified and traditional fields will always be filled
  - Always fill color hanzi when bulk filling
- **Bugfixes**
  - Fixed Google & Baidu TTS
  - Removed extra final new line from translations
  - Fixed error when certain special characters were in hanzi field
- **Misc**
  - Updated dictionaries
  - Reduced addon size by not shipping the dictionary backup
  - Backend tweaks
