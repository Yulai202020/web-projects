import jinja2 , cherrypy , os
from cherrypy.lib.static import serve_file

cmd=os.getcwd()

class home(object):
    @cherrypy.expose
    def infoofsegos(self):
        with open("html/infoofsegos.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render()
    @cherrypy.expose
    def home(self):
        with open("html/home.html","r") as file:
            html = file.read()
        tmpl = jinja2.Template(html)
        return tmpl.render()

class files(object):
    @cherrypy.expose
    def kubgame(self):
        return serve_file(cmd+"\\appsinstall\\kubgame.py", "python/txt", "inline", "kubgame.py")
    @cherrypy.expose
    def calculatorapp(self):
        return serve_file(cmd+"\\appsinstall\\calculatorapp.py", "python/txt", "inline", "calculatorapp.py")
    @cherrypy.expose
    def infoapp(self):
        return serve_file(cmd+"\\appsinstall\\infoapp.py", "python/txt", "inline", "infoapp.py")
    @cherrypy.expose
    def guessgame(self):
        return serve_file(cmd+"\\appsinstall\\guessgame.py", "python/txt", "inline", "guessgame.py")
    @cherrypy.expose
    def pinneygame(self):
        return serve_file(cmd+"\\appsinstall\\pinneygame.py", "python/txt", "inline", "pinneygame.py")
    @cherrypy.expose
    def stylemincss(self):
        return serve_file(cmd+"\\style.min.css", "text/css", "inline", "test.css")

class update(object):
    @cherrypy.expose
    def UpdateData(self):
        return serve_file(cmd+"\\OSupdate\\datads.py", "python/txt", "inline", "datads.py")
    @cherrypy.expose
    def UpdateOS(self):
        return serve_file(cmd+"\\OSupdate\\segos.py", "python/txt", "inline", "segos.py")
    @cherrypy.expose
    def UpdateSettingsData(self):
        return serve_file(cmd+"\\OSupdate\\settingsdata.py", "python/txt", "inline", "settingsdata.py")

if __name__ == '__main__':
    cherrypy.tree.mount(files(), '/files')
    cherrypy.tree.mount(update(), '/OS')
    cherrypy.tree.mount(home())
    cherrypy.engine.start()
    cherrypy.engine.block()