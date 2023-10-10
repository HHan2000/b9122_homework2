from bs4 import BeautifulSoup
import urllib.request

def is_contain_crisis_part2(title_href):
    try:
        req = urllib.request.Request(title_href)
        webpage = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(webpage)
        
        if 'crisis' in soup.get_text():
            return True
        else:
            return False
            
    except:
        return False

def press_release_contain_plenary_crisis(number_of_press):
    page = 0
    url_of_press_contain_plenary_crisis = []
    while len(url_of_press_contain_plenary_crisis) < number_of_press:
        seed_url = f'https://www.europarl.europa.eu/news/en/press-room/page/{page}'
        req = urllib.request.Request(seed_url)
        webpage = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(webpage)
        
        for i in soup.find_all('article', {'class':"ep_gridcolumn ep-m_product ep-layout_linkmode"}):
            for j in i.find_all('span', {'class':"ep_name"}):
                if len([x for x in j if 'Plenary session' in x.get_text()]) > 0:
                    title_href = (i.find('div', {'class':'ep_title'}).find('a', href = True))['href']
                    if is_contain_crisis_part2(title_href):
                        url_of_press_contain_plenary_crisis.append(title_href)
        page += 1
        
    return url_of_press_contain_plenary_crisis

def extract_file_part2(url_of_press_contain_plenary_crisis):
    for i in range(len(url_of_press_contain_plenary_crisis)):
        req = urllib.request.Request(url_of_press_contain_plenary_crisis[i])
        webpage = urllib.request.urlopen(req).read()
        with open(f"2_{i+1}.txt", 'w', encoding="utf-8") as f:
            f.write(webpage.decode())

## find at least 10 files
url_of_press_contain_plenary_crisis = press_release_contain_plenary_crisis(10)
## extract files
extract_file_part2(url_of_press_contain_plenary_crisis)
