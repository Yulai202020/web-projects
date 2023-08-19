import os,random,sqlite3,jinja2,cherrypy
from cherrypy.lib.static import serve_file
cmd=os.getcwd()

MYID = ""
cherrypy.config.update({
    'server.socket_host':'127.9.9.9',
    'server.socket_port':9999,
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
        with open("sites/regis.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render()
   
    @cherrypy.expose
    def regis(self):
        with open("sites/regis.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render()

class home(object):
    @cherrypy.expose
    def viewnewsone(self,ID,idnews):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From News where ID = \'"+idnews+"\'")
        ros = cur.fetchall()
        test = ros[0]
        name = test[0]
        newstext = test[1]
        with open("main/view.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,newstext=newstext,name=name)

    @cherrypy.expose
    def index(self,ID):
        MYID = ID
        raise cherrypy.HTTPRedirect("/homenews?ID="+MYID)

    @cherrypy.expose
    def uploadnews(self,ID):
        MYID=ID
        with open("sites/uploadnews.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)

    @cherrypy.expose
    def homenews(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From News")
        rows = cur.fetchall()
        with open("main/home.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID,rows=rows)

class returns(object):
    @cherrypy.expose
    def write(self,sub,text,ID):
        MYID = ID
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into News(\"Name\",\"Text\") values ('{0}','{1}')".format(sub,text))
        raise cherrypy.HTTPRedirect("/homenews?ID="+MYID)
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
            conn.executescript("insert into Accaunts(\"Email\",\"Pass\",\"ID\") values ('{0}','{1}','{2}')".format(email,password,id))
        MYID = id
        os.mkdir(str(MYID))
        raise cherrypy.HTTPRedirect("/homenews?ID="+MYID)

class files(object):
    @cherrypy.expose
    def stylemincss(self):
        return serve_file(cmd+"\\style.min.css", "text/css", "inline", "test.css")

if __name__ == '__main__':
    cherrypy.tree.mount(home())
    cherrypy.tree.mount(user(), '/user')
    cherrypy.tree.mount(files(), '/files')
    cherrypy.tree.mount(returns(), '/return')
    cherrypy.engine.start()
    cherrypy.engine.block()