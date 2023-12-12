function incrementarQuantidade(button) {
    var row = button.closest('tr');
    var spanQuantidade = row.querySelector('.quantidade');
    var quantidade = parseInt(spanQuantidade.textContent);

    quantidade++;
    spanQuantidade.textContent = quantidade;

    atualizarSubtotal(row);
    calcularTotal();
}

function decrementarQuantidade(button) {
    var row = button.closest('tr');
    var spanQuantidade = row.querySelector('.quantidade');
    var quantidade = parseInt(spanQuantidade.textContent);

    if (quantidade > 1) {
        quantidade--;
        spanQuantidade.textContent = quantidade;

        atualizarSubtotal(row);
        calcularTotal();
    }
}

function atualizarSubtotal(row) {
    var precoUnitario = parseFloat(row.querySelector('td:eq(1)').textContent.replace('R$', ''));
    var quantidade = parseInt(row.querySelector('.quantidade').textContent);
    var subtotal = precoUnitario * quantidade;

    row.querySelector('.subtotal').textContent = 'R$' + subtotal.toFixed(2);
}

function calcularTotal() {
    var total = 0;
    var linhas = document.querySelectorAll('#table tbody tr');
    linhas.forEach(function (row) {
        var subtotal = parseFloat(row.querySelector('.subtotal').textContent.replace('R$', ''));
        total += subtotal;
    });

    document.getElementById('sub-total').textContent = 'R$' + total.toFixed(2);
    // Adicione aqui a lógica para calcular o frete e atualizar o total
    var totalComFrete = total; // Exemplo: apenas o total sem frete
    document.getElementById('total').textContent = 'R$' + totalComFrete.toFixed(2);
}
