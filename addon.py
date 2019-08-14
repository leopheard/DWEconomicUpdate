from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL0 = "https://economicupdate.libsyn.com/rss"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/8/1/3/b/813b34b6d72b702a/EU_FBprofpic-01.png"},
   {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('latest_episodes'),
            'thumbnail': "https://ssl-static.libsyn.com/p/assets/8/1/3/b/813b34b6d72b702a/EU_FBprofpic-01.png"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL0)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/latest_episodes/')
def latest_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL0)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
