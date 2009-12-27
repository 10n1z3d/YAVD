#!/usr/bin/env python
#
# YAVD (Yet Another Video Downloader)
# Copyright (C) 2009 10n1z3d <10n1z3d[at]w[dot]cn>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__version__ = '0.5'

import sys

from optparse import OptionParser

from yavd.LinkParser import LinkParser
from yavd.VideoDownloader import VideoDownloader

def header():
    print ' ___ ___ _______ ___ ___ _____  '
    print '|   |   |   _   |   |   |     \ '
    print ' \     /|       |   |   |  --  |'
    print '  |___| |___|___|\_____/|_____/ '
    print '  Yet Another Video Downloader  '
    print '       10n1z3d[at]w[dot]cn      '
    print '          Version: %s         \n' % __version__

def usage():
    print 'Usage: python ./yavd.py <url> [options]'
    print 'Options:'
    print '      -l, --link               Just output the video download link.'
    print '      -q, --quiet              Quiet mode (no console output).'
    print '      -p, --path=<save_path>   Save path (e.g. /home/videos/).\n'

def parseOptions():
    try:
        video_url = sys.argv[1]
        parser = OptionParser(add_help_option=False)
        parser.add_option('-h', '--help', action='store_true',
                          dest='help', default=False)
        parser.add_option('-l', '--link', action='store_true',
                          dest='show_link', default=False)
        parser.add_option('-q', '--quiet', action='store_false',
                          dest='verbose', default=True)
        parser.add_option('-p', '--path', dest="save_path", default=None)

        (options, args) = parser.parse_args()

        return (video_url, options.show_link, options.verbose,
                options.save_path, options.help)
    except:
        usage()
        exit(2)

def main():
    (video_url, show_link, verbose, save_path, help) = parseOptions()

    if verbose: header()
    if help: usage(); exit(0)

    link_parser = LinkParser()
    video_downloader = VideoDownloader()

    website = video_url.replace('http://', '').replace('www.', '').split('/')[0]

    try:
        (video_title, download_url) = link_parser.parseVideoData(video_url)
    except:
        print '[-] Error. Could not parse the video data.'
        print ('[!] This might be caused because the video url is invalid or '
               'the website is not supported.\n')
        exit(1)

    if show_link:
        if verbose:
            print '[+] Video title: "%s"' % video_title
            print '[+] Download link: %s\n' % download_url
        else:
            print download_url
        exit(0)

    try:
        video_downloader.downloadVideo(website, video_title, download_url,
                                       save_path, verbose)
    except:
        print '\n[-] Error. Could not download the video.\n'
        exit(1)
                                   
if __name__ == "__main__":
    main()
