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
#
# NOTE: Everything here is hardcoded and stupid but w/e.
# It took me some time to reverse some of the websites...

from urllib import unquote
from urllib import urlencode
from urllib2 import urlopen

class VideoDataParser():
    '''This class provides functions for parsing video title's and download link's
    for various video sharing websites.
    '''
    def parseYouTubeVideoData(self, video_url):
        # TODO: Add HD video download support
        '''Parses and returns the video title and download url of YouTube.com
        video.

            Args:
                url: string
                
            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_id = request.split("VIDEO_ID': '")[1].split("',")[0]
        video_title = request.split("'VIDEO_TITLE': '")[1].split("',")[0]
        token_value = request.split('"t": "')[1].split('",')[0]
        download_url = ('http://www.youtube.com/get_video?video_id=' + video_id +
                        '&t=' + token_value)

        return (video_title, download_url)

    def parseMetacafeVideoData(self, video_url):
        '''Parses and returns the video title and download url of Metacafe.com
        video.

            Args:
                url: string
                
            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' - Video</title>')[0]
        quoted = request.split('&mediaURL=')[1].split('&postRollContentURL=')[0]
        download_url = unquote(quoted)

        return (video_title, download_url)

    def parseDailymotionVideoData(self, video_url):
        # TODO: Add HD video download support
        '''Parses and returns the video title and download url of Dailymotion.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('vs_videotitle:"')[1].split('",vs_user:')[0]
        quoted = request.split('addVariable("video", "')[1].split('");')[0]
        download_url = unquote(quoted).split('||')[0]

        return (video_title, download_url)

    def parseBreakVideoData(self, video_url):
        '''Parses and returns the video title and download url of Break.com video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<div id="content-title"><h1>')[1]
        video_title = video_title.split('</h1>')[0]
        sGlobalContentFilePath = request.split("sGlobalContentFilePath='")[1]
        sGlobalContentFilePath = sGlobalContentFilePath.split("';")[0]
        sGlobalFileName = request.split("sGlobalFileName='")[1].split("';")[0]
        download_url = 'http://video1.break.com/dnet/media/' + sGlobalContentFilePath
        download_url += '/' + sGlobalFileName + '.flv'

        return (video_title, download_url)

    def parseStreetFireVideoData(self, video_url):
        '''Parses and returns the video title and download url of Streetfire.net
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' - Car Videos on')[0]
        video_conf = request.split("s2.addVariable('file','")[1].split("');")[0]
        request2 = urlopen('http://videos.streetfire.net' + unquote(video_conf))
        download_url = request2.read().split('<location><![CDATA[')[1]
        download_url = download_url.split(']]></location>')[0]

        return (video_title, download_url)

    def parseGoogleVideoData(self, video_url):
        '''Parses and returns the video title and download url of video.google.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = request.split('/googleplayer.swf?videoUrl\\x3d')[1]
        download_url = download_url.split('\\x26thumbnailUrl\\x3d')[0]

        return (video_title, unquote(download_url))

    def parseDataBGVideoData(self, video_url):
        '''Parses and returns the video title and download url of video.data.bg
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('"viewpagettl_video">')[1].split('</span>')[0]
        download_url = request.split('&file=')[1].split('&')[0]
        
        return (video_title, download_url)

    def parseClipfishVideoData(self, video_url):
        '''Parses and returns the video title and download url of Clipfish.de video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        config_path = request.split('data: "')[1].split('",')[0]
        request2 = urlopen('http://www.clipfish.de' + config_path).read()
        video_title = request2.split('<title><![CDATA[')[1].split(']]></title>')[0]
        download_url = request2.split('<filename>')[1].split('</filename>')[0]

        return (video_title, download_url)

    def parseDiscloseVideoData(self, video_url):
        '''Parses and returns the video title and download url of Disclose.tv video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        video_id = request.split('/videos/thumbnails/')[1].split('_')[0]
        download_url = 'http://www.disclose.tv/files/videos/videos/' + video_id + '.flv'
        
        return (video_title, download_url)

    def parseEbaumsworldVideoData(self, video_url):
        '''Parses and returns the video title and download url of eBaumsworld.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = request.split('&file=')[1].split('&showdigits=')[0]
        
        return (video_title, download_url)

    def parseFunnyjunkVideoData(self, video_url):
        '''Parses and returns the video title and download url of Funnyjunk.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = request.split('clip: "')[1].split('",')[0]
       
        return (video_title, download_url)

    def parseLiveleakVideoData(self, video_url):
        '''Parses and returns the video title and download url of Liveleak.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>LiveLeak.com - ')[1].split('</title>')[0]
        download_url = request.split('var convert_url = "')[1].split('"</script>')[0]
        
        return (video_title, unquote(download_url))

    def parseRutubeVideoData(self, video_url):
        '''Parses and returns the video title and download url of Rutube.ru video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('::')[0]
        download_url = request.split('?buffer_first=1.0&file=')[1]
        download_url = download_url.split('&xurl=')[0].replace('.iflv', '.flv')
        
        return (video_title, unquote(download_url))


    def parseDtrailerVideoData(self, video_url):
        '''Parses and returns the video title and download url of Dtrailer.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = 'http://dtrailer.com/dupload/trailerz/'
        download_url += request.split('s1.addVariable("file","')[1].split('");')[0]

        return (video_title, download_url)

    def parse5minVideoData(self, video_url):
        '''Parses and returns the video title and download url of 5min.com video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<h1 class="videoTitle">')[1].split('</h1>')[0]
        download_url = request.split('&videoUrl=')[1].split('&pageUrl=')[0]

        return (video_title, unquote(download_url))

    def parseBlipVideoData(self, video_url):
        '''Parses and returns the video title and download url of Blip.tv video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<div id="EpisodeTitle">')[1].split('</div>')[0]
        download_url = request.split('player.setPrimaryMediaUrl("')[1].split('?re')[0]
        
        return (video_title, download_url)

    def parseBofunkVideoData(self, video_url):
        '''Parses and returns the video title and download url of Bofunk.com video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_id = request.split('<embed src="/w/')[1].split('" quality="')[0]
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = 'http://media.bofunk.com/media/flvs/' + video_id + '.flv'

        return (video_title, download_url)

    def parseClipjunkieVideoData(self, video_url):
        '''Parses and returns the video title and download url of Clipjunkie.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' - clipjunkie.com</title>')[0]
        download_url = request.split("var file = '")[1].split("';")[0]

        return (video_title, download_url)

    def parseMyspaceVideoData(self, video_url):
        '''Parses and returns the video title and download url of vids.myspace.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        data = request.split('<link rel="image_src" href="')[1].split('" />')[0]
        vid = 'vid_' + data.split('thumb1_')[1].split('.jpg')[0]
        path = data.split('.com/')[1].split('/')[0]
        path2 = data.split(path + '/')[1].split('thumb1_')[0]
        video_title = request.split('<h1 id="tv_tbar_title">')[1].split('</h1>')[0]
        download_url = 'http://cache01-' + path + '.myspacecdn.com/' + path2 + vid +'.flv'
        
        return (video_title, download_url)

    def parseGrasprVideoData(self, video_url):
        '''Parses and returns the video title and download url of Graspr.com video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        config_url = 'http://www.graspr.com' + request.split('Variable("dataID", "')[1]
        request2 = urlopen(config_url.split('");')[0]).read()
        video_title = request.split('<title>')[1].split(' | Graspr.com</title>')[0]
        video_title = video_title.replace('\n', '')
        download_url = request2.split('&moviePath=')[1].split('&movieCode=')[0]
        
        return (video_title, download_url)

    def parseTeachertubeVideoData(self, video_url):
        '''Parses and returns the video title and download url of Teachertube.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>TeacherTube Videos - ')[1].split('</title>')[0]
        video_title = video_title.replace('\n', '')
        config = request.split("'config=")[1].split("',")[0]
        download_url = urlopen(config).read().split('Name="FLVPath" Value="')[1]
        download_url = download_url.split('"/>')[0]
        
        return (video_title, download_url)

    def parseJokerooVideoData(self, video_url):
        '''Parses and returns the video title and download url of Jokeroo.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' - Funny Videos')[0]
        download_url = request.split('vid:"')[1].split('", file_id:')[0]

        return (video_title, download_url)

    def parseSevenloadVideoData(self, video_url):
        '''Parses and returns the video title and download url of Sevenload.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        config = unquote(request.split('value="configPath=')[1].split(';')[0])
        video_title = request.split('<title>')[1].split(' - Video - sevenload</title>')[0]
        download_url = urlopen(config).read().split('<location seeking="yes">')[1]
        download_url = download_url.split('</location>')[0]

        return (video_title, download_url)

    def parseFunnyordieVideoData(self, video_url):
        '''Parses and returns the video title and download url of Funnyordie.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = 'http://videos0.ordienetworks.com/videos/'
        download_url += request.split('s1.addVariable("key","')[1].split('");')[0]
        download_url += '/sd.flv'
        
        return (video_title, download_url)

    def parseShredordieVideoData(self, video_url):
        '''Parses and returns the video title and download url of Shredordie.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = 'http://videos0.ordienetworks.com/videos/'
        download_url += request.split('s1.addVariable("key","')[1].split('");')[0]
        download_url += '/sd.flv'
        
        return (video_title, download_url)

    def parseGreatamericansVideoData(self, video_url):
        '''Parses and returns the video title and download url of Greatamericans.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>Watch ')[1].split('Video at')[0]
        config = request.split("'<scr' + 'ipt src=" + '"')[1].split('"></scr')[0]
        download_url = urlopen(config).read().split('?link=')[1].split('"')[0]

        return (video_title, download_url)

    def parseVideowebtownVideoData(self, video_url):
        '''Parses and returns the video title and download url of Videowebtown.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = request.split('/flvplayer.swf?file=')[1].split('&autostart')[0]
        
        return (video_title, unquote(download_url))

    def parseSnotrVideoData(self, video_url):
        '''Parses and returns the video title and download url of Snotr.com video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' - Snotr</title>')[0]
        download_url = 'http://videos.snotr.com/'
        download_url += + video_url.split('http://www.snotr.com/video/')[1] + '.flv'
        
        return (video_title, download_url)

    def parseJwakVideoData(self, video_url):
        '''Parses and returns the video title and download url of Jwak.net video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('Jwak.Net - ')[1].split('</title>')[0]
        download_url = request.split('"file","')[1].split('");')[0]

        return (video_title, download_url)

    def parseWorldstarthiphopVideoData(self, video_url):
        '''Parses and returns the video title and download url of Worldstarthiphop.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>Video: ')[1].split(' </title>')[0]
        download_url = request.split('playFLV.php?loc=')[1].split('&amp;')[0]

        return (video_title, download_url)

    def parseTinyclipsVideoData(self, video_url):
        '''Parses and returns the video title and download url of Tinyclips.net
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' -')[0]
        download_url = request.split('file=')[1].split('&image=')[0]

        return (video_title, download_url)

    def parseShockinghumorVideoData(self, video_url):
        '''Parses and returns the video title and download url of Shockinghumor.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = request.split('"file=')[1].split('&autostart=')[0]

        return (video_title, download_url)

    def parseBoomclipsVideoData(self, video_url):
        '''Parses and returns the video title and download url of Boomclips.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' -')[0]
        download_url = request.split('"file=')[1].split('&image=')[0]

        return (video_title, download_url)

    def parseLivevideoVideoData(self, video_url):
        '''Parses and returns the video title and download url of Livevideo.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' -')[0]
        config = unquote(request.split('?&video=')[1].split("', '")[0])
        path = config.split('&path=')[1].split('&t=')[0]
        video_id = request.split("mediaId = '")[1].split("';")[0]

        download_url = 'http://cdnec.livevideo.com/video/flash8/' + path + '/'
        download_url += video_id + '.flv'

        return (video_title, download_url)

    def parseWegameVideoData(self, video_url):
        '''Parses and returns the video title and download url of Wegame.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        config = request.split('xmlrequest: "')[1].split('",')[0]
        request2 = urlopen('http://www.wegame.com' + config).read()
        download_url = request2.split('<url><![CDATA[')[1].split(']]></url>')[0]

        return (video_title, download_url)

    def parseKontrabandVideoData(self, video_url):
        '''Parses and returns the video title and download url of Kontraband.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split(' at Kontraband')[0]
        config = request.split("'file',")[1].split('")')[0]
        config = config.replace('encodeURIComponent("', '')
        request2 = urlopen('http://www.kontraband.com' + config).read()
        download_url = request2.split('</track><track><location>')[1]
        download_url = download_url.split('</location>')[0]

        return (video_title, download_url)

    def parseClipshackVideoData(self, video_url):
        '''Parses and returns the video title and download url of Clipshack.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<span id="lblTitle">')[1].split('</span>')[0]
        video_key = video_url.split('key=')[1]
        request2 = urlopen('http://www.clipshack.com/GetPlaylist.aspx?key=' + video_key)
        download_url = request2.read().split('<location>')[1].split('</location>')[0]

        return (video_title, download_url)

    def parseLinuxVideoData(self, video_url):
        '''Parses and returns the video title and download url of Linux.com video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<title>')[1].split('</title>')[0]
        download_url = request.split('"file=')[1].split('&enablejs=')[0]

        return (video_title, download_url)

    def parseVeryAngryToadVideoData(self, video_url):
        '''Parses and returns the video title and download url of Veryangrytoad.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('"mainBoxHeader">')[1].split('</h1>')[0]
        download_url = ('http://www.veryangrytoad.com/flvideo/' +
                        video_url.split('/')[-2] + '.flv')
        
        return (video_title, download_url)

    def parseMonkeySeeVideoData(self, video_url):
        '''Parses and returns the video title and download url of Monkeysee.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<h1>')[1].split('</h1>')[0]
        config = 'http://www.monkeysee.com/%s' % \
        request.split('("video_id", "')[1].split('");')[0]
        request2 = urlopen(unquote(config)).read()
        download_url = request2.split('<File>')[1].split('</File>')[0]

        return (video_title, download_url)

    def parseVbox7VideoData(self, video_url):
        '''Parses and returns the video title and download url of Vbox7.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        video_id = video_url.split('play:')[1][0:8]
        request = urlopen(video_url).read()
        video_title = request.split('titlenew">')[1].split('</span>')[0]
        post_data = urlencode({'onLoad': '[type Function]', 'vid' : video_id})
        request2 = urlopen('http://www.vbox7.com/play/magare.do', post_data).read()
        download_url = request2.split('&videoFile=')[1].split('&')[0]

        return (video_title, download_url)

    def parseAniboomVideoData(self, video_url):
        '''Parses and returns the video title and download url of Aniboom.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        video_id = video_url.split('video/')[1].split('/')[0]
        request = urlopen(video_url).read()
        video_title = request.split('<title>Watch ')[1].split(' ')[0]
        download_url = 'http://newmedia.aniboom.com/http/%s.flv' % video_id

        return (video_title, download_url)

    def parseExpotvVideoData(self, video_url):
        '''Parses and returns the video title and download url of Expotv.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('title: "')[1].split('",')[0]
        download_url = request.split('url: "')[2].split('",')[0]

        return (video_title, download_url)

    def parseGubbtvVideoData(self, video_url):
        '''Parses and returns the video title and download url of Gubb.tv
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('content="Gubb.tv - ')[1].split(' "/>')[0]
        download_url = request.split('"file=')[1].split('&wmode=')[0]

        return (video_title, download_url)

    def parseNaroiaciVideoData(self, video_url):
        '''Parses and returns the video title and download url of Na-roiaci.com
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('id="viewvideo-title">')[1].split('</div>')[0]
        video_title = video_title.replace('  ', '')
        download_url = request.split('&flv=')[1].split('&autostart=')[0]

        return (video_title, download_url)

    def parseAnimeFreakVideoData(self, video_url):
        '''Parses and returns the video title and download url of Animefreak.tv
        video.

            Args:
                url: string

            Returns:
                video_title: string, download_url: string
        '''
        request = urlopen(video_url).read()
        video_title = request.split('<h1>')[1].split('</h1>')[0]
        download_url = request.split('.xml&file=')[1].split('&image=')[0]
        
        return (video_title, download_url)