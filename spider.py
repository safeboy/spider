from urllib2 import urlopen

def get_page(url):
    try:
        html = urlopen(url)
        page = html.read()
        #print page
        return page
    except:
        return ""
    return ""
    

def get_next_target(page):
    start_link = page.find('href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
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
    f = file('website.txt', 'w')
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            #tocrawl = tocrawl + get_all_links( get_page(page) )
            union(tocrawl, get_all_links( get_page(page) ) )
            page = page + "\n"
            print page
            f.writelines(page)
            crawled.append(page)
    f.close()
    return crawled


def print_links(links):
    for link in links:
        print link
        
#links = crawl_web('http://www.udacity.com/cs101x/index.html')

#crawl_web('http://www.udacity.com/cs101x/index.html')

#print_links(links)

#print get_page('http://www.baidu.com')

crawl_web('http://www.bistu.edu.cn')

    