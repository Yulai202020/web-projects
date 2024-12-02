import cherrypy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import jinja2
import sqlite3
import random

class HelloWorld(object):

    @cherrypy.expose
    def sendform(self):
        with open("send_message.html") as file:
            a = file.read()
        tmpl = jinja2.Template(a)
        return tmpl.render()

    @cherrypy.expose
    def delete(self,id):
        id = int(id)
        with sqlite3.connect("data.db") as conn :
            conn.executescript("DELETE From Data where ID = {}".format(id))
        raise cherrypy.HTTPRedirect("/")
    
    @cherrypy.expose
    def view(self,id):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Data where ID = {}".format(id))
        rows = cur.fetchall()
        with open("view.html") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(row=rows[0])

    @cherrypy.expose
    def index(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * from Data")
        rows = cur.fetchall()
        with open("index.html") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(rows=rows)

    @cherrypy.expose
    def send(self,subject,to,message):
        # try :
        addr_from = "bdishbum@gmail.com"
        password = "oGOz.KJ*aLM36EO"
        msg = MIMEMultipart()
        msg['From'] = addr_from
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(True)
        server.starttls()
        server.login(addr_from, password)
        server.send_message(msg)
        server.quit()
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Data(\"From\",\"To\",Subject,Message) values ('bdishbum@gmail.com','{0}','{1}','{2}')".format(to,subject,message))
        raise cherrypy.HTTPRedirect("/")

cherrypy.quickstart(HelloWorld())