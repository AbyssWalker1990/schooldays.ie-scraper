from school_util import CitiesScraper

"""Starting url that contains all needed links to crawl"""
url = "https://www.schooldays.ie/articles/primary-Schools-in-Ireland-by-County"

"""Selectors needed to extract all cities links"""
cities_selectors = ['sdschoollist', 'panelMun', 'panelCon', 'panelUls']

def main():
    """Get ALL cities links, and preparing it for scraping"""
    scraper = CitiesScraper(url, cities_selectors)
    scraper.reset_log()
    cities_list_dirty = scraper.get_cities_links()
    cities_list = scraper.fix_links(cities_list_dirty)

    """ Start scrape all the data
        extract_school_links is getting list of school links in city and give it further to CityScraper class
        extract_data obtain list of schools and start scraping using methods of DataExtractor class
        For every school creating School object(dataclass)
        Data writing to csv file using dataclass_csv library
        Scraped links also writing to a log file, that can be used for resume scraping if something went wrong
        and program raised Error """

    scraper.extract_school_links(cities_list)


if __name__ == "__main__":
    main()


