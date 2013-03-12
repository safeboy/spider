def get_page(url):
    """��ȡ��ҳ����"""
    try:
        import urllib
        return url.urlopen(url).read()
    except:
        return ""
    

def get_next_target(page):
    """��page�л�ȡһ��������
        ���ҷ������ӵ�ַ
        ������ĩβ������λ��"""
    start_link = page.find('href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    """�ϲ�p��q��������"""
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    """��ȡҳ�����г����ӣ��������links
        �б���"""
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    """���棬����������seed��ʼ"""
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            union(tocrawl, get_all_links( content ))
            crawled.append(page)
    return crawled


def print_links(links):
    """��ӡlinks�б���������"""
    for link in links:
        print link
        

