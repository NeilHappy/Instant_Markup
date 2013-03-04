import sys,re
from util import *

print "<html><head><title>...</title><body>"

title=True

for block in blocks(sys.stdin):
    block =re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)  #This pattern r'\*(.+?)\*'可以改成r'\*(.*)\*' and I think they are the same.
    if title:
        print '<h1>'
        print block
        print '</h1>'
        title=False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'
