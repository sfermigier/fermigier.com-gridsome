#!/usr/bin/env python
import re
import sys
from pprint import pprint

import bleach
import dataset
from markdown import markdown


def main():
    db = dataset.connect('sqlite:///data/fermigier.com.db')

    posts = db['post'].all()
    for post in posts:
        # pprint(dict(post))
        make_post(post)


def make_post(post):
    # pprint(dict(post))
    # sys.exit()
    title = post['title']
    date = post['date']
    year = post['date'].year
    month = date.month
    day = date.day
    slug = post['slug']
    body = post['body_markdown']

    filename = f"blog/{year}-{month}-{day}-{slug}.md"
    title_escaped = title.replace('"', r'\"')
    summary = make_summary(body)
    summary_escaped = summary.replace('"', r'\"')
    tags = make_tags(body)

    content = "---\n"
    content += f"title: \"{title_escaped}\"\n"
    content += f"date: {date:%Y-%m-%d}\n"
    content += f"path: blog/{year}/{month}/{slug}\n"
    content += f"summary: \"{summary_escaped}\"\n"
    content += f"tags: {tags}\n"
    content += "---\n\n"
    content += body

    open(filename, "w").write(content)
    # sys.exit()


def make_summary(body):
    html = markdown(body)
    text = bleach.clean(html, tags=[], strip=True)

    m = re.match(r"^(.*?)[.?!]\s", text, re.DOTALL)

    if not m:
        return ""

    summary = m.group(1).strip()
    summary = re.sub(r"\s+", " ", summary)
    return summary + "."


def make_tags(body):
    html = markdown(body)
    text = bleach.clean(html, tags=[], strip=True)

    tags = []

    keywords = [
        "Abilian",
        "Nuxeo",
        #
        "Python",
        "Zope",
        "CPS",
        #
        "Java",
        "Eclipse",
        "Apache",
        "OW2",
        #
        "Linux",
        "GNU",
        "Debian",
        "Ubuntu",
        "Mandriva",
        "Mandrake",
        "Red Hat",
        "GNOME",
        "KDE",
        #
        "AFUL",
        "GTLL",
        "CNLL",
        "Open Source",
        "Brevets",
        "SCO",
        "Miscrosoft",
        "OpenOffice",
        "LibreOffice",
        "Mozilla",
    ]

    words = set(re.split(r"\W+", text))
    words_lower = {w.lower() for w in words}

    for kw in keywords:
        if " " in kw and kw in text:
            tags += [kw]
        elif kw.lower() in words_lower:
            tags += [kw]

    if tags:
        return tags
    else:
        return ["Misc"]


main()

