import cherrypy
import jinja2
import sqlite3
import random
import os
from cherrypy.lib.static import serve_file
cmd=os.getcwd()

MYID = ""
cherrypy.config.update({
    'server.socket_host':'127.7.7.7',
    'server.socket_port': 7777,
    'log.error_file': 'site.log',
    'tools.encode.encoding': 'utf-8',
    'tools.encode.on': True,
})
conn = sqlite3.connect("data.db")

class HelloWorld(object):
    @cherrypy.expose
    def index(self,ID):
        MYID = ID
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
    @cherrypy.expose
    def home(self,ID):
        MYID = ID
        with open("sites/home.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)
    @cherrypy.expose
    def regis(self):
        with open("sites/regis.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render()
    @cherrypy.expose
    def writevideo(self,ufile,videonam,description,ID):
        MYID = ID
        upload_path = os.path.dirname(__file__)
        upload_path = 'video/'+ufile.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path))
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Files (\"Name\",\"Descriptions\",\"Type\") values ('{0}','{1}','video')".format(ufile.filename,videonam,description))
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
    @cherrypy.expose
    def writeaudio(self,ufile,audionam,description,ID):
        MYID = ID
        upload_path = os.path.dirname(__file__)
        upload_path = 'audiobook/'+ufile.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path))
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Files (\"Name\",\"Descriptions\",\"Type\") values ('{0}','{1}','audio')".format(ufile.filename,audionam,description))
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
    @cherrypy.expose
    def writemusic(self,ufile,musicnam,description,ID):
        MYID = ID
        upload_path = os.path.dirname(__file__)
        upload_path = 'music/'+ufile.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path))
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Files (\"Name\",\"Descriptions\",\"Type\") values ('{0}','{1}','music')".format(ufile.filename,description))
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
    @cherrypy.expose
    def writeimg(self,ufile,imgnam,description,ID):
        MYID = ID
        upload_path = os.path.dirname(__file__)
        upload_path = 'img/'+ufile.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path))
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Files (\"Name\",\"Descriptions\",\"Type\") values ('{0}','{1}','img')".format(ufile.filename,description))
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
    @cherrypy.expose
    def writescreenshote(self,ufile,ScreenShotenam,description,ID):
        MYID = ID
        upload_path = os.path.dirname(__file__)
        upload_path = 'img/'+ufile.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path))
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into Files (\"Name\",\"Descriptions\",\"Type\") values ('{0}','{1}','screenshote')".format(ufile.filename,description))
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)
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
    @cherrypy.expose
    def screenshote(self,ID):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where ID = {0}".format(ID))
        rows = cur.fetchall()
        for i in rows:
            v = 'c:/src/html/platform/img/'
            out = i[0]
            out = v + out
        return serve_file(out, "image/png", "inline", "sceenshot.png")
    @cherrypy.expose
    def img(self,ID):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where ID = {0}".format(ID))
        rows = cur.fetchall()
        for i in rows:
            v = 'c:/src/html/platform/img/'
            out = i[0]
            out = v + out
        return serve_file(out, "image/png", "inline", "test.png")
    @cherrypy.expose
    def video(self,ID):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where ID = {0}".format(ID))
        rows = cur.fetchall()
        for i in rows:
            v = 'c:/src/html/platform/video/'
            out = i[0]
            out = v + out
        return serve_file(out, "video/mp4", "inline", "test.mp4")
    @cherrypy.expose
    def music(self,ID):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where ID = {0}".format(ID))
        rows = cur.fetchall()
        for i in rows:
            v = 'c:/src/html/platform/music/'
            out = i[0]
            out = v + out
        return serve_file(out, "audio/mp3", "inline", "test.mp3")
    @cherrypy.expose
    def audiobook(self,ID):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where ID = {0}".format(ID))
        rows = cur.fetchall()
        for i in rows:
            v = 'c:/src/html/platform/audiobook/'
            out = i[0]
            out = v + out
        return serve_file(out, "audio/mp3", "inline", "test.mp3")
    @cherrypy.expose
    def uploadaudio(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        with open("uploads/uploadaudio.html") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)
    @cherrypy.expose
    def uploadscreenshote(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        with open("uploads/uploadscreenshote.html") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)
    @cherrypy.expose
    def uploadimg(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        with open("uploads/uploadimg.html") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)
    @cherrypy.expose
    def uploadmusic(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        with open("uploads/uploadmusic.html") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)
    @cherrypy.expose
    def uploadvideo(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        with open("uploads/uploadvideo.html") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)
    @cherrypy.expose
    def musics(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where Type = 'music'")
        ro1 = cur.fetchall()
        with open("sites/musics.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,mess=ro1,rows=ro1)
    @cherrypy.expose
    def videos(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where Type = 'video'")
        ro1 = cur.fetchall()
        with open("sites/videos.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,mess=ro1,rows=ro1)
    @cherrypy.expose
    def audiobooks(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where Type = 'audio'")
        ro1 = cur.fetchall()
        with open("sites/audiobooks.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,mess=ro1,rows=ro1)
    @cherrypy.expose
    def imgs(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where Type = 'img'")
        ro1 = cur.fetchall()
        with open("sites/imgs.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,mess=ro1,rows=ro1)
    @cherrypy.expose
    def screenshotes(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where Type = 'screenshote'")
        ro1 = cur.fetchall()
        with open("sites/screenshotes.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,mess=ro1,rows=ro1)
    @cherrypy.expose
    def watchvideo(self,MYIDIN,ID):
        MYID = MYIDIN
        with open("watch/watchvideo.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,idvideo=ID)
    @cherrypy.expose
    def watchaudiobook(self,MYIDIN,ID):
        MYID = MYIDIN
        with open("watch/watchaudiobook.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,idaudio=ID)
    @cherrypy.expose
    def watchmusic(self,MYIDIN,ID):
        MYID = MYIDIN
        with open("watch/watchmusic.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,idmusic=ID)
    @cherrypy.expose
    def watchscreenshote(self,MYIDIN,ID):
        MYID = ID
        with open("watch/watchscreenshotes.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,idscreenshote=ID)
    @cherrypy.expose
    def watchimg(self,MYIDIN,ID):
        MYID = ID
        with open("watch/watchimg.html","r") as file:
           html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,idimg=ID)
    @cherrypy.expose
    def stylecss(self):
        return serve_file(cmd+"/style.css", "text/css", "inline", "test.css")
if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())