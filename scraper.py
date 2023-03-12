from bs4 import BeautifulSoup
from urllib import request
import re

html = request.urlopen("https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge").read()
soup = BeautifulSoup(html, "html.parser")

finalString = ""

for section in soup.body.findAll('section', { 'id': re.compile(r"^([0-9])\1") }, recursive=False):
  for main in section.findAll("main", { 'id': re.compile(r"([0-9])\1$") }, recursive=False):
    for article in main.findAll("article", { 'id': re.compile(r".+([0-9])\1.+") }, recursive=False):
      finalString += article.find("p", recursive=False).get("value")

print(finalString)
