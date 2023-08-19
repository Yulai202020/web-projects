import os,dataa,random,sqlite3,jinja2,cherrypy
from cherrypy.lib.static import serve_file

cmd=os.getcwd()

def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size

MYID = ""
cherrypy.config.update({
    'server.socket_host':'127.1.1.1',
    'server.socket_port':1000,
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
    def view(self,ID,idfile):
        MYID = ID
        idfile=idfile
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT herf From files where IDPK = "+idfile)
        ros = cur.fetchall()
        res = ""
        for i in ros:
            i = ros[0]
            for f in i:
                res = i[0]
        with open(res,"rb") as file:
            weight = len(file.read())
            weight = convert_bytes(weight)
        res+=" "
        with open("sites/view.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(idfile=idfile,weight=weight,ID=MYID)

    @cherrypy.expose
    def index(self,ID):
        MYID = ID
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)

    @cherrypy.expose
    def upgrade(self,ID):
        MYID = ID
        with open("main/upgrade.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)

    @cherrypy.expose
    def home(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From files where ID = \'"+MYID+"\'")
        ros = cur.fetchall()
        with open("main/home.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        byt = getFolderSize(MYID)
        procent=0
        byt = int(byt)
        if byt == 0:
            procent=100//(dataa.gbused["gb1"] / 1)
        return tmpl.render(names=ros,byt=convert_bytes(byt),total=dataa.gbused["gb2"],procent=procent,ID=MYID)

    @cherrypy.expose
    def uploadfiles(self,ID):
        MYID = ID
        conn = sqlite3.connect("data.db")
        with open("main/uploadfiles.html") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render(ID=MYID)

class returns(object):

    @cherrypy.expose
    def setusedgb(self,type,ID):
        MYID = ID
        if type == 128:
            dataa.gbused["gb1"]=128
            dataa.gbused["gb2"]=137438883103
        elif type == 1024:
            dataa.gbused["gb1"]=1024
            dataa.gbused["gb2"]=1099511992568
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
            conn.executescript("insert into Accaunts(\"Email\",\"Pass\",\"ID\") values ('{0}','{1}','{2}')".format(email,password,id))
        MYID = id
        os.mkdir(str(MYID))
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)

    @cherrypy.expose
    def write(self,ufile,ID):
        MYID = ID
        upload_path = os.path.dirname(__file__)
        upload_path = MYID+'\\'+ufile.filename
        upload_file = os.path.normpath(os.path.join(upload_path))
        with open(upload_file, 'wb') as out:
            while True:
                data = ufile.file.read(8192)
                if not data:
                    break
                out.write(data)
        with sqlite3.connect("data.db") as conn:
            conn.executescript("insert into files(\"herf\",\"name\",\"ID\") values ('{0}','{1}','{2}')".format(upload_path,ufile.filename,MYID))
        raise cherrypy.HTTPRedirect("/home?ID="+MYID)

    @cherrypy.expose
    def files(self,ID):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT * From Files where IDPK = {0}".format(ID))
        pyth = cur.fetchall()
        pythor=""
        for i in pyth:
            i = pyth[0]
            for pythor in i:
                pythor = i[1]
        return serve_file(cmd +"\\"+ str(pythor))

class files(object):
    @cherrypy.expose
    def stylemincss(self):
        return serve_file(cmd+"\\style.min.css", "text/css", "inline", "test.css")

if __name__ == '__main__':
    cherrypy.tree.mount(home())
    cherrypy.tree.mount(files(), '/files')
    cherrypy.tree.mount(user(), '/user')
    cherrypy.tree.mount(returns(), '/return')

    cherrypy.engine.start()
    cherrypy.engine.block()