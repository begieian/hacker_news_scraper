from bs4 import BeautifulSoup
import requests
import pprint

URL = 'https://news.ycombinator.com/news?p='

for page in range(0,5):

    res = requests.get(URL + str(page))
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    # print(links[0].a['href'])

    def sort_titles_by_votes(hacker_news_list):
        return sorted(hacker_news_list, key=lambda k:k['votes'], reverse=True)


    def create_custom_hacker_news(links, subtext):
        hacker_news_list = []
        for index, item in enumerate(links):
            title = links[index].getText()
            href = links[index].a.get('href', None)
            # href = links[index].a.get('href')
            # print(href)
            vote = subtext[index].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points >= 100:
                    hacker_news_list.append({'title': title, 'link': href, 'votes': points})
        return sort_titles_by_votes(hacker_news_list)



if __name__ == '__main__':
    pprint.pprint(create_custom_hacker_news(links, subtext))