function contar() {
    let inicio = document.getElementById('txtinicio').value
    let fim = document.getElementById('txtfim').value
    let passo = document.getElementById('txtpasso').value
    let res = document.getElementById('res')

    if (inicio == '' || fim == '' || passo == '') {
        res.innerHTML = 'ERRO: Impossível contar!'
        alert('Por favor, preencha todos os campos!')
    } else {
        if (passo <= 0) {
            alert('Passo inválido! Considerando PASSO 1')
            passo = 1
        }
        res.innerHTML = 'Contando: <br>'
        let i = Number(inicio)
        let f = Number(fim)
        let p = Number(passo)
        if (i < f) {
            // Contagem crescente
            for (let c = i; c <= f; c += p) {
                res.innerHTML += ` ${c} \u{1F449}`
            }
        } else {
            // Contagem decrescente
            for (let c = i; c >= f; c -= p) {
                res.innerHTML += ` ${c} \u{1F449}`
            }
        }
        res.innerHTML += `\u{1F3C1}`
    }
}