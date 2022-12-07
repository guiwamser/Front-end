function carregalocalstorage(){
    return JSON.parse(localStorage.getItem('Alunos'))
};

function carregarEditar(event, id){
    console.log('Evento de click', event);
    event.preventdefault();
    carregarEditar(id)

};

function carregar(){
    console.log('Carregando janela');
    var tbody = document.querySelector('tbody');
    tbody.innerHTML = ''

    var alunos = localStorage.getItem('Alunos');

    alunos = JSON.parse(alunos);
    
    alunos.forEach((e) =>{
    var tr = `<tr>
                    <td>${e['id']}</td>
                    <td>${e['nome']}</td>
                    <td>${e['cpf']}</td>
                    <td>${e['idade']}</td>
                    <td>
                    <a href="editar.html?id=${e['id']}">editar</a>
                    <button href="" onclick="deletar(${e['id']})">Deletar</button>
                    </td>
                </tr>`

        tbody.innerHTML += tr
        
    });
}
function deletar(id){
    var lista = carregalocalstorage();
    var novalista = [];
    lista.forEach(e => {
        if(e['id'] != id){
            novalista.push(e)
        }
    });
    localStorage.setItem('Alunos', JSON.stringify(novalista));
    carregar();

}


window.onload = carregar