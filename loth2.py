import requests
from bs4 import BeautifulSoup
import re
# Make a GET request to the webpage
url = "https://divineoffice.org/0621-mp/?accessible=true&date=20230621"  # Replace with your desired URL

# Set the User-Agent header to spoof a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

# Fetch the HTML content from the URL with the spoofed User-Agent
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200 indicates success)
def psalm_extractor(html):
    psalm_number_pattern = r'<span style="color: #ff0000;">(.*?)<br />'
    descriptor_pattern = r'">(.*?)<br />'
    scripture_verse_pattern = r'\((.*?)\)\.'
    content_pattern = r'</p>\n<p>(.*?)</p>'

    # Extracting sections using regular expressions
    psalm_number = re.search(psalm_number_pattern, html).group(1)
    descriptor = re.search(descriptor_pattern, html).group(1)
    scripture_verse = re.search(scripture_verse_pattern, html).group(1)
    content = re.findall(content_pattern, html, re.DOTALL)[0]

    # Printing the sections
    print("Psalm Number:", psalm_number)
    print("Descriptor:", descriptor)
    print("Scripture Verse:", scripture_verse)
    print("Content:", content)
def get_p_text(identifier):
    str=""
    if type(identifier) is list:
        
        for l in identifier:
            str=str+'p:-soup-contains("'+l+'"),'
        str=str[:-1]
    else:
        str='p:-soup-contains("'+identifier+'")'
        
    ant1=soup.select_one(str)
    for child in ant1.find_all(['span']):
        child.extract()

    target_text = ant1.get_text(separator=' ').strip()
    return target_text
def get_psalm(num):
    '''does require psalm to end with Glory...'''
    
    psalm_match = re.search(r'(?:Ant\.( ?)'+str(num)+'(.+?)<\/p(.+?)<\/p>)(.+?)<p>Glory to the', response.text, flags=re.MULTILINE|re.DOTALL)
    #re.compile(pattern, flags=re.MULTILINE|re.DOTALL)
    if psalm_match:
        psalm_text = psalm_match.group(4)
        # Remove any remaining HTML tags
        #psalm_text = re.sub(r'<.*?>', '', psalm_text)
        return(psalm_text.strip())

if response.status_code == 200:
    #print(response.text)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Use BeautifulSoup to find the desired element(s)
    try:
        hymn = soup.find('div', class_='hymn-container')
        #print("Hymn:", hymn)

        ant1=get_p_text("Ant. 1")
        print("Ant. 1:", ant1)

        ant2=get_p_text(["Ant. 2","Ant.2"])
        print("Ant. 2:", ant2)

        ant3=get_p_text(["Ant. 3","Ant.3"])
        print("Ant. 3:", ant3)            
            
        psalm1 = get_psalm(1)
        print("Psalm 1:", psalm1)

        psalm2 = get_psalm(2)
        print("Psalm 2:", psalm2)
        psalm3 = get_psalm(3)
        print("Psalm 3:", psalm3)
        
        exit
        psalm1 = soup.find(string='Psalm 1').find_next('p').get_text(strip=True)
        ant2 = soup.find(string='Ant. 2').find_next('p').get_text(strip=True)
        psalm2 = soup.find(string='Psalm 2').find_next('p').get_text(strip=True)
        ant3 = soup.find(string='Ant. 3').find_next('p').get_text(strip=True)
        psalm3 = soup.find(string='Psalm 3').find_next('p').get_text(strip=True)
        reading = soup.find(string='Reading').find_next('p').get_text(strip=True)
        responsory = soup.find(string='Responsory').find_next('p').get_text(strip=True)
        canticle_antiphon = soup.find(string='Canticle of Zechariah Antiphon').find_next('p').get_text(strip=True)
        intercessions = soup.find(string='Intercessions').find_next('p').get_text(strip=True)
        concluding_prayer = soup.find(string='Concluding Prayer').find_next('p').get_text(strip=True)

        # Print the extracted fields
        print("Hymn:", hymn)
        print("Ant. 1:", ant1)
        print("Psalm 1:", psalm1)
        print("Ant. 2:", ant2)
        print("Psalm 2:", psalm2)
        print("Ant. 3:", ant3)
        print("Psalm 3:", psalm3)
        print("Reading:", reading)
        print("Responsory:", responsory)
        print("Canticle of Zechariah Antiphon:", canticle_antiphon)
        print("Intercessions:", intercessions)
        print("Concluding Prayer:", concluding_prayer)


    except IndexError:
        print("Element not found")
else:
    print("Failed to fetch the webpage. Error:", response.status_code)

