function removerRango(lista,indice,indiceFinal){
    lista.splice(indice,indiceFinal-indice+1)
    return lista
}

lista = [20,30,40,50,60,70]

console.log(removerRango(lista,2,4))