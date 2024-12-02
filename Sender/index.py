import cherrypy
import jinja2
import sqlite3
import random

MYID = ""

class HelloWorld(object):

    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)

    @cherrypy.expose
    def home(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Accaunts where ID = '{0}'".format(MYID))
        emails = cur.fetchall()
        emailout = ""
        for email in emails:
            emailout = email[0] 
        with open("home.html") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,email=emailout)

    @cherrypy.expose
    def regis(self):
        with open("regis.html","r") as file:
            a = file.read()
        tmpl = jinja2.Template(a)
        return tmpl.render()

    @cherrypy.expose
    def write(self,email,password):
        rand0 = random.randint(0,9)
        rand1 = random.randint(0,9)
        rand2 = random.randint(0,9)
        rand3 = random.randint(0,9)
        rand4 = random.randint(0,9)
        rand5 = random.randint(0,9)
        rand6 = random.randint(0,9)
        rand7 = random.randint(0,9)
        id = str(rand0)+str(rand1)+str(rand2)+str(rand3)+"-"+str(rand4)+str(rand5)+str(rand6)+str(rand7)
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Accaunts(\"Email\",\"Password\",\"ID\") values ('{0}','{1}','{2}')".format(email,password,id))
        MYID = id
        with open("myid.dat","w") as file:
            file.write(MYID)
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)

    @cherrypy.expose
    def sending(self,to,message,From):
        message = str(message)
        if message == "" or message == None:
            raise cherrypy.HTTPRedirect("/home?ID="+From)
        else :
            with sqlite3.connect("data.db") as conn:
                conn.executescript("insert into Messages(\"To\",\"Message\",\"From\") values ('{0}','{1}','{2}')".format(to,message,From))
            raise cherrypy.HTTPRedirect("/home?ID="+From)
        raise cherrypy.HTTPRedirect("/home?ID="+From)
    
    @cherrypy.expose
    def delete(self,id,myidin):
        MYID = myidin
        id = int(id)
        with sqlite3.connect("data.db") as conn :
            conn.executescript("DELETE From Messages where ID = {}".format(id))
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)

    @cherrypy.expose
    def view(self,id,myidin):
        MYID = myidin
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Messages where ID = {}".format(id))
        rows = cur.fetchall()
        with open("view.html") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(row=rows[0],ID=MYID)

    @cherrypy.expose
    def accauntinfo(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Accaunts where ID = '{0}'".format(MYID))
        mess = cur.fetchall()
        with open("accauntinfo.html") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(mess=mess,ID=MYID)

    @cherrypy.expose
    def messages(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Messages where \"From\" = '{0}' or \"To\" = '{0}'".format(MYID))
        mess = cur.fetchall()
        with open("messages.html") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(mess=mess,ID=MYID)

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())