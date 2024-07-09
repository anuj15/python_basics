from bs4 import BeautifulSoup

with open('website.html', encoding='utf-8') as f:
    contents = f.read()
soup = BeautifulSoup(markup=contents, features='html.parser')

# title of the webpage
print(soup.title.text)

# first anchor tag
print(soup.a.text)

# find all anchor tags
tags = soup.find_all(name='a')
print(tags)

for tag in tags:
    print(tag.get('href'))

# find using tag & attribute
tag = soup.find(name='h1', id='name')
print(tag.text)

tag = soup.find(name='h3', class_='heading')
print(tag.text)

# find using css selector
tag = soup.select_one(selector='p a')
print(tag.text)
print(tag.get('href'))

tag = soup.select_one(selector='#name')
print(tag.text)

tags = soup.select(selector='.heading')
print(tags)
