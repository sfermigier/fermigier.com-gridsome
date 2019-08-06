#!/usr/bin/env python
import sys
from pprint import pprint

import dataset


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


    content = "---\n"
    content += f"""title: \"{title_escaped}\"\n"""
    content += f"date: {date:%Y-%m-%d}\n"
    content += f"path: {year}/{month}/{slug}\n"
    content += "---\n\n"
    content += body

    open(filename, "w").write(content)
    # sys.exit()


main()

