import mechanize,time
from bs4 import BeautifulSoup
def submit(s,code):
    br=mechanize.Browser()
    br.open('http://www.spoj.com/')
    br.select_form(nr=0)
    user,password='muk','urmilaswati'
    br.form['login_user']=user
    br.form['password']=password
    res=br.submit()
    response=res.read()
    res=br.open('http://www.spoj.com/submit/'+code+'/')
    br.select_form(nr=0)
    br.form['file']=s
    br.form['lang']=['4']
    res=br.submit()
    response=res.read()
    x=response.index('Solution submitted!')
    if x==-1:
        print 'Not submitted'
    else:
        time.sleep(5)
        res=br.open('http://www.spoj.com/status/muk/')
        response=res.read()
        soup=BeautifulSoup(response)
        table=soup.find('table',attrs={'class':'problems table newstatus'})
        tbody=table.find('tbody')
        tr=tbody.find('tr')
        print tr['class']
'''
s="""
t=int(raw_input(''))
while t!=42:
    print t
    t=int(raw_input(''))"""
code='TEST'
submit(s,code)
'''
