import requests
from bs4 import BeautifulSoup
import ssl
import warnings
from openpyxl import Workbook
import csv as csv
import requests.packages.urllib3.exceptions as urllib3_exceptions
warnings.simplefilter("ignore", urllib3_exceptions.InsecureRequestWarning)

def extract_url(sourceurl, category):

    records = []

    # Work around for SSL Error 
    class TLSAdapter(requests.adapters.HTTPAdapter):
        def init_poolmanager(self, *args, **kwargs):
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.set_ciphers("DEFAULT@SECLEVEL=1")
            ctx.options |= 0x4
            kwargs["ssl_context"] = ctx
            return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

    with requests.session() as s:
        s.mount("https://", TLSAdapter())

        response = s.get(sourceurl)
        soup = BeautifulSoup(response.text, 'html.parser')

        urls = []
               
        
                       
        for link in soup.table.find_all('a'):
            url = ''
            record = {}
            
            # check scraped url and process it accordingly
            if link.get('href')[0] == '/' :
                url = "https://policy.un.org" + link.get('href')
            else:
                if link.get('href').find("https://www.undocs.org/en/") > -1 :
                    url = link.get('href')
                elif link.get('href').find("https://www.undocs.org/") > -1 :
                    url = link.get('href').replace("https://www.undocs.org/", "https://www.undocs.org/en/")
                else:
                    url = link.get('href')

            record["url"] = url
            record["category"] = category

            records.append(record)

        # Write urls and category to csv
        with open(f"scrapefull.csv", 'a') as f:
            writer=csv.writer(f, delimiter=',', dialect='unix')
            for row in records:
                writer.writerow([row["url"], row["category"]])

        records = []
            

if __name__ == "__main__":
    
    # Urls from website and labeled category
    sourceurls = ["https://policy.un.org/policy-all?f%5B0%5D=node%253Afield_document_topic_theme%253Aparents_all%3A30425", 
                  "https://policy.un.org/policy-all?f%5B0%5D=node%253Afield_document_topic_theme%253Aparents_all%3A30425&page=1",
                  "https://policy.un.org/policy-all?f%5B0%5D=node%253Afield_document_topic_theme%253Aparents_all%3A29785",
                  "https://policy.un.org/policy-all?f%5B0%5D=node%253Afield_document_topic_theme%253Aparents_all%3A29785&page=1",
                  "https://policy.un.org/policy-all?f%5B0%5D=node%253Afield_document_topic_theme%253Aparents_all%3A29060",
                  "https://policy.un.org/policy-all?f%5B0%5D=node%253Afield_document_topic_theme%253Aparents_all%3A29060&page=1",
                  "https://policy.un.org/policy-all?f%5B0%5D=node%253Afield_document_topic_theme%253Aparents_all%3A29665",
                  "https://policy.un.org/policy-all?f%5B0%5D=node%253Afield_document_topic_theme%253Aparents_all%3A29665&page=1"]
    sourcecategories = ["accountability", 
                        "accountability",
                        "health and wellbeing",
                        "health and wellbeing",
                        "human resources",
                        "human resources",
                        "travel",
                        "travel"]

    with open(f"scrapefull.csv", 'w') as f:
        writer=csv.writer(f, delimiter=',', dialect='unix')
        writer.writerow(["url", "category"])
    f.close()

    for sourceurl, sourcecategory in zip(sourceurls, sourcecategories):
        print(f"processing {sourceurl} - {sourcecategory}")
        extract_url(sourceurl, sourcecategory)
    

