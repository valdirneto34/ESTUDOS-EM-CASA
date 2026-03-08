let num = document.getElementById('num')
let lista = document.getElementById('lista')
let res = document.getElementById('res')
let valores = []

function adicionar() {
    n = Number(num.value)
    if (n < 1 || n > 100 || valores.indexOf(n) != -1) {
        alert('Número inválido ou já adicionado!')
    } else {
        res.innerHTML = ''
        valores.push(n)
        let option = document.createElement('option')
        option.value = n
        option.textContent = `Valor ${n} adicionado.`
        lista.appendChild(option)
    }
    num.value = ''
    num.focus()
}

function finalizar() {
    if (valores.length == 0) {
        alert('Adicione valores antes de finalizar!')
    } else {
        res.innerHTML = `<p>Ao todo, temos ${valores.length} números cadastrados.</p>`
        res.innerHTML += `<p>O maior valor informado foi ${Math.max(...valores)}.</p>`
        res.innerHTML += `<p>O menor valor informado foi ${Math.min(...valores)}.</p>`
        let soma = valores.reduce((a, b) => a + b, 0)
        res.innerHTML += `<p>Somando todos os valores, temos ${soma}.</p>`
        res.innerHTML += `<p>A média dos valores digitados é ${soma / valores.length}.</p>`
    }

}
