document.addEventListener('DOMContentLoaded', function() {
    // Adiciona um event listener para todos os botões de mesa
    var botoesMesa = document.querySelectorAll('.botaoMesa');
    botoesMesa.forEach(function(botao) {
      botao.addEventListener('click', function() {
        // Adiciona a classe 'clicked' para alterar a cor no CSS
        this.classList.add('clicked');

        // Encontra o elemento pai 'category-card'
        var categoryCard = this.closest('.category-card');

        // Modifica o texto da div, substituindo o conteúdo anterior
        categoryCard.querySelector('.fw-bold').innerHTML = '<div class="fw-bold">Mesa reservada</div>';

        // Exibe um alerta
        alert('Mesa reservada com sucesso!');
      });
    });
  });
