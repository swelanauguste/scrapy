import scrapy


class AwesomeSpider(scrapy.Spider):
    name = "job-spider"

    def start_requests(self):
        # GET request
        yield scrapy.Request("https://www.govt.lc/jobs", meta={"playwright": True})

    async def parse(self, response):
        for job in response.css("li.rc-li"):
            yield {
                "job-title": job.css("span[data-bind='text: Title']::text").get().lower().replace('\u2013', ' - '),
                "published": job.css("span[data-bind='dateString: Date']::text").get(),
                "links": job.css("a.rc-title").attrib['href'],
                }
