import urllib2, urllib, xbmcplugin,sys,re, xbmcgui,xbmcaddon,xbmc,os
from t0mm0.common.net import Net
from t0mm0.common.addon import Addon
addon_handle= int(sys.argv[1])
tamilgun_icon = "http://cdn.appstorm.net/mac.appstorm.net/files/2012/07/icon4.png"
net = Net()
addonId        = 'plugin.video.vijai'
addon_settings = xbmcaddon.Addon(id = addonId);
addon          = Addon( addonId, sys.argv )
addonPath      = xbmc.translatePath( addon.get_path() )
resPath        = os.path.join( addonPath, 'resources' )
iconPath       = os.path.join( resPath, 'images' )

class site:
    def __init__(self,url=None,redirection_name=None,get_site_content_regex=None,get_nav_data_regex=None,get_stream_url_regex=None):
        self.url = url
        self.redirection_name = redirection_name #this variable is used in nav redirection 
        self.get_site_content_regex = get_site_content_regex
        self.get_nav_data_regex = get_nav_data_regex
        self.get_stream_url_regex = get_stream_url_regex

    @staticmethod
    def addDir (dir_type,mode,url,name,iconimage,fanart):
        base_url = sys.argv[0]
        base_url +="?url=" +urllib.quote_plus(url)
        base_url += "&mode=" +str(mode)
        #base_url +="&name=" +urllib.quote_plus(name)
        base_url +="&name=" + name
        base_url +="&icoimage=" +urllib.quote_plus(iconimage)
        base_url +="&fanart=" +urllib.quote_plus(fanart)
        li = xbmcgui.ListItem(name,iconImage=iconimage)
        li.setInfo(type="Video",infoLabels={"Title": name})
        li.setProperty("Fanart_Image", fanart)
        if dir_type != '':
            link = xbmcplugin.addDirectoryItem(handle=addon_handle,url=base_url,listitem=li,isFolder=True)
        else:
            link = xbmcplugin.addDirectoryItem(handle=addon_handle,url=url,listitem=li,isFolder=False)
        return link
    
    @staticmethod
    def getdatacontent(url,reg):
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        req = urllib2.Request(url)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        r = opener.open(req)
        html = r.read()
        r = re.compile(reg)
        data = [m.groupdict() for m in r.finditer(html)]
        return data
    @staticmethod
    def getnavcontent(url,reg):
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        req = urllib2.Request(url)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        r = opener.open(req)
        html = r.read()
        data = re.compile(reg).findall(html)
        return data
        
    @staticmethod
    def gethtmlcontent(url):
        proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(proxy_handler)
        req = urllib2.Request(url)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        r = opener.open(req)
        html = r.read()
        return html
    
    @staticmethod
    def getImgPath( icon ):
        icon = icon + '.png'
        imgPath = os.path.join( iconPath, icon )
       # print imgPath
        if os.path.exists( imgPath ):
            return imgPath
        else:
            return ''

    def loadsitecontent(self,url):
        args = sys.argv[2]
        if str(sys.argv[2]).find('url=') > 1:
            args = sys.argv[2]
            mode = args.split('url=')
            xbmc.log(str(mode))
            mode = mode[1]
            mode = mode.split('&')
            url = mode[0]
            url = urllib.unquote_plus(url)
        data = self.getdatacontent(url,self.get_site_content_regex)
        nav = self.getnavcontent(url,self.get_nav_data_regex)
        nav =  nav[0]
        for item in data:
            self.addDir('folder','liststreamurl',item['pageurl'],item['title'],item['poster'],item['poster'])
        if nav:

            self.addDir( 'folder',self.redirection_name,nav[0],'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png" )
            #self.addDir( 'folder',self.name,nav[0],'[B]Next Page...[/B]',"https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png","https://lh3.googleusercontent.com/-NsVeHCUW0lo/V4b8r67FVSI/AAAAAAAAD7U/G1ifDqs0nFENPck0-oKCQgc3-Gdm_JM7QCCo/s574/next_574x358.png" )
        #xbmcplugin.endOfDirectory(int(sys.argv[1]))

    def liststreamurl(self):
        args = sys.argv[2]
        mode = args.split('url=')
        mode = mode[1]
        mode = mode.split('&')
        url = mode[0]
        url = urllib.unquote_plus(url)
        data= self.getdatacontent(url,self.get_stream_url_regex)
        for item in data:
            streamurl = item['streamurl']
            streamtitle = streamurl.split('/')
            streamtitle = streamtitle[2]
            self.addDir('folder','playurl',streamurl,streamtitle,self.getImgPath("openload_icon"),self.getImgPath("openload_fanart"))
        xbmcplugin.endOfDirectory(int(sys.argv[1]))