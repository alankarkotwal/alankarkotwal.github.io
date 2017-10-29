#################################################
# Placement Notification Script '15             #
# Alankar Kotwal <alankarkotwal13@gmail.com>    #
#################################################

import urllib2, base64, getpass, smtplib, pdb
from bs4 import BeautifulSoup as bs
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

theurl = "http://placements.iitb.ac.in/blog/"
uname = raw_input('Enter LDAP username: ')
passwd = getpass.getpass()

base64string = base64.encodestring('%s:%s' % (uname, passwd))[:-1]
authheader =  "Basic %s" % base64string

last = ''

me = "aloo@wncc-iitb.org"
you = "alankarkotwal13+placements@gmail.com"

while 1:
    
    req = urllib2.Request(theurl)
        req.add_header("Authorization", authheader)
        
        handle = urllib2.urlopen(req)
        resp = handle.read()
        
        soup = bs(resp, "html.parser")
        mydivs = soup.findAll("div", { "class" : "post" })
        
        now = mydivs[0].findAll('a')[0]
        nowString = now.string
        
        if last != nowString:
            
            link = now['href']
                
                reqIn = urllib2.Request(link)
                reqIn.add_header("Authorization", authheader)
                
                handleIn = urllib2.urlopen(reqIn)
                respIn = handleIn.read()
                
                soupIn = bs(respIn, "html.parser")
                mydivsIn = soupIn.findAll("div", { "class" : "entry" })
                
                attLinkTags = mydivsIn[0].findAll('a')
                
                msg = MIMEMultipart('alternative')
                msg['Subject'] = nowString
                msg['From'] = me
                msg['To'] = you
                
                text = link
                html = respIn
                
                part1 = MIMEText(text, 'plain')
                part2 = MIMEText(html, 'html')
                
                msg.attach(part1)
                msg.attach(part2)
                
                for tag in attLinkTags:
                    
                    attLink = tag['href']
                        if ".xlsx" in attLink or ".csv" in attLink or ".docx" in attLink:
                            
                            attName = attLink.split('/')[-1]
                                
                                attReq = urllib2.Request(attLink)
                                attReq.add_header("Authorization", authheader)
                                
                                attHandle = urllib2.urlopen(attReq)
                                attachment = attHandle.read()
                                
                                part3 = MIMEBase('application', "octet-stream")
                                part3.set_payload(attachment)
                                encoders.encode_base64(part3)
                                part3.add_header('Content-Disposition', 'attachment; filename="'+attName+'"')
                                msg.attach(part3)
                
                s = smtplib.SMTP('localhost')
                s.sendmail(me, [you], msg.as_string())
                s.quit()
                
            last = nowString