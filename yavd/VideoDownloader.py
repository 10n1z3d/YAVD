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

import os
import sys
import urllib

class VideoDownloader():
    '''The main class used for downloading the videos from the website.'''
    def __showProgress(self, blocks, block_size, total_size, bar_width=40):
        '''Simple progress bar function.

        Args:
            bar_width: integer The maximum width of the progress bar.

        Example output:
            [ ======> 34%                ]
        '''
        width = bar_width - 10
        percent = (blocks * block_size * 100) / total_size
        equals = (percent * width) / 100
        spaces = (width-equals-len(str(percent))) + 3

        progressBar = '[ %s> %s%%%s ]' % ('=' * equals, str(percent), ' ' * spaces)

        sys.stdout.write('\r' + progressBar)

        if percent == 100:
            sys.stdout.write('\n\n')

        sys.stdout.flush()

    def downloadVideo(self, website, video_title, download_url, save_path,
                      verbose=True):
        '''Simple function to download the videos from web using
        urllib.urlretrieve.

        Args:
            website: string The name of the website we are downloading the video
            from.
            video_title: string
            download_url: string
            save_path: string 
        '''
        if verbose:
            print '[+] Website: %s' % website.capitalize()
            print '[+] Video title: "%s"' % video_title
            
            if save_path != None:
                print '[+] Save path: %s' % save_path

                if os.path.exists(save_path):
                    print '[+] Downloading "%s.flv"...\n' % video_title
                    urllib.urlretrieve(download_url, save_path + video_title +
                                       '.flv', reporthook=self.__showProgress)

                    print '[+] Done. The video is saved in "%s"\n' % save_path
                else:
                    print '\n[!] Error. %s does not exist!' % save_path
                    print ('[?] Do you want to continue downloading the video in'
                           ' the current directory? [y/n]')

                    user_choice = raw_input()
                    if user_choice.lower() in ['y', 'yes']:
                        urllib.urlretrieve(download_url, video_title +
                                           '.flv', reporthook=self.__showProgress)
                        print '[+] Done.\n'
                    else:
                        print '\n[-] Download aborted.\n'
                        return
            else:
                print '[+] Downloading "%s.flv"...\n' % video_title
                urllib.urlretrieve(download_url, video_title +
                                   '.flv', reporthook=self.__showProgress)
                print '[+] Done.\n'
        else:
            urllib.urlretrieve(download_url, video_title + '.flv')