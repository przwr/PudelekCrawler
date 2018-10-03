# -*- coding: utf-8 -*-
import scrapy


class PudelekSpider(scrapy.Spider):
	name = "pudelek_spider"
	start_urls = [
		'http://www.pudelek.pl/artykul/136402/kierowca_bmw_zada_od_anny_muchy_50_tysiecy_zlotych_zapamietaj_ten_numer_konta_bo_na_niego_wplacisz_50_000_pln_po_przegranej_sprawie',
	]

	def parse(self, response):
		for quote in response.css("div.comment.comment-odd > div.comment-body > div.comment-text"):
			yield {
				'text': quote.css('div::text').extract_first().strip(),
			}

		for quote in response.css("div.comment.comment-even > div.comment-body > div.comment-text"):
			yield {
				'text': quote.css('div::text').extract_first().strip(),
			}

		next_page_url = response.css("div.comments-paging > a.next::attr(href)").extract_first()
		if next_page_url is not None:
			yield scrapy.Request(response.urljoin(next_page_url))
