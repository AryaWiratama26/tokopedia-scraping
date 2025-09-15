from automation import TokopediaScraping

bot_scraping = TokopediaScraping()
bot_scraping.search(keyword="pensil")
bot_scraping.get_price(data_len=20)