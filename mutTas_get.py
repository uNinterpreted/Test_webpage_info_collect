#!/usr/bin/python
# -*- coding: utf-8 -*-

import mechanize
import sys,time,re
from bs4 import BeautifulSoup

br = mechanize.Browser()

br.set_handle_equiv(True)
#br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

#Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

# 欺骗行为
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
                                'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


r = br.open('http://www.mutationtaster.org/StartQueryEngine.html')
# for f in br.forms():
#     print f

br.select_form(nr = 0)

vcf_file = "E:\\05.WorkSpace\\05.splicing_sites\\FB199B0060-A3A7AA8XKF1-A001L000.intron_sys.vcf"
br.form.add_file(open(vcf_file), 'text/plain', vcf_file)
br.form.set_all_readonly(False)
#br.form['filename'] = "vcf"
br.submit()
# # # 查看搜索结果
brr=br.response().read()
#是html代码
soup = BeautifulSoup(brr, features="html5lib")
# for i,child in enumerate(soup.body.children):
#     print(i,child)
project_html = soup.find(text=re.compile("^.*opt/tmp/vcf_.*progress\.html$"))
project = re.match(".*tmp(/vcf.*html$)", project_html)
if project:
    project_id = project.group(1)
else:
    print "[WARN] No ProjectID found."
    sys.exit()

result_url = "http://doro.charite.de/" + "temp" + project_id
print result_url
time.sleep(100)
cr = mechanize.Browser()

cr.set_handle_equiv(True)
#br.set_handle_gzip(True)
cr.set_handle_redirect(True)
cr.set_handle_referer(True)
cr.set_handle_robots(False)

#Follows refresh 0 but not hangs on refresh > 0
cr.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

cr.set_debug_http(True)
cr.set_debug_redirects(True)
cr.set_debug_responses(True)

# 欺骗行为
cr.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) '
                                'Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

res = cr.open(result_url)
print res.read()
# for f in cr.forms():
#     print f
# export = cr.submit(nr=1)
# print export

