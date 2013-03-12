def get_page(url):
    """获取网页内容"""
    try:
        import urllib
        return url.urlopen(url).read()
    except:
        return ""
    

def get_next_target(page):
    """从page中获取一个超链接
        并且返回链接地址
        和链接末尾的索引位置"""
    start_link = page.find('href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    """合并p、q两个集合"""
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    """获取页面所有超链接，结果放在links
        列表中"""
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
    """爬虫，从种子链接seed开始"""
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
    """打印links列表所有内容"""
    for link in links:
        print link
        

