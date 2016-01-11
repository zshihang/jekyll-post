#!/usr/bin/env python

import os
import sys
import argparse
from datetime import datetime
from tzlocal import get_localzone


def main():
    parser = argparse.ArgumentParser(prog='jekyll_post',
                                     description='Create a post')
    parser.add_argument('title')
    args = parser.parse_args()

    post_dir = '_posts/'
    if not os.path.exists(post_dir):
        print("Please cd into root directory of your site.")
        sys.exit()

    # define datetime in UTC local timezone
    local_tz = get_localzone()
    fmt = "%Y-%m-%d %H:%M:%S %z"
    dt = datetime.now(tz=local_tz)
    date = dt.strftime(fmt)

    # define filename
    filename_date = "{:d}-{:d}-{:d}".format(dt.year, dt.month, dt.day)
    filename_title = ''.join(c for c in args.title.replace(' ', '-')
                             if c.isalnum() or c == '-') + '.md'
    filename = filename_date + '-' + filename_title

    filepath = post_dir+filename
    if os.path.exists(filepath):
        print(filename, "already exists.")
        sys.exit()

    with open(filepath, 'w') as f:
        f.write('---\n')
        f.write('layout: post\n')
        f.write("title: {}\n".format(args.title))
        f.write("date: {}\n".format(date))
        f.write('---\n')

    print(filename, "has been created.")

if __name__ == '__main__':
        main()
