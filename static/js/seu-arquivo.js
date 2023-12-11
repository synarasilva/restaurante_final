function enviarFormulario() {
    // Aqui você pode adicionar a lógica de envio do formulário, por exemplo, enviar para um servidor backend
    
    // Simulando um envio de formulário assíncrono
    setTimeout(function() {
        // Obtém os dados do formulário
        var usuario = document.getElementById('specificSizeInputGroupUsername').value;
        var data = document.getElementById('specificSizeInputGroupEmail').value;

        // Salva os dados no armazenamento local
        salvarDadosLocal(usuario, data, );

        // Exibe a mensagem de resposta
        document.getElementById('mensagemResposta').innerHTML = 'Sua dúvida será respondida em breve. Aguarde a resposta no seu e-mail.';

        // Limpa os campos do formulário se necessário
        document.getElementById('specificSizeInputGroupUsername').value = '';
        document.getElementById('specificSizeInputGroupdata').value = '';
        document.getElementById('specificSizeInputGroupDoubt').value = '';
    }, 1000); // Tempo de simulação de envio (1 segundo)
}

function salvarDadosLocal(usuario, data) {
    // Obtém os dados existentes do armazenamento local ou inicializa uma lista vazia
    var dadosArmazenados = JSON.parse(localStorage.getItem('dados')) || [];

    // Adiciona os novos dados à lista
    dadosArmazenados.push({
        usuario: usuario,
        data: data,
    });

    // Salva a lista atualizada de volta no armazenamento local
    localStorage.setItem('dados', JSON.stringify(dadosArmazenados));
}

document.getElementById('botaoMesa1').addEventListener('click', function() {
    // Adiciona a classe 'clicked' para alterar a cor no CSS
    this.classList.add('clicked');

    // Modifica o texto da div, substituindo o conteúdo anterior
    document.getElementById('mensagemDiv1').innerHTML = '<div class="fw-bold">Mesa reservada 1</div>'

    // Exibe um alerta
    alert('Mesa reservada com sucesso!');
});



function enviarFormulario() {
    // Aqui você pode adicionar a lógica de envio do formulário, por exemplo, enviar para um servidor backend
    
    // Simulando um envio de formulário assíncrono
    setTimeout(function() {
        // Exibe a mensagem de resposta
        document.getElementById('mensagemResposta').innerHTML = 'Sua dúvida será respondida em breve. Aguarde a resposta no seu e-mail.';
        
        // Limpa os campos do formulário se necessário
        document.getElementById('specificSizeInputGroupUsername').value = '';
        document.getElementById('specificSizeInputGroupdata').value = '';
        document.getElementById('specificSizeInputGroupDoubt').value = '';
    }, 1000); // Tempo de simulação de envio (1 segundo)
}


