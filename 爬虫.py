import urllib.request
import re
class GetHtml(object)
	def _init_(self,URL,HEAD):
        self.url=URL
        self.head=HEAD
        
    def get_index(self):
      return self.response.read()
  self.request=urllib.request.Request(self,url)
 self.request.add_header("user-agent",self.head)
self.response=urllib.request.urlopen(self.request)
 return self.reponse.read()
#self.response=urllib.request.urlopen(self.url)
 def get_list(self):
	self.strimglist=[]
    self.imglist=re.findall(b"style/\w{60}.jpg",self.get_index())
  for i in self.imglist:
    self.strimglist.append(self.url+str+(i,encoding="utf-8"))
	return self.strimglist
    
    # print(self.strimglist)   #self.imglist=re.findall(b"style/\w{60}.jpg",self.get_index())


def get_image(self)
	num=0
    for self.url in self.get list():
     num+=1
   with open(str(num)+".jpg","wb") as f:
    f.write(self.get_index)

    html=GetHtml("http://10.10.10.209")
print(html.get_index())
