import requests
from bs4 import BeautifulSoup
import re
from Hour import Breviary, Antiphon, Psalm

# Helper function to extract text from HTML element
def get_text_from_element(soup,identifier):
    if isinstance(identifier, list):
        # Multiple identifiers provided as a list
        selectors = 'p:-soup-contains("' + '"), p:-soup-contains("'.join(identifier) + '")'
    else:
        # Single identifier provided as a string
        selectors = 'p:-soup-contains("' + identifier + '")'

    element = soup.select_one(selectors)
    for child in element.find_all(['span']):
        child.extract()
    
    target_text = element.get_text(separator=' ').strip()
    return target_text

# Helper function to extract information using regular expressions
def extract_regex(needle, haystack, group):
    match = re.search(needle, haystack, flags=re.MULTILINE|re.DOTALL)
    results = []
    
    if match:
        if isinstance(group, list):
            for g in group:
                results.append(match.group(g).strip())
        elif isinstance(group, bool):
            results = match
        elif isinstance(group, int):
            results = match.group(group).strip()
        
    return results

# Function to extract information from psalm sections
def extract_psalm(html):
    psalm_number_pattern = r'<span style="color: #ff0000;">(.*?)<br />'
    descriptor_pattern = r'<br \/>\n(.*?)<\/'
    scripture_verse_pattern = r'<em>(.+?)<\/em>'
    scripture_verse_author_pattern = r'\((.+?)\)'

    # Extracting sections using regular expressions
    psalm_number = re.search(psalm_number_pattern, html).group(1).strip()
    descriptor = re.search(descriptor_pattern, html, flags=re.MULTILINE|re.DOTALL).group(1).strip()
    try:
        scripture_verse = re.search(scripture_verse_pattern, html).group(1).strip()
    except AttributeError:
        scripture_verse = ""
    try:
        #some psalms don't have this so return empty
        scripture_verse_author = re.search(scripture_verse_author_pattern, html).group(1).strip()
    except AttributeError:
        scripture_verse_author = ""
    # Printing the sections
    #print("Psalm Number:", psalm_number)
    #print("Descriptor:", descriptor)
    #print("Scripture Verse:", scripture_verse)
    #print("Scripture Verse Author:", scripture_verse_author)
    return {"psalm_number":psalm_number, "descriptor":descriptor,"scripture_verse":scripture_verse,"scripture_verse_author":scripture_verse_author,"psalm_text":None}

# Function to extract intercessions
def extract_intercessions(haystack):
    first = ""
    reply = ""
    subsequent = []
    first_pass = extract_regex(
        "INTERCESSIONS(?:.*?)<p>(.*?)<br \/>(?:.*?)<em>(.*?)<\/em>(?:.*?)\n(.*?)<p>Our Father who art in heaven,<br />",
        haystack, [1, 2, 3]
    )
    first = first_pass[0]
    reply = first_pass[1]
    second_pass = extract_regex(
        "(?:<p>(.*?)<br \/>(?:.*?)<\/span> (.*?)<br \/>(?:.*?)<\/p>(?:\n?))",
        first_pass[2], False
    )
    return {"first": first, "reply": reply, "subsequent": second_pass}

# Function to extract psalm text
def get_psalm_text(haystack,num):
    psalm_match = re.search(
        r'(?:Ant\.( ?)' + str(num) + '(.+?)<\/p(.+?)<\/p>)(.+?)<p>Glory to the',
        haystack, flags=re.MULTILINE|re.DOTALL
    )
    
    if psalm_match:
        psalm = extract_psalm(psalm_match.group(3).strip())
        psalm_text = psalm_match.group(4)
        psalm["psalm_text"] = psalm_text.strip()
        return psalm
            
            
def scrape_url(url):
    # Fetch the HTML content from the URL with the spoofed User-Agent
    response = requests.get(url, headers=headers)

    if "No content found" in response.text:
        raise ValueError("Wrong URL: No content found")
        
        
    # Check if the request was successful (status code 200 indicates success)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        try:
            # Extract information from the webpage
            hymn = soup.find('div', class_='hymn-container')
            antiphon1 = Antiphon("Ant. 1", get_text_from_element(soup,"Ant. 1"))
            antiphon2 = Antiphon("Ant. 2", get_text_from_element(soup,["Ant. 2", "Ant.2"]))
            antiphon3 = Antiphon("Ant. 3",get_text_from_element(soup,["Ant. 3", "Ant.3"]))
            psalm1 = Psalm(get_psalm_text(response.text,1))
            psalm2 = Psalm(get_psalm_text(response.text,2))
            psalm3 = Psalm(get_psalm_text(response.text,3))
            reading = extract_regex("READING <\/span>(.*?)<\/p>\n<p>(.*?)<\/p>", response.text, [1, 2])
            responsory = extract_regex(
                "RESPONSORY(?:\s?)<\/span><\/p>\n<p>(.*?)<br \/>\n<span style=\"color: #ff0000;\">&#8212;<\/span> (.*?)<\/p>\n<p>(.*?)<br \/>\n<span style=\"color: #ff0000;\">&#8212;<\/span> (.*?)<\/p>\n<p>(.*?)<br \/>\n<span style=\"color: #ff0000;\">&#8212;<\/span> (.*?)<\/p>",
                response.text, [1, 2, 3, 4, 5, 6]
            )
            canticle_antiphon = extract_regex("CANTICLE OF ZECHARIAH(?:.*?)Ant.(?:\s*?)<\/span> (.*?)<\/p>", response.text, 1)
            intercessions = extract_intercessions(response.text)
            concluding_prayer = extract_regex("Concluding Prayer(?:.*?)<p>(.*?)<br />\n<span", response.text, 1)

            # Print the extracted fields
            print("Hymn:", hymn)
            print("Antiphon 1:", antiphon1)
            print("Psalm 1:", psalm1)
            print("Antiphon 2:", antiphon2)
            print("Psalm 2:", psalm2)
            print("Antiphon 3:", antiphon3)
            print("Psalm 3:", psalm3)
            exit(0)
            print("Reading Verse:", reading[0])
            print("Reading:", reading[1])
            print("Responsory Verse 1:", responsory[0])
            print("Responsory Response 1:", responsory[1])
            print("Responsory Verse 2:", responsory[2])
            print("Responsory Response 2:", responsory[3])
            print("Responsory Verse 3:", responsory[4])
            print("Responsory Response 3:", responsory[5])
            print("Canticle of Zechariah Antiphon:", canticle_antiphon)
            print("Intercessions:", intercessions)
            print("Concluding Prayer:", concluding_prayer)

        except IndexError:
            print("Element not found")
    else:
        print("Failed to fetch the webpage. Error:", response.status_code)

# Set the base URL
base_url = "https://divineoffice.org/ord-w{week}-{day}-{prayer}/?accessible=true"

# Set the User-Agent header to spoof a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
}

# Define the days, weeks, and prayer times
days = ["mon", "tue", "wed", "thu", "fri", "sat"]
weeks = ["01", "02", "03", "04"]
prayer_times = ["mp"]#, "ep"]

# Loop through the combinations of days, weeks, and prayer times
for week in weeks:
    for day in days:
        for prayer in prayer_times:
            # Exclude Saturday Evening Prayer
            if day == "sat" and prayer == "ep":
                continue

            # Construct the modified URL
            url = base_url.format(week=week, day=day, prayer=prayer)
            
            print("Week:",week," Day:",day," Prayer:",prayer," ",url,"\n")
            scrape_url(url)