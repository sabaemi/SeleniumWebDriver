from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

address = input("Enter the address: ")
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get(address)
# driver.get("E:\\school\\.SoftwareTesting\\Tamrin\\project\\example.html")

def check_exists_by_css(cssSelector):
    try:
        driver.find_elements_by_css_selector(cssSelector)
    except NoSuchElementException:
        return False
    return True
def check_exists_by_xpath(xpath):
    try:
        driver.find_elements_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

print("**** Question 1 ****")
if check_exists_by_xpath("//a"):
    lnks = driver.find_elements_by_tag_name("a")
    formats=["tif","tiff","bmp","jpg","jpeg","gif","png","eps","raw","cr2","nef","orf","sr2","apng","avif","jfif","jpeg","pjp","svg","webp"]
    for a in lnks:
        word = a.get_attribute("href")
        extntion = word[-5:]
        if("html" not in extntion):
            for x in formats:
                if (x in extntion):
                    print("Link",word, "should not directly target image")

print("**** Question 2 ****")
d = {
    '[accept]': ['form'],
    '[align]': ['caption', 'col', 'div', 'embed', 'h1', 'hr', 'iframe', 'img', 'input', 'legend', 'object', 'p','table', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
    '[alink]': ['body'],
    '[allowtransparency]': ['iframe'],
    '[archive]': ['object'],
    '[axis]': ['td', 'th'],
    '[background]': ['body', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th'],
    '[bgcolor]': ['body', 'table', 'td', 'th', 'tr'],
    '[border]': ['object'],
    '[bordercolor]': ['table'],
    '[cellpadding]': ['table'],
    '[cellspacing]': ['table'],
    '[char]': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
    '[charoff]': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
    '[charset]': ['a', 'link'],
    '[classid]': ['object'],
    "[clear]": ['br'],
    '[code]': ['object'],
    '[codebase]': ['object'],
    '[codetype]': ['object'],
    '[color]': ['hr'],
    '[compact]': ['dl', 'ol', 'ul'],
    '[coords]': ['a'],
    '[datafld]': ['a', 'applet', 'button', 'div', 'fieldset', 'frame', 'iframe', 'img', 'input', 'label', 'legend','marquee', 'object', 'param', 'select', 'span', 'textarea'],
    '[dataformatas]': ['button', 'div', 'input', 'label', 'legend', 'marquee', 'object', 'option', 'select', 'span','table'],
    '[datapagesize]': ['table'],
    '[datasrc]': ['a', 'applet', 'button', 'div', 'frame', 'iframe', 'img', 'input', 'label', 'legend', 'marquee','object', 'option', 'select', 'span', 'table', 'textarea'],
    '[declare]': ['object'],
    '[event]': ['script'],
    '[for]': ['script'],
    '[frame]': ['table'],
    '[frameborder]': ['iframe'],
    '[height]': ['td', 'th'],
    '[hspace]': ['embed', 'iframe', 'img', 'input', 'object'],
    '[ismap]': ['input'],
    '[link]': ['body'],
    '[lowsrc]': ['img'],
    '[marginbottom]': ['body'],
    '[marginheight]': ['body', 'iframe'],
    '[marginleft]': ['body'],
    '[marginright]': ['body'],
    '[margintop]': [' body'],
    '[marginwidth]': ['body', 'iframe'],
    '[methods]': ['a', 'link'],
    '[name]': ['embed', 'img', 'option'],
    '[nohref]': ['area'],
    '[noshade]': [' hr'],
    '[nowrap]': ['td', 'th'],
    '[profile]': ['head'],
    '[rules]': ['table'],
    '[scheme]': ['meta'],
    '[scope]': [' td'],
    '[scrolling]': [' iframe'],
    '[shape]': ['a'],
    '[size]': [' hr'],
    '[standby]': [' object'],
    '[summary]': [' table'],
    '[target]': ['link'],
    '[text]': ['body'],
    '[type]': ['li', 'param', 'ul'],
    '[urn]': ['a', 'link'],
    '[usemap]': [' input'],
    '[valign]': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
    '[valuetype]': ['param'],
    '[version]': ['html'],
    '[vlink]': [' body'],
    '[vspace]': ['embed', 'iframe', 'img', 'input', 'object'],
    '[width]': ['col', 'hr', 'pre', 'table', 'td', 'th']
}
for key, value in d.items():
    if check_exists_by_css(key):
        elem = driver.find_elements_by_css_selector(key)
        for x in elem:
            for y in value:
                if x.tag_name == y:
                    print("Attribute",key,"should not be used in",y)
d2={'[border]': ['img'],'[language]': ['script'],'[name]': ['a']}
for key, value in d2.items():
    if check_exists_by_css(key):
        elem = driver.find_elements_by_css_selector(key)
        for x in elem:
            for y in value:
                if x.tag_name == y:
                    if (key == "[border]" and x.get_attribute("border") != "0"):
                        print("Attribute", key, "should not be used in", y,"if border is not equal to zero")
                    elif (key == "[language]" and x.get_attribute("language").lower() != "javascript"):
                        print("Attribute", key, "should not be used in", y,"if language is not javascript")
                    elif (key == "[name]" and x.get_attribute("name") != x.get_attribute("id")):
                        print("Attribute", key, "should not be used in", y,"if name is not eqaul to a's element id")

print("**** Question 3 ****")
if check_exists_by_xpath("//meta"):
    lnks = driver.find_elements_by_tag_name("meta")
    for a in lnks:
        refrsh = a.get_attribute("http-equiv")
        if(refrsh=="refresh"):
            print("Meta tags should not be used to refresh or redirect")

print("**** Question 4 ****")
if check_exists_by_css("[style]"):
    print("The style attribute should not be used in:")
    elem = driver.find_elements_by_css_selector("[style]")
    for x in elem:
        print(x.tag_name)

print("**** Question 5 ****")
if check_exists_by_xpath("//a"):
    lnks = driver.find_elements_by_tag_name("a")
    uniqelm = []
    uniqtxt = []
    for x in lnks:
        if x.text not in uniqtxt:
            uniqtxt.append(x.text)
            uniqelm.append(x)

    flag = 0
    for x in uniqelm:
        for y in lnks:
            if x.text == y.text:
                if x.get_attribute("href") != y.get_attribute("href"):
                    if flag != x:
                        print("Links with text", x.text, "have different targets:")
                        # print(x.text)
                        print(x.get_attribute("href"))
                        print(y.get_attribute("href"))
                        flag = x
                    else:
                        print(y.get_attribute("href"))

print("**** Question 6 ****")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def doOverlap(l1, r1, l2, r2):
    if (l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y):
        return False
    if (l1.x >= r2.x or l2.x >= r1.x):
        return False
    if (l1.y >= r2.y or l2.y >= r1.y):
        return False
    return True

def checkoverlap():
    flag=0
    size=[800,600,1024,768,1448,1072,1600,1200,2048, 1536]
    elem=[]
    taglist=["input","label","select","textarea","button","fieldset","legend","datalist","output","option","optgroup"]
    for x in taglist:
        if check_exists_by_css(x):
            tolist=driver.find_elements_by_css_selector(x)
            for y in tolist:
                elem.append(y)
    if len(elem)>0:
        i=0
        while i < len(size):
            print("Check with size", size[i],",", size[i+1],":")
            driver.set_window_size(size[i], size[i+1])
            for x in range(len(elem)):
                lx = elem[x].location.get('x')
                ly = elem[x].location.get('y')
                h = elem[x].size.get('height')
                w = elem[x].size.get('width')
                rx = lx + w
                ry = ly + h
                l = Point(lx, ly)
                r = Point(rx, ry)
                for y in range(x + 1, len(elem)):
                    lx = elem[y].location.get('x')
                    ly = elem[y].location.get('y')
                    h = elem[y].size.get('height')
                    w = elem[y].size.get('width')
                    rx = lx + w
                    ry = ly + h
                    l1 = Point(lx, ly)
                    r1 = Point(rx, ry)
                    if (doOverlap(l, r, l1, r1)):
                        if (l1.x != l.x or l1.y != l.y or r1.x != r.x or r1.y != r.y):
                            print(elem[x].tag_name, "and", elem[y].tag_name, "Overlap")
                            flag=1
                            # print(elem[x].tag_name, "number", x,"and", elem[y].tag_name, " number",y, "Overlap")
            i=i+2
            if (flag != 1): print("no overlap found!")
    else: print("no input element found!")


print("Check Overlap In Chrome:")
checkoverlap()
driver.close()
print("Check Overlap In FireFox:")
driver = webdriver.Firefox()
driver.get(address)
# driver.get("E:\\school\\.SoftwareTesting\\Tamrin\\project\\sample1 - Copy.htm")
checkoverlap()

driver.close()