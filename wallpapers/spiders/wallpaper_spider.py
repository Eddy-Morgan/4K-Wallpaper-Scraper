import scrapy

from ..items import WallpapersItem

#some urls
# http://images.hdqwalls.com/mr-robot-wallpapers/page/6

def url_generator():
    urls = []
    for i in range(2288):
        url = 'https://hdqwalls.com/latest-wallpapers/page/%s' % i
        urls.append(url)
    return urls


class WallpaperSpider(scrapy.Spider):
    name = "wallpaper"
    start_urls = url_generator()
    item = WallpapersItem()
    img_urls = []

    def parse(self, response):
        for wallpaper in response.css('div.wallpapers_container div.wall-resp'):
            img= wallpaper.css('img::attr(src)').get()
            segments = img.split('/')
            segments[3] = 'download'
            segments[4] = '1'
            img_url = '/'.join(segments)
            self.img_urls.append(img_url)
#        next_page = response.css('li.next a::attr(href)').get()
#        if next_page is not None:
#            yield response.follow(next_page, callback=self.parse)
        self.item['image_urls'] = self.img_urls
        return self.item