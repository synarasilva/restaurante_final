document.addEventListener('DOMContentLoaded', function() {
    // Obtém os dados do armazenamento local
    var dadosArmazenados = JSON.parse(localStorage.getItem('dados')) || [];

    // Exibe os dados na lista
    var listaDados = document.getElementById('listaDados');
    dadosArmazenados.forEach(function(dado) {
        var listItem = document.createElement('li');
        listItem.innerHTML = `<strong>Usuário:</strong> ${dado.usuario}, <strong>Email:</strong> ${dado.email}, <strong>Dúvida:</strong> ${dado.duvida}`;
        listaDados.appendChild(listItem);
    });
});
