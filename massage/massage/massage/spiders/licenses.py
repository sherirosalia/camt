import scrapy
import json
import random


class LicensesSpider(scrapy.Spider):
    name = 'licenses'
    allowed_domains = ['ws.camtc.org']
    start_urls = ['https://ws.camtc.org/api/Individual/IndividualSearchPublic/123?FirstName=&LastName=&LicenseNumber=72000&CityofWork=']

    def start_requests(self):

        for x in range(1,85000):
            # randomized_num = random.randint(1,85000)
            url = f'https://ws.camtc.org/api/Individual/IndividualSearchPublic/123?FirstName=&LastName=&LicenseNumber={x}&CityofWork='
            yield scrapy.Request(url=url, callback=self.parse, meta={'id':x})

    def parse(self, response):
        response_data=json.loads(response.text)
        if not response_data["IndividualSearchResponse"]:
            yield {     "FirstName": "",
                        "MiddleName": "",
                        "LastName": "",
                        'CertificateNumber': response.meta['id'],
                        "CertificateType": "",
                        "Effective": "",
                        "Expires": "",
                        "CityfromIndividualAddress": None,
                        "IndividualId": '',
                        'Status': 'Deactivated',
                        
            
            }
        else:
            data_list=response_data['IndividualSearchResponse'][0]
            yield data_list


