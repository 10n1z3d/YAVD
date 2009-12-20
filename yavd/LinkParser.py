#!/usr/bin/env python
#
# This file is part of YAVD (Yet Another Video Downloader).
#
# YAVD is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with YAVD.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: 10n1z3d <10n1z3d[at]w[dot]cn>

from VideoDataParser import VideoDataParser

class LinkParser():
    def __replaceHtmlEntities(self, video_title):
        '''Unescapes the html entities from the video title.

        Args:
            video_title: string Escaped video title

        Returns:
            video_title: string The unescaped video title.
        '''
        map = {'&quot;': '"',
               '&apos;': "'",
               '&amp;': '&',
               '&gt;': '',
               '&lt;': '',
               '|': '',
               '\t': '',
               '\n': '',
               '\r': ''
              }

        for esc, unesc in map.iteritems():
            video_title = video_title.replace(esc, unesc)

        return video_title

    def parseVideoData(self, video_url):
        '''Determines the website and parses the video title
        and download url of the video.

            Args:
                video_url: string

            Returns:
                video_title: string
                download_url: string
        '''
        data_parser = VideoDataParser()

        if 'youtube.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseYouTubeVideoData(video_url)
        elif 'metacafe.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseMetacafeVideoData(video_url)
        elif 'break.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseBreakVideoData(video_url)
        elif 'dailymotion.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseDailymotionVideoData(video_url)
        elif 'streetfire.net' in video_url:
            (video_title, download_url) = \
            data_parser.parseStreetFireVideoData(video_url)
        elif 'video.google.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseGoogleVideoData(video_url)
        elif 'clipfish.de' in video_url:
            (video_title, download_url) = \
            data_parser.parseClipfishVideoData(video_url)
        elif 'disclose.tv' in video_url:
            (video_title, download_url) = \
            data_parser.parseDiscloseVideoData(video_url)
        elif 'ebaumsworld.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseEbaumsworldVideoData(video_url)
        elif 'funnyjunk.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseFunnyjunkVideoData(video_url)
        elif 'liveleak.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseLiveleakVideoData(video_url)
        elif 'rutube.ru' in video_url:
            (video_title, download_url) = \
            data_parser.parseRutubeVideoData(video_url)
        elif 'dtrailer.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseDtrailerVideoData(video_url)
        elif '5min.com' in video_url:
            (video_title, download_url) = \
            data_parser.parse5minVideoData(video_url)
        elif 'blip.tv' in video_url:
            (video_title, download_url) = \
            data_parser.parseBlipVideoData(video_url)
        elif 'bofunk.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseBofunkVideoData(video_url)
        elif 'vids.myspace.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseMyspaceVideoData(video_url)
        elif 'graspr.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseGrasprVideoData(video_url)
        elif 'teachertube.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseTeachertubeVideoData(video_url)
        elif 'jokeroo.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseJokerooVideoData(video_url)
        elif 'sevenload.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseSevenloadVideoData(video_url)
        elif 'funnyordie.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseFunnyordieVideoData(video_url)
        elif 'shredordie.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseShredordieVideoData(video_url)
        elif 'greatamericans.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseGreatamericansVideoData(video_url)
        elif 'videowebtown.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseVideowebtownVideoData(video_url)
        elif 'snotr.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseSnotrVideoData(video_url)
        elif 'jwak.net' in video_url:
            (video_title, download_url) = \
            data_parser.parseJwakVideoData(video_url)
        elif 'worldstarhiphop.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseWorldstarthiphopVideoData(video_url)
        elif 'tinyclips.net' in video_url:
            (video_title, download_url) = \
            data_parser.parseTinyclipsVideoData(video_url)
        elif 'shockinghumor.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseShockinghumorVideoData(video_url)
        elif 'boomclips.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseBoomclipsVideoData(video_url)
        elif 'livevideo.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseLivevideoVideoData(video_url)
        elif 'wegame.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseWegameVideoData(video_url)
        elif 'kontraband.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseKontrabandVideoData(video_url)
        elif 'clipshack.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseClipshackVideoData(video_url)
        elif 'linux.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseLinuxVideoData(video_url)
        elif 'veryangrytoad.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseVeryAngryToadVideoData(video_url)
        elif 'monkeysee.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseMonkeySeeVideoData(video_url)
        elif 'vbox7.com' in video_url:
            (video_title, download_url) = \
            data_parser.parseVbox7VideoData(video_url)

        return (self.__replaceHtmlEntities(video_title), download_url)