from pelis import Pagina,Pagina_pelicula,Pagina_pelis,Pelicula
from peliculas import peliculas
from flask import Flask
app = Flask(__name__)

pelis=Pagina_pelis()
for p in peliculas:
    pe = Pelicula(**p)
    pelis.append_peli(pe)

@app.route("/")
def home_www():
	return pelis.pagina_web()

@app.route("/pelicula/<int:codigo>/")
def peli_www(codigo):
    for peli in pelis.peliculas:
        if peli.codigo == codigo:
            break
    else: home_www()
    pag = Pagina_pelicula( peli )
    return pag.pagina_web()

app.run(host="0.0.0.0", port=8080, debug=True)
