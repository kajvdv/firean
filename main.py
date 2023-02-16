import re


def main():
    text = '''2021 was a very challenging year, with strong growth in a
dynamic environment. The semiconductor industry has
reached new records of output and sales amid an ongoing
global pandemic while still being unable to satisfy the
demand for semiconductors. Industries around the world
are severely affected by this lack of supply. And despite
these challenging circumstances, I’m proud to say that at
ASML we continued to grow and have welcomed many
new colleagues. ASML reached €18.6 billion in net sales,
and we welcomed our 30,000th employee in Giheung,
South Korea. '''
    text = text.replace('\n', ' ')
    pattern = re.compile('[A-Z0-9][\s\S]+?\.\s')
    sentences = pattern.findall(text)
    for x in sentences:
        print(x)
    


if __name__ == '__main__':
    main()