var elemento = document.querySelector('h1')
elemento.innerHTML = 'JS';
elemento.style.color = '#00f';
console.log(elemento)

function limpar(event){

    event.preventDefault();
    
    

    document.querySelector('form').reset();
    console.log('Limpando....');
}