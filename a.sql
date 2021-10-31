select Cliente.nombre,Cliente.apellido,sum(Arriendo.total),count(Arriendo.total) from Cliente inner join Arriendo on Arriendo.codCliente = Cliente.codCliente;



select Director.nombre,Director.apellido,,count(Pelicula.titulo) from Director inner join PELICULA on Director.codDr = PELICULA.codDirector;
