from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import sys
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

def main():
    page = Page('http://quote.eastmoney.com/center/gridlist.html#hs_a_board')
    soup = BeautifulSoup(page.html, 'lxml')
    pattern = re.compile(r'//quote.eastmoney.com/.*?/.*?/\d\.(.*)')
    tagList = soup.findAll('a', href=pattern)
    for tag in tagList:
        if re.search(r'^\d+$',tag.getText()) != None:
            print(tag.getText())

if __name__ == '__main__': main()


