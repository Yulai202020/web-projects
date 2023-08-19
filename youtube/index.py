import cherrypy
import jinja2
import sqlite3
import random
import os
import json
from cherrypy.lib.static import serve_file
cmd=os.getcwd()

MYID = ""
cherrypy.config.update({
    'server.socket_host':'127.5.5.5',
    'server.socket_port': 7555,
    'log.error_file': 'site.log',
    'tools.encode.encoding': 'utf-8',
    'tools.encode.on': True,
})

class user(object):
    @cherrypy.expose
    def logout(self):
        raise cherrypy.HTTPRedirect("/user/login")
    @cherrypy.expose
    def login(self):
        with open("sites/login.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render()
    @cherrypy.expose
    def regis(self):
        with open("sites/regis.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render()
    @cherrypy.expose
    def accaunt(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Accaunts where ID = '{0}'".format(MYID))
        mess = cur.fetchall()
        emailuser = ""
        cur.execute("SELECT Emails From Accaunts where ID = '{0}'".format(MYID))
        ro1 = cur.fetchall()
        for i in ro1:
            emailuser = i[0]
        with open("main/accauntinfo.html") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(mess=mess,ID=MYID,emailuser=emailuser)

class home(object):
    @cherrypy.expose
    def linksvideos(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT \"ID\" From Videos")
        rows = cur.fetchall()
        emailuser = ""
        cur.execute("SELECT Emails From Accaunts where ID = '{0}'".format(MYID))
        ro1 = cur.fetchall()
        for i in ro1:
            emailuser = i[0]
        with open("main/linksvideos.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(mess=rows,ID=MYID,emailuser=emailuser)
    @cherrypy.expose
    def results(self,search,ID):
        MYID = ID
        row = ""
        likes = ""
        author = ""
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Videos where \"Videos Names\" = '{0}'".format(search))
        rows = cur.fetchall()
        for i in rows:
            likes = i[4]
            author = i[1] 
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT ID From Videos where \"Videos Names\" = '{0}'".format(search))
        rows2 = cur.fetchall()
        for i in rows2:
            row = i[0]
        emailuser = ""
        cur.execute("SELECT Emails From Accaunts where ID = '{0}'".format(MYID))
        ro1 = cur.fetchall()
        for i in ro1:
            emailuser = i[0]
        if row == "":
            with open("sites/resultsnone.html") as file:
                html = file.read()
        else :
            with open("sites/results.html") as file:
                html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,namevideo=search,idvideo=row,emailuser=emailuser,likes=likes,author=author)

    @cherrypy.expose
    def watch(self,ID,MYIDIN):
        emailuser = ""
        author = ""
        videonam = ""
        description = ""
        MYID = MYIDIN
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Videos where ID = {0}".format(ID))
        rows = cur.fetchall()
        cur.execute("SELECT * From Comments where IDvideos = {0}".format(ID))
        ro = cur.fetchall()
        cur.execute("SELECT Emails From Accaunts where ID = '{0}'".format(MYID))
        ro1 = cur.fetchall()
        for i in ro1:
            emailuser = i[0]
        for i in rows:
            author = i[1]
            videonam = i[2]
            description = i[3]
        with open("sites/watch.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(rows=ro,row=ID,ID=MYID,videonam=videonam,description=description,emailuser=emailuser,author=author)
    @cherrypy.expose
    def index(self,ID):
        MYID = ID
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
    @cherrypy.expose
    def home(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Videos where ID > 0")
        rows = cur.fetchall()
        emailuser = ""
        cur.execute("SELECT Emails From Accaunts where ID = '{0}'".format(MYID))
        ro1 = cur.fetchall()
        for i in ro1:
            emailuser = i[0]
        with open("main/home.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(rows=rows,ID=MYID,emailuser=emailuser)
    @cherrypy.expose
    def top(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Videos WHERE Likes >= 20 ORDER BY Likes DESC")
        rows = cur.fetchall()
        emailuser = ""
        cur.execute("SELECT Emails From Accaunts where ID = '{0}'".format(MYID))
        ro1 = cur.fetchall()
        for i in ro1:
            emailuser = i[0]
        with open("main/top.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(rows=rows,ID=MYID,emailuser=emailuser)
    @cherrypy.expose
    def uploadfiles(self,ID):
        MYID = ID
        emailuser = ""
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT Emails From Accaunts where ID = '{0}'".format(MYID))
        ro1 = cur.fetchall()
        for i in ro1:
            emailuser = i[0]
        with open("main/uploadfiles.html") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,emailuser=emailuser)

class returns(object):
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
            conn.executescript("insert into Accaunts(\"Emails\",\"Passwords\",\"ID\") values ('{0}','{1}','{2}')".format(email,password,id))
        MYID = id
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
    @cherrypy.expose
    def write(self,ufile,videonam,description,ID):
        MYID = ID
        upload_path = os.path.dirname(__file__)
        upload_path = 'video/'+ufile.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path))
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Videos (\"Names\",\"Author\",\"Videos Names\",\"Descriptions\",\"Likes\",\"Dislikes\") values ('{0}','{1}','{2}','{3}',0,0)".format(ufile.filename,MYID,videonam,description))
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
    @cherrypy.expose
    def comments(self,ID,Comments,MYIDIN):
        MYID = MYIDIN
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Comments(\"IDvideos\",\"IDusers\",\"Comments\") values ('{0}','{1}','{2}')".format(ID,MYID,Comments))
        raise cherrypy.HTTPRedirect("/watch?ID="+ID+"&MYIDIN="+MYID)
    @cherrypy.expose
    def ajaxlike(self,id):
        likes = 0
        with sqlite3.connect("data.db") as conn:
            conn.executescript("UPDATE Videos SET Likes = Likes + 1 WHERE ID = {0}".format(id))
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            cur.execute("SELECT Likes From Videos where ID = {0}".format(id))
            rows = cur.fetchall()
            likes = rows[0]
        return json.dumps({"likes":likes})
    @cherrypy.expose
    def ajaxdislike(self,id):
        dislikes = 0
        with sqlite3.connect("data.db") as conn:
            conn.executescript("UPDATE Videos SET Dislikes = Dislikes + 1 WHERE ID = {0}".format(id))
            cur = conn.cursor()
            cur.execute("SELECT Dislikes From Videos where ID = {0}".format(id))
            rows = cur.fetchall()
            dislikes = rows[0]
        return json.dumps({"dislikes":dislikes})
    @cherrypy.expose
    def video(self,ID):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Videos where ID = {0}".format(ID))
        rows = cur.fetchall()
        for i in rows:
            v = cmd+"\\video\\"
            out = i[0]
            out = v + out
        return serve_file(out, "video/mp4", "inline", "test.mp4")

class files(object):
    @cherrypy.expose
    def stylemincss(self):
        return serve_file(cmd+"\\style.min.css", "text/css", "inline", "test.css")
    @cherrypy.expose
    def jsscriptmin(self):
        return serve_file(cmd+"\\script.min.js", "text/js", "inline", "test.js")
    @cherrypy.expose
    def stylecss(self):
        return serve_file(cmd+"\\style.css", "text/css", "inline", "test.css")
    @cherrypy.expose
    def jsscript(self):
        return serve_file(cmd+"\\script.js", "text/js", "inline", "test.js")
    @cherrypy.expose
    def infoyoutube(self):
        return serve_file(cmd+"\\infoofyoutube.txt", "text/txt", "inline", "test.txt")

if __name__ == '__main__':
    cherrypy.tree.mount(home())
    cherrypy.tree.mount(files(), '/files')
    cherrypy.tree.mount(user(), '/user')
    cherrypy.tree.mount(returns(), '/return')

    cherrypy.engine.start()
    cherrypy.engine.block()