//criei uma variavel chamada elemento 
//document acessa o documento html que esta sendo chamado o script
//query selector e um methodo interno do javaScript que nos retorna um elemento html 
var elemento = document.querySelector('h1')
//variavel recebendo inner html para incremento ou alteracao descrtivo
elemento.innerHTML += ' JS';
//variavel elemento recebendo estilizacao de cor 
elemento.style.color = '#blue';
//console log e o nosso print retorno variavel
console.log(elemento);

function limpar(event){
    event.preventDefault();
    document.querySelector('form').reset();
    console.log('Limpando....');
}

function salvar(event){
    event.preventDefault();
    console.log('salvando....');
    
    var name = document.getElementsByName('nome')[0].value;
    var doc_people = document.getElementsByName('cpf')[0].value;
    var year = document.getElementsByName('idade')[0].value;

    var listaAlunos = JSON.parse(localStorage.getItem('Alunos'));

    if(listaAlunos == null){
        listaAlunos = [];
    }
    
    var id = JSON.parse(localStorage.getItem('IdAluno'));
    if(listaAlunos == null){
        id = 0;
    }
    id = id +1;

    var Aluno = {
                    'id': id,
                    'nome': name,
                    'cpf': doc_people,
                    'idade': year
        };listaAlunos.push(Aluno);

    
    localStorage.setItem('IdAluno', JSON.stringify(id));    
    localStorage.setItem('Alunos', JSON.stringify(listaAlunos));
    limpar(event)
}

document.getElementById('salvar').addEventListener('click', salvar)