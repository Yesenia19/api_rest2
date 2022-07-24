import web
urls=(
    "/",  "index",
    "/crear_usuario",     "crearUsuario",
)

app = web.application(urls, globals())
render = web.template.render("templates/")



           
if __name__ == "__main__":
    app.run()
