#!/usr/bin/env python3

# Copyright 2018 Joseph Lorimer <joseph@lorimer.me>
#
# Permission to use, copy, modify, and distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright
# notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
# INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
# LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.

from re import sub

from markdown2 import markdown


def main():
    """Covert GitHub mardown to AnkiWeb HTML."""
    # permitted tags: img, a, b, i, code, ul, ol, li

    translate = [
        (r'<h1>([^<]+)</h1>', r''),
        (r'<h2>([^<]+)</h2>', r'<b><i>\1</i></b>\n\n'),
        (r'<h3>([^<]+)</h3>', r'<b>\1</b>\n\n'),
        (r'<strong>([^<]+)</strong>', r'<b>\1</b>'),
        (r'<em>([^<]+)</em>', r'<i>\1</i>'),
        (r'<kbd>([^<]+)</kbd>', r'<code><b>\1</b></code>'),
        (r'</a></p>', r'</a></p>\n'),
        (r'<p>', r''),
        (r'</p>', r'\n\n'),
        (r'</(ol|ul)>(?!</(li|[ou]l)>)', r'</\1>\n'),
    ]

    with open('README.md', encoding='utf-8') as f:
        html = ''.join(filter(None, markdown(f.read()).split('\n')))

    for a, b in translate:
        html = sub(a, b, html)

    with open('README.html', 'w', encoding='utf-8') as f:
        f.write(html.strip())
        
    print("Conversion done")


if __name__ == '__main__':
    main()
