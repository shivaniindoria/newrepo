import requests
from bs4 import BeautifulSoup
from plyer import notification

def get_top_headlines():
    url = 'https://indianexpress.com/section/technology/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        headlines = soup.find_all('alt', class_='heading')

        top_headlines = [headline.text.strip() for headline in headlines]

        return top_headlines
    else:
        print("Failed to fetch headlines")
        return None

def notify_top_headlines(headlines):
    if headlines:
        headlines_str = '\n'.join(headlines)

        notification.notify(
            title='Top News Headlines',
            message=headlines_str,
            app_name='News Notifier',
            timeout=8
        )
    else:
        print("No headlines to notify")

if __name__ == "__main__":
    headlines = get_top_headlines()

    notify_top_headlines(headlines)
