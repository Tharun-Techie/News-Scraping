import bs4 as bs
import urllib.request
import time

# Set up initial variables and URLs
initial_urls = []
page_counter = 1
base_url = 'https://www.businesswire.com/portal/site/home/template.PAGE/news/?javax.portlet.tpst=ccf123a93466ea4c882a06a9149550fd&javax.portlet.prp_ccf123a93466ea4c882a06a9149550fd_viewID=MY_PORTAL_VIEW&javax.portlet.prp_ccf123a93466ea4c882a06a9149550fd_ndmHsc=v2*A1515934800000*B1518565773469*DgroupByDate*G'
part_2 = '*N1000003&javax.portlet.begCacheTok=com.vignette.cachetoken&javax.portlet.endCacheTok=com.vignette.cachetoken'

# Main loop for continuous scraping
while True:
    # Fetch and parse the HTML content
    url = base_url + str(page_counter) + part_2
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        sauce = urllib.request.urlopen(req).read()
    except Exception as e:
        print("Error fetching URL:", e)
        time.sleep(5)  # Wait for 5 seconds before retrying
        continue

    soup = bs.BeautifulSoup(sauce, 'html.parser')

    # Extract URLs of news articles
    for a in soup.find_all('a', class_='bwTitleLink', limit=25):
        initial_urls.append('https://www.businesswire.com' + a['href'])

    # Check if flipping to the next page is needed
    if page_counter > 5:
        print('Flipping Pages to Page', page_counter)

    # Increase the page counter for the next iteration
    page_counter += 1

    # Add some delay to avoid overwhelming the server
    time.sleep(1)
