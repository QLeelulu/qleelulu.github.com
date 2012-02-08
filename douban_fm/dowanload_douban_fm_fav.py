#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
仅供学习交流使用，请勿用于其他用途。
感谢[豆瓣FM]伴我写代码的日日夜夜。
至于用途，请看文件名。

注： 文件会下载到当前目录
依赖：wget, python2.6 or python2.7

使用：
        Linux、Mac下请安装wget
        Win下请安装"wget for window"
        如果是python2.5，请自己提供json库
'''
__author__ = 'qleelulu@gmail.com (@QLeelulu)'


import os, sys, urllib, urllib2, cookielib, re, json

url_pic_request="http://douban.fm/j/new_captcha"
url_pic ="http://douban.fm/misc/captcha?size=m&id="

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
captcha_id=opener.open(url_pic_request).read().replace('"','')  
url_login = 'http://douban.fm/j/login'
alias = raw_input('输入用户名:')
form_password = raw_input('输入密码:')
print u'请将如下链接复制到浏览器，获取验证码'
print "http://douban.fm/misc/captcha?size=m&id=%s" % captcha_id   
captcha_solution=raw_input('输入验证码:')
post_data = {"source":"radio",'alias': alias, 'form_password':form_password,'captcha_solution':captcha_solution,"captcha_id":captcha_id}

lg = opener.open(url_login, urllib.urlencode(post_data)).read()

if lg.find('user_info') < 0:
    print u'登录失败:'
    print lg
    sys.exit(0)

url_fav_song = 'http://douban.fm/mine?type=liked&start='
url_song_info = 'http://38bef685.dotcloud.com/song/'
url_play_list = 'http://douban.fm/j/mine/playlist?type=n&h=&channel=0&from=mainsite&r=4941e23d79'

start = 0
reg_sid = re.compile('sid="(\d+)"')
fail_retry = 2
fail_downloads = []
success_downloads = []

def down_load_songs(_start, sids=None):
    global fail_downloads, fail_retry, start

    if not sids:
        fav_page = opener.open(url_fav_song + str(_start)).read()
        sids = reg_sid.findall(fav_page)

    for sid in sids:
        print '---===---'
        print 'down load song sid =', sid

        try:
            down_load_song(sid)
        except Exception,e:
            fail_downloads.append(sid)
            print 'down load error:', e

        print '\r\n-- END --'
        print ''

    if _start is not None and len(sids) > 14:
        start += len(sids)
        return down_load_songs(start)
    elif fail_retry > 0 and len(fail_downloads) > 0:
        print '--== retry ==--'
        temp = fail_downloads
        fail_downloads = []
        fail_retry -= 1
        return down_load_songs(None, temp)

def down_load_song(sid):
    global fail_downloads, fail_retry, success_downloads, start

    song = opener.open(url_song_info + str(sid)).read()
    try:
        song = json.loads(song)
    except:
        song = None
    if not song:
        print u'load song error, song id is:', song
        fail_downloads.append(sid)
        return

    if not song.has_key('sid') or not song.has_key('ssid'):
        fail_downloads.append(sid)
        print 'song has no "sid" or "ssid" : ', song
        return

    print 'down load : ', song['title']

    start_cookie = '%sg%sg0' % (song['sid'], song['ssid'])
    ck = ck = cookielib.Cookie(version=0, name='start', value=start_cookie, port=None, port_specified=False, domain='.douban.fm', domain_specified=False, domain_initial_dot=False, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
    cj.set_cookie(ck)
    pl = opener.open(url_play_list).read()
    try:
        pl = json.loads(pl)
    except:
        print 'load play list error:', pl
        fail_downloads.append(sid)
        return

    if pl['song'][0]['sid'] != str(sid):
        print 'load song info ERROR: NOT THE SAME SID'
        fail_downloads.append(sid)
        return

    url = pl['song'][0]['url']

    print '==>> wget: ==>> ', url

    cmd = 'wget -O "%s.mp3" %s' % (song['title'], url)
    os.system(cmd.encode('utf8'))

    success_downloads.append(sid)

down_load_songs(0)


print 'down load success:', len(success_downloads)
print 'down load fail:', len(fail_downloads)
print 'ALL DONE'
print u'支持音乐事业，请购买正版！'
print u'=>> 支持软件事业，也请购买正版软件！ <<=='


