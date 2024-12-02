import cherrypy
import jinja2
import sqlite3
import os
import random
from cherrypy.lib.static import serve_file

MYID = ""

class HelloWorld(object):

    @cherrypy.expose
    def img(self,ID):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From IMG where ID = {0}".format(ID))
        rows = cur.fetchall()
        for i in rows:
            v = 'c:/src/html/photos/img/'
            out = i[0]
            out = v + out
        return serve_file(out, "image/png", "inline", "test.png")

    # home and result
    @cherrypy.expose
    def index(self,ID):
        MYID = ID
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)

    @cherrypy.expose
    def home(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From IMG")
        rows = cur.fetchall()
        with open("home.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(rows=rows)

    # regis
    @cherrypy.expose
    def regis(self):
        with open("regis.html","r") as file:
            a = file.read()
        tmpl = jinja2.Template(a)
        return tmpl.render()

    @cherrypy.expose
    def creat(self,email,password):
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

    # write photos
    @cherrypy.expose
    def write(self,ufile,ID):
        MYID = ID
        upload_path = os.path.dirname(__file__)
        upload_filename = 'img/'+ufile.filename
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into IMG (\"NAME\") values ('{0}')".format(ufile.filename))
        upload_file = os.path.normpath(os.path.join(upload_path, upload_filename))
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read()
                if not data:
                    break
                out.write(data)
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)

    # uploadfiles
    @cherrypy.expose
    def uploadfiles(self,ID):
        MYID = ID
        with open("uploadfiles.html") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render()

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())