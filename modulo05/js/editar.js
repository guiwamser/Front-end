function carregalocalstorage(){
    return JSON.parse(localStorage.getItem('Alunos'))
};

function limpar(event){
    event.preventDefault();
    document.querySelector('form').reset();
    console.log('Limpando....');
};

function editar(event){
    event.preventDefault();
    console.log('salvando....');

    var id = document.getElementsByName('id')[0].value;
    var name = document.getElementsByName('nome')[0].value;
    var doc_people = document.getElementsByName('cpf')[0].value;
    var year = document.getElementsByName('idade')[0].value;

    var Aluno = {
        'id': id,
        'nome': name,
        'cpf': doc_people,
        'idade': year
};

var lista = carregalocalstorage();
var novaLista = [];

lista.forEach(e => {
    if(e['id'] != id){
        novaLista.push(e);
    }
    else{
        novaLista.push(Aluno);
    }
    
});
localStorage.setItem('Alunos', JSON.stringify(novaLista));
alert('Editado com Sucesso...'),

limpar(event);    
};

function carregaCampos(dado){
    document.getElementsByName('id')[0].value = dado['id'];
    document.getElementsByName('nome')[0].value = dado['nome'];
    document.getElementsByName('cpf')[0].value = dado['cpf'];
    document.getElementsByName('idade')[0].value = dado['idade'];
};

function carregadados(){
    var urlParametros = new URLSearchParams(window.location.search);

    var id = parseInt =(urlParametros.get('id'));

    var alunos = JSON.parse(localStorage.getItem('Alunos'));
    
    alunos.forEach(e =>{
        if(e['id'] == id){
            carregaCampos(e);
        }
    });
};
window.onload = carregadados();