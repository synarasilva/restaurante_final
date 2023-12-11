document.addEventListener('DOMContentLoaded', function() {
    // Faz uma requisição para a rota que retorna os dados
    fetch('/obter_reservas')
        .then(response => response.json())
        .then(data => {
            // Exibe os dados na tabela
            var tabela = document.getElementById('listaDados');
            var tbody = tabela.querySelector('tbody');
            tbody.innerHTML = '';  // Limpa os dados antigos

            data.reservas.forEach(function(dado) {
                var row = document.createElement('tr');
                row.innerHTML = `
                    <td>${dado.nome}</td>
                    <td>${dado.Data}</td>
                    <td>${dado.Mesa}</td>
                    <td><a href="#" class="btn btn-info">Editar</a></td>
                    <td><a href="#" class="btn btn-danger">Excluir</a></td>
                `;
                tbody.appendChild(row);
            });
        })
        .catch(error => console.error('Erro:', error));
});
