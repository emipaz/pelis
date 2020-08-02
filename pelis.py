class Pelicula:
    def __init__(self, titulo ,  director,  year,  protagonistas , portada , codigo):
        self.titulo        = titulo
        self.director      = director
        self.protagonistas = protagonistas
        self.portada       = portada
        self.year          = year
        self.codigo        = codigo

class Pagina:
    
    def __init__(self,titulo):
        self.titulo = titulo
    
    def mostrtar_titulo(self):
        return self.titulo
    
    def pagina_web(self):
        return f"""<!DOCTYPE html><html><meta charset='UTF-8'>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
        <title>{self.titulo}</title>"""

class Pagina_pelis(Pagina):
    
    def __init__(self , titulo = "lista de peliculas" ):
        Pagina.__init__(self,titulo)
        self.peliculas = []
    
    def append_peli(self,peli):
        self.peliculas.append(peli)
    
    def pagina_web(self):
        st="<ul class='list-group'>"
        for peli in self.peliculas:
            st += f"<li class='list-group-item'><a href=pelicula/{peli.codigo}>{peli.titulo}</a></li>"
        st +="</ul></br><a href='/'>Volver al inicio</a> </html>"
        return Pagina.pagina_web(self) + st

class Pagina_pelicula(Pagina):
    
    def __init__(self , pelicula):
        Pagina.__init__(self,pelicula.titulo)
        #self.titulo = pelicula.titulo
        self.datos  = pelicula
    
    def pagina_web(self):
        st = f"""<ul class='list-group'><h1>{self.datos.titulo} del año {self.datos.year}</h1>
                <img style="width:500px; height:500px;" src={self.datos.portada}>
                <h2>Director :</h2><h1>{self.datos.director}</h1><h2>Protagonistas :</h2><ul class='list-group'>
                <li class='list-group-item'>"""
        for dato in self.datos.protagonistas:
            st += f"<li class='list-group-item'>{dato}</li>"
        return Pagina.pagina_web(self) + st +  "</ul></br><a href='/'>Volver al inicio</a> </html>"
