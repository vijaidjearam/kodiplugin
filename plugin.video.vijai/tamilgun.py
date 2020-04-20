import urllib2, urllib, xbmcgui, xbmcplugin,xbmcaddon, xbmc, re, sys, os, requests
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
from unpack import unpack
from vijaicontent import getdatacontent,gethtmlcontent
from vijaidirectory import addDir
import resolveurl
from getImgPath import getImgPath
from playurl import playurl

def tamilgun(url):
    args = sys.argv[2]
    if str(sys.argv[2]).find('url=') > 1:
        args = sys.argv[2]
        mode = args.split('url=')
        xbmc.log(str(mode))
        mode = mode[1]
        mode = mode.split('&')
        url = mode[0]
        url = urllib.unquote_plus(url)
    xbmc.log("tamilgun url 2--------------------------------------------------------------------------------")
    xbmc.log(url)
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    req = urllib2.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read()
    # headers = {
    # 'Connection': 'keep-alive',
    # 'Upgrade-Insecure-Requests': '1',
    # 'DNT': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Referer': 'http://tamilgun.de/tamil/',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
    #     }

    # response = requests.get('http://tamilgun.de/tamil/categories/new-movies-a', headers=headers, verify=False)
    # html = response.content
    reg = "<img src=\" (.*?) \" alt=\"(.*?)\" \/>\s+<div class=\"rocky-effect\">\s+<a href=\"(.*?)\" >"
    #data = getdatacontent(url,reg)
    navRegex = '<a class="next page-numbers" href="(.*?)">'
    data = re.compile(reg).findall(html)
    nav = re.compile( navRegex ).findall( html )
    for item in data:
        addDir('folder','loadgunmovie',item[2],item[1],item[0],item[0])
        
    if nav:
        #tamilgun(nav[0])
        addDir( 'folder','tamilgun_HD_movie',nav[0],'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png" )
        # url = nav[0]
        # return url
        # base_url = sys.argv[0]
        # base_url +="?url=" +urllib.quote_plus(nav[0])
        # base_url += "&mode=" +str(mode)
        # base_url +="&name=" +urllib.quote_plus('Tamilgun')
        # base_url +="&icoimage=" +urllib.quote_plus("https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png")
        # base_url +="&fanart=" +urllib.quote_plus("https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png")
        # li = xbmcgui.ListItem('[B]Next Page...[/B]',iconImage="https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png")
        # li.setInfo(type="Video",infoLabels={"Title": '[B]Next Page...[/B]'})
        # li.setProperty("Fanart_Image", "https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png")
        # xbmcplugin.addDirectoryItem(handle=addon_handle,url=base_url,listitem=li,isFolder=True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

def tamildbox(url):
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        req = urllib2.Request(url)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        r = opener.open(req)
        html = r.read()
        reg = 'onclick=\"return loadEP\((\d+),(\d+)\);'
        data = re.compile(reg).findall(html)
        xbmc.log(str(data))
        if len(data) >=2:
            datatemp = data[1]
            ep_id= datatemp[0]
            server_id=datatemp[1]
            urlextract = url.split('/')
            url = "http://"+urlextract[2]+"/actions.php?case=loadEP&ep_id="+ep_id+"&server_id="+server_id
            proxy_handler = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxy_handler)
            req = urllib2.Request(url)
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')]
            r = opener.open(req)
            htmltemp = r.read()
            iframe = re.compile('(?:iframe src|IFRAME SRC)="(.+?)"').findall(htmltemp)
            if iframe:
                for url in iframe:
                    xbmc.log(url)
                    if url.find('megamp4') > 1:
                        proxy_handler = urllib2.ProxyHandler({})
                        opener = urllib2.build_opener(proxy_handler)
                        req = urllib2.Request(url)
                        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                        r = opener.open(req)
                        api_html = r.read()
                        moviereg = 'file:"(.*?)"'
                        movieurl = re.compile(moviereg).findall(api_html)
                        movieurl = movieurl[0]
                        # api_html = net.http_GET(url).content
                        # moviereg = 'file:"(.*?)"'
                        # movieurl = re.compile(moviereg).findall(api_html)[0]
                        if movieurl:
                            addDir('','',movieurl,"Tamildbox - megamp4 link","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
                    if url.find('ssfile') > 1:
                        proxy_handler = urllib2.ProxyHandler({})
                        opener = urllib2.build_opener(proxy_handler)
                        req = urllib2.Request(url)
                        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                        r = opener.open(req)
                        api_html = r.read()
                        moviereg = 'sources: \[(\".*?\")\]'
                        movieurl = re.compile(moviereg).findall(api_html)
                        # xbmc.log(str(movieurl))
                        # xbmc.log(str(type(movieurl)))
                        if movieurl:
                            temp = movieurl[0]
                            temp = temp.split(",")
                            temp = temp[1]
                            temp = temp.replace("\"","")
                            xbmc.log(str(temp))                
                            if temp:
                                xbmc.log("+++++++++++++++++++++++++++++++++++++++          vijai  ssfiles test ++++++++++++++++++++++++++++++++++++++++++++++++")
                                addDir('','',temp,"ssfile","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png") 
        if data[0]:    
            datatemp = data[0]
            ep_id= datatemp[0]
            server_id=datatemp[1]
            urlextract = url.split('/')
            url = "http://"+urlextract[2]+"/actions.php?case=loadEP&ep_id="+ep_id+"&server_id="+server_id
            proxy_handler = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxy_handler)
            req = urllib2.Request(url)
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')]
            r = opener.open(req)
            htmltemp = r.read()
            iframe = re.compile('(?:iframe src|IFRAME SRC)="(.+?)"').findall(htmltemp)
            if iframe:
                for url in iframe:
                    xbmc.log(url)
                    if url.find('megamp4') > 1:
                        proxy_handler = urllib2.ProxyHandler({})
                        opener = urllib2.build_opener(proxy_handler)
                        req = urllib2.Request(url)
                        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                        r = opener.open(req)
                        api_html = r.read()
                        moviereg = 'file:"(.*?)"'
                        movieurl = re.compile(moviereg).findall(api_html)
                        movieurl = movieurl[0]
                        # api_html = net.http_GET(url).content
                        # moviereg = 'file:"(.*?)"'
                        # movieurl = re.compile(moviereg).findall(api_html)[0]
                        if movieurl:
                            addDir('','',movieurl,"Tamildbox - megamp4 link","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
                    if url.find('ssfile') > 1:
                        proxy_handler = urllib2.ProxyHandler({})
                        opener = urllib2.build_opener(proxy_handler)
                        req = urllib2.Request(url)
                        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                        r = opener.open(req)
                        api_html = r.read()
                        moviereg = 'sources: \[(\".*?\")\]'
                        movieurl = re.compile(moviereg).findall(api_html)
                        # xbmc.log(str(movieurl))
                        # xbmc.log(str(type(movieurl)))
                        if movieurl:
                            temp = movieurl[0]
                            temp = temp.split(",")
                            temp = temp[1]
                            temp = temp.replace("\"","")
                            xbmc.log(str(temp))                
                            if temp:
                                xbmc.log("+++++++++++++++++++++++++++++++++++++++          vijai  ssfiles test ++++++++++++++++++++++++++++++++++++++++++++++++")
                                addDir('','',temp,"ssfile","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
def loadgunmovie():
    import ssl 
    try:
        _create_unverified_https_context = ssl._create_unverified_context 

    except AttributeError: 
        pass 
    else: 
        ssl._create_default_https_context =_create_unverified_https_context
    args = sys.argv[2]
    mode = args.split('url=')
    mode = mode[1]
    mode = mode.split('&')
    url = mode[0]
    url = urllib.unquote_plus(url)
    #url = sys.argv[2]
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    req = urllib2.Request(url)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    r = opener.open(req)
    html = r.read()
    regex = 'src="\/\/embed1\.(.*)\/hls_stream\/(.*?)\"'
    tempurl = re.compile(regex).findall(html)
    if tempurl:
        tempurl = tempurl[0]
        #tamilgunurl = "http://embed1."+tempurl[0]+"/hls/"+tempurl[1]+"/playlist.m3u8"
        tamilgunurl = "http://embed1."+"tamilgun.tv"+"/hls/"+tempurl[1]+"/playlist.m3u8"
        xbmc.log("---------------------------------------------------------------------tamilgunurl-----------------------------------------------")
        xbmc.log(tamilgunurl)
        addDir('','',tamilgunurl,"tamilgunurl","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
    #---------------------------------------------------------
    #----------------------------------------Tamildbox Link------------------------------------------------------------------- 
    regex = "<div class=\"essb_postbar_start\"><\/div>\s*<p>(.*?)<br \/>\s*<a href=\"(.*?)\" target=\"_blank\""
    tamilboxurl = re.compile(regex).findall(html)
    if tamilboxurl:
        tamilboxurl = tamilboxurl[0]
        tamilboxurl = tamilboxurl[-1]
        xbmc.log("+++++++++++++++++++++++++++++++++++++++          tamildbox++++++++++++++++++++++++++++++++++++++++++++++++")
        xbmc.log(str(tamilboxurl))

        if "watch" in tamilboxurl:
            try:
                tamildbox(tamilboxurl)
                xbmc.log("+++++++++++++++++++++++++++++++++++++++          tamildbox -- Ends++++++++++++++++++++++++++++++++++++++++++++++++")
            except Exception as e:
                pass

  

    #---------------------------------scraping other links -------------------------------------------------------------------------------------------------------
    iframe= re.compile('<(iframe|IFRAME) (.*?) (src|SRC)=\"(.*?)\"').findall(html)
    #iframe = iframe[0]
    xbmc.log("+++++++++++++++++++++++++++++++++++++++          vidoza++++++++++++++++++++++++++++++++++++++++++++++++")
    xbmc.log(str(iframe))
    if iframe:
        for item in iframe:
            if item:
                for url in item:
                    if "vidoza" in url:
                        addDir('folder','playurl',url,"vidoza","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
                    if "rapidvideo" in url:
                        addDir('folder','playurl',url,"rapidvideo","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
                    if 'ssfiles' in url:
            
                        proxy_handler = urllib2.ProxyHandler({})
                        opener = urllib2.build_opener(proxy_handler)
                        req = urllib2.Request(url)
                        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                        r = opener.open(req)
                        api_html = r.read()
                        moviereg = 'sources: \[(\".*?\")\]'
                        movieurl = re.compile(moviereg).findall(api_html)
                        # xbmc.log(str(movieurl))
                        # xbmc.log(str(type(movieurl)))
                        temp = movieurl[0]
                        temp = temp.split(",")
                        temp = temp[1]
                        temp = temp.replace("\"","")
                        xbmc.log(str(temp))                
                        if temp:
                            xbmc.log("+++++++++++++++++++++++++++++++++++++++          vijai  ssfiles test ++++++++++++++++++++++++++++++++++++++++++++++++")
                            addDir('','',temp,"ssfile","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
    regex ="Loading...<\/div><script>[\s\S]*?>[\s\S]*?<\/script>"
    data = re.compile(regex).findall(html)
    if data:
        st = data[0]
        stsplit= st.split('<script>', 1 )
        stsplit = stsplit[1]
        stsplit= stsplit.split('\n</script>', 1 )
        res = stsplit[0]
        # out= unpack(res)
        # xbmc.log(out)
        if "360p" in res:
            moviereg = '"file":"(.*?)"'
            movieurl = re.compile(moviereg).findall(res)[0]
            movieurl = movieurl.replace ("\\" ,"")
            movieurl = movieurl + "&stream=1"

            headers = {'Range':'bytes=0-','Referer': url,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 'Host': url.split('/')[2], 'Accept-Encoding': 'identity;q=1, *;q=0', }
            r = requests.get(movieurl, headers=headers, allow_redirects=False)
            movieurl=  r.headers.get('location')
           
            if movieurl:
                addDir('','',movieurl,"Link - 360p","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
            #xbmcplugin.endOfDirectory(int(sys.argv[1]))
        if "720p" in res:
            moviereg = '"file":"(.*?)"'
            movieurl = re.compile(moviereg).findall(res)[1]
            movieurl = movieurl.replace ("\\" ,"")
            movieurl = movieurl + "&stream=1"

            headers = {'Range':'bytes=0-','Referer': url,'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36', 'Host': url.split('/')[2], 'Accept-Encoding': 'identity;q=1, *;q=0', }
            r = requests.get(movieurl, headers=headers, allow_redirects=False)
            movieurl=  r.headers.get('location')
            xbmc.log(str(r.headers))
            if movieurl:
                addDir('','',movieurl,"Link - 720p","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
    iframe = re.compile('(?:iframe src|IFRAME SRC)="(.+?)"').findall(html)
    if iframe:
        for url in iframe:
            if "megamp4" in url:
                addDir('folder','playurl',url,"megamp4 link","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
                #xbmcplugin.endOfDirectory(int(sys.argv[1]))
            #tentkotta megamp4 link extraction
            if 'cdn20.megamp4.net' in url:                    
                url =url.split("=")
                url=url[0].split("?")
                prefix = "http://megamp4.net/embed-"
                url = prefix+url[1]+".html"
                proxy_handler = urllib2.ProxyHandler({})
                opener = urllib2.build_opener(proxy_handler)
                req = urllib2.Request(url)
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                r = opener.open(req)
                api_html = r.read()
                moviereg = 'file:"(.*?)"'
                movieurl = re.compile(moviereg).findall(api_html)
                movieurl= movieurl[0]                
                xbmc.log(movieurl)
                if movieurl:
                    xbmc.log(movieurl)
                    addDir('','',movieurl,"megamp4 link","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
            
            if 'ssfiles' in url:
            
                        proxy_handler = urllib2.ProxyHandler({})
                        opener = urllib2.build_opener(proxy_handler)
                        req = urllib2.Request(url)
                        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                        r = opener.open(req)
                        api_html = r.read()
                        moviereg = 'sources: \[(\".*?\")\]'
                        movieurl = re.compile(moviereg).findall(api_html)
                        # xbmc.log(str(movieurl))
                        # xbmc.log(str(type(movieurl)))
                        if movieurl:
                            temp = movieurl[0]
                            temp = temp.split(",")
                            temp = temp[1]
                            temp = temp.replace("\"","")
                            xbmc.log(str(temp))                
                            if temp:
                                xbmc.log("+++++++++++++++++++++++++++++++++++++++          vijai  ssfiles test ++++++++++++++++++++++++++++++++++++++++++++++++")
                                addDir('','',temp,"ssfile","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
    regex = "document\.write\(unescape\(\'(.*?)\'\)\)"
    data = re.compile(regex).findall(html)
    if data:
        data = urllib2.unquote(data[0])
        iframe= re.compile("<(iframe|IFRAME) (.*?) (src|SRC)=\"(.*?)\"").findall(data)
        if iframe:
            for item in iframe[0]:
                if "rapidvideo" in item:
                    addDir('folder','playurl',item,"rapidvideo",getImgPath("openload_icon"),getImgPath("openload_fanart"))
                if "ssfile" in item:
                    addDir('folder','playurl',item,"ssfile",getImgPath("openload_icon"),getImgPath("openload_fanart"))
#----------------------------------------second link detection-------------------------------------------------------------------    
    # reg = "<a href=\"(.*?)\" target=\"_blank\" rel=\"noopener\"><img src="
    # data = re.compile(reg).findall(html)
    # xbmc.log("+++++++++++++++++++++++++++++++++++++++          vijai tamildbox test ++++++++++++++++++++++++++++++++++++++++++++++++")
    # xbmc.log(str(data))
    # if data:
    #     url = data[0]
    #     proxy_handler = urllib2.ProxyHandler({})
    #     opener = urllib2.build_opener(proxy_handler)
    #     xbmc.log("+++++++++++++++++++++++++++++++++++++++          vijai test ++++++++++++++++++++++++++++++++++++++++++++++++")
    #     xbmc.log(url)
    #     req = urllib2.Request(url)
    #     opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #     r = opener.open(req)
    #     html = r.read()
    #     reg = "\$\(\"#player_button\"\)\.click\(function\(\){\s*return loadEP((.*?));"
    #     data = re.compile(reg).findall(html)
    #     data = data[0]
    #     data = data[0]
    #     ep_id= data[2:5]
    #     server_id=data[7:11]
    #     url = "http://tamildbox.com/actions.php?case=loadEP&ep_id="+ep_id+"&server_id="+server_id
    #     proxy_handler = urllib2.ProxyHandler({})
    #     opener = urllib2.build_opener(proxy_handler)
    #     req = urllib2.Request(url)
    #     opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #     r = opener.open(req)
    #     html = r.read()
    #     iframe = re.compile('(?:iframe src|IFRAME SRC)="(.+?)"').findall(html)
    #     if iframe:
    #         for url in iframe:
    #             xbmc.log(url)
    #             if url.find('megamp4') > 1:
    #                 proxy_handler = urllib2.ProxyHandler({})
    #                 opener = urllib2.build_opener(proxy_handler)
    #                 req = urllib2.Request(url)
    #                 opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    #                 r = opener.open(req)
    #                 api_html = r.read()
    #                 moviereg = 'file:"(.*?)"'
    #                 movieurl = re.compile(moviereg).findall(api_html)
    #                 movieurl = movieurl[0]
    #                 # api_html = net.http_GET(url).content
    #                 # moviereg = 'file:"(.*?)"'
    #                 # movieurl = re.compile(moviereg).findall(api_html)[0]
    #                 if movieurl:
    #                     # xbmc.log("+++++++++++++++++++++++++++++++++++++++          vijai test 12321 ++++++++++++++++++++++++++++++++++++++++++++++++")
    #                     xbmc.log(movieurl)
    #                     addDir('','',movieurl,"Tamildbox megamp4 link","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
    #-----------------------------------detect cdn link
    iframe= re.compile("src=\"(.*?)\"").findall(html)
    if iframe:
        for url in iframe:
            if "cdnplay" in url:
                proxy_handler = urllib2.ProxyHandler({})
                opener = urllib2.build_opener(proxy_handler)
                req = urllib2.Request(url)
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                r = opener.open(req)
                html1 = r.read()
                movieurl= re.compile("'file':'(.*?)'").findall(html1)
                if movieurl:
                    for tempurl in movieurl:
                        addDir('','',tempurl,"Cdn-link","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")

    iframe= re.compile("<a onclick=\"window.open\('(.*?)'").findall(html)
    if iframe:
        for url in iframe:
            if "embed1.tamildbox" in url:
                xbmc.log("---------------------------------------embed1-tamildbox-----------------------------------------------------------")
                xbmc.log(url)
                if "https" in url:
                    url = url 
                elif "http" in url:
                    url = url.replace("http","https")
                else:
                    url = 'https:'+url
                xbmc.log(url)
                proxy_handler = urllib2.ProxyHandler({})
                opener = urllib2.build_opener(proxy_handler)
                req = urllib2.Request(url)
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                r = opener.open(req)
                html1 = r.read()
                movieurl= re.compile("domainStream = '(.*?)'").findall(html1)
                xbmc.log("---------------------------------------embed1-tamildbox - movie-url-----------------------------------------------------------")
                xbmc.log(str(movieurl))
                if movieurl:
                    for tempurl in movieurl:
                        xbmc.log("---------------------------------------embed1-tamildbox - temp-url-----------------------------------------------------------")
                        xbmc.log(tempurl)
                        addDir('','',tempurl,"TamilGun-embeded-URL","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
                elif "domainStream = domainStream.replace('.tamildbox.tips', '.tamilgun.tv')" in html1:
                    url = url.replace('hls_vast', 'hls')
                    url = url.replace('.tamildbox.tips', '.tamilgun.tv')
                    url = url + '/playlist.m3u8'
                    xbmc.log(url)
                    addDir('','',url,"TamilGun-embeded-URL","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
                movieurl = re.compile('<iframe id=\"player\" src=\"(.*?)\"><\/iframe>').findall(html1)
                xbmc.log("---------------------------------------embed1-tamildbox - movie-url-----------------------------------------------------------")
                xbmc.log(str(movieurl))
                headers = {
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'DNT': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Mode': 'nested-navigate',
                    'Referer': url,
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
                }
                for url in movieurl:
                    if url:
                        print url
                        response = requests.get(url, headers=headers)
                        temp = response.content
                        movieurl = re.compile('sources:\s+\[\"(.*?)\",\"(.*?)\"\]').findall(temp)
                        movieurl = movieurl[0]
                        print movieurl[0]
                        if movieurl[0]:
                            headers = {
                                'Connection': 'keep-alive',
                                'Origin': 'https://chromecast.video',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
                                'DNT': '1',
                                'Accept': '*/*',
                                'Sec-Fetch-Site': 'same-site',
                                'Sec-Fetch-Mode': 'cors',
                                'Referer': url,
                                'Accept-Encoding': 'gzip, deflate, br',
                                'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
                            }
                            response = requests.get(movieurl[0], headers=headers)
                            temp = response.content
                            movieurl = re.compile('https:\/\/(.*?)index-v1-a1.m3u8').findall(temp)
                            xbmc.log(str(movieurl))
                            if movieurl[-1]:

                                movieurl = 'https://'+movieurl[-1]+'index-v1-a1.m3u8'
                                xbmc.log(movieurl)
                                addDir('','',movieurl,"TamilGun-embeded-URL","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")
        iframe= re.compile('<IFRAME SRC=\"(.*?)\"').findall(html)
        print iframe
        if iframe:
            for url in iframe:
                if "chromecast.video" in url:
                    if "https" in url:
                        url = url 
                    elif "http" in url:
                        url = url.replace("http","https")
                    else:
                        url = 'https:'+url
                    
                    headers = {
                        'Connection': 'keep-alive',
                        'DNT': '1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
                        'Sec-Fetch-User': '?1',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-Mode': 'navigate',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
                    }

                    response = requests.get(url, headers=headers)
                    html1 = response.content
                    movieurl = re.compile('sources:\s+\[\"(.*?)\",\"(.*?)\"\]').findall(html1)
                    movieurl = movieurl[0]
                    
                    if movieurl[0]:
                        headers = {
                            'Connection': 'keep-alive',
                            'Origin': 'https://chromecast.video',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
                            'DNT': '1',
                            'Accept': '*/*',
                            'Sec-Fetch-Site': 'same-site',
                            'Sec-Fetch-Mode': 'cors',
                            'Referer': url,
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9,ta-IN;q=0.8,ta;q=0.7,fr-FR;q=0.6,fr;q=0.5',
                        }
                        response = requests.get(movieurl[0], headers=headers)
                        temp = response.content
                        movieurl = re.compile('https:\/\/(.*?)index-v1-a1.m3u8').findall(temp)
                        if movieurl[-1]:
                            movieurl = 'https://'+movieurl[-1]+'index-v1-a1.m3u8'
                          
                            addDir('','',movieurl,"TamilGun-embeded-URL","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png","http://1.bp.blogspot.com/-MRgrvLyXh_M/WRREmIJa_AI/AAAAAAAABrs/zbzu9W5rwKo5RK6Xk8G-E_aXCgkz7rknACK4B/s400/TamilGun.png")


   #-----------------------------------End of detect cdn link   
    xbmcplugin.endOfDirectory(int(sys.argv[1]))