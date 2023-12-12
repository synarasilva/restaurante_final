$(document).ready(function () {
    // Função para calcular o total da compra
    function calcularTotal() {
        var total = 0;
        $('.table tbody tr').each(function () {
            var precoUnitario = parseFloat($(this).find('td:eq(1)').text().replace('R$', ''));
            var quantidade = parseInt($(this).find('.qty span').text());
            var subtotal = precoUnitario * quantidade;
            total += subtotal;
            $(this).find('td:eq(3)').text('R$' + subtotal.toFixed(2));
        });
        $('#footer span:contains("Total")').text('R$' + total.toFixed(2));
    }

    // Adiciona um produto ao carrinho
    $('#button').on('click', function () {
        // Adapte isso para obter as informações reais do produto
        var nomeProduto = "Nome do Produto";
        var precoProduto = 120;

        var newRow = '<tr>' +
            '<td><div class="product"><div class="info"><div class="name">' + nomeProduto + '</div></div></div></td>' +
            '<td>R$' + precoProduto + '</td>' +
            '<td><div class="qty"><button><i class="bx bx-minus"></i></button><span>1</span><button><i class="bx bx-plus"></i></button></div></td>' +
            '<td>R$' + precoProduto + '</td>' +
            '<th><button class="remove"><i class="bx bx-x"></i></button></th>' +
            '</tr>';
        $('#table tbody').append(newRow);
        calcularTotal();
    });

    // Remove um produto do carrinho
    $(document).on('click', '.remove', function () {
        $(this).closest('tr').remove();
        calcularTotal();
    });

    // Atualiza a quantidade e recalcula o total ao clicar nos botões de +/- na quantidade
    $(document).on('click', '.qty button', function () {
        var spanQuantidade = $(this).siblings('span');
        var quantidade = parseInt(spanQuantidade.text());

        if ($(this).hasClass('bx-minus') && quantidade > 1) {
            quantidade--;
        } else if ($(this).hasClass('bx-plus')) {
            quantidade++;
        }

        spanQuantidade.text(quantidade);
        calcularTotal();
    });

    // Inicializa o total ao carregar a página
    calcularTotal();
});
