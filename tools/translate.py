import json
import sys
from bs4 import BeautifulSoup

def html_to_json(content, indent=None):
    soup = BeautifulSoup(content, "html.parser")
    rows = soup.find_all("tr")
    
    headers = {}
    thead = soup.find("thead")
    if thead:
        thead = thead.find_all("th")
        for i in range(len(thead)):
            headers[i] = thead[i].text.strip().lower()
    data = []
    for row in rows:
        cells = row.find_all("td")
        if thead:
            items = {}
            for index in headers:
                items[headers[index]] = cells[index].text
        else:
            items = []
            for index in cells:
                items.append(index.text.strip())
        data.append(items)
    return json.dumps(data, indent=indent)


# if __name__ == "__main__":
# content = "<table> <thead> <th>Company</th> <th>Contact</th> <th>Country</th> </thead> <tr> <td>Alfreds Futterkiste</td><td>Maria Anders</td><td>Germany</td></tr><tr> <td>Centro comercial Moctezuma</td><td>Francisco Chang</td><td>Mexico</td></tr><tr> <td>Ernst Handel</td><td>Roland Mendel</td><td>Austria</td></tr><tr> <td>Island Trading</td><td>Helen Bennett</td><td>UK</td></tr><tr> <td>Laughing Bacchus Winecellars</td><td>Yoshi Tannamuri</td><td>Canada</td></tr><tr> <td>Magazzini Alimentari Riuniti</td><td>Giovanni Rovelli</td><td>Italy</td></tr></table>"
lines = sys.stdin.readlines()
content = ""
for line in lines:
    content += line
sys.stdout.write(html_to_json(content, indent=4))
