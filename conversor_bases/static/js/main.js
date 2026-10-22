function solicitarConversao(baseOrigem, idInput, nomeBase) {
    const valor = document.getElementById(idInput).value;

    if (!valor.trim()) {
        alert("Por favor, digite um valor antes de converter.");
        return;
    }

    fetch('/api/converter', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            valor: valor,
            base_origem: baseOrigem
        })
    })
    .then(response => response.json())
    .then(dados => {
        const modalCorpo = document.getElementById('modalCorpo');
        const modalTitulo = document.getElementById('modalTitulo');

        modalTitulo.innerText = `Conversão a partir de: ${nomeBase} (${valor})`;

        if (dados.sucesso) {
            modalCorpo.innerHTML = `
                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <strong>Decimal:</strong> <span>${dados.decimal}</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <strong>Binário:</strong> <span>${dados.binario}</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <strong>Hexadecimal:</strong> <span>${dados.hexadecimal}</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <strong>Octal:</strong> <span>${dados.octal}</span>
                    </li>
                </ul>
            `;
        } else {
            modalCorpo.innerHTML = `
                <div class="alert alert-danger" role="alert">
                    <strong>Erro de Validação:</strong> ${dados.erro}
                </div>
            `;
        }

        const modalEl = new bootstrap.Modal(document.getElementById('modalResultado'));
        modalEl.show();
    })
    .catch(error => {
        console.error('Erro na requisição:', error);
    });
}
