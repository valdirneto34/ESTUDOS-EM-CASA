function gerarTabuada() {
    let numero = document.getElementById('txtnumero').value
    let tabuada = document.getElementById('seltabuada')
    tabuada.innerHTML = ''
    
    if (numero == '') {
        alert('Por favor, digite um número!')
        let item = document.createElement('option')
        item.text = 'Digite um número acima'
        item.value = 'option'
        tabuada.appendChild(item)
        return
    }
    
    let n = Number(numero)
    for (let c = 1; c <= 10; c++) {
        let item = document.createElement('option')
        item.text = `${n} x ${c} = ${n * c}`
        item.value = `tab${c}`
        tabuada.appendChild(item)
    }
}