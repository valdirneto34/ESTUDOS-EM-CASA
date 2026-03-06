let num = [0, 3, 2, 1, 4]
num[5] = 6 // Adiciona um elemento na posição 5 do vetor
num.push(7) // Adiciona um elemento no final do vetor
console.log(`O tamanho do vetor é ${num.length}.`) // Retorna o tamanho do vetor
console.log(`Nosso vetor é o ${num}`)
console.log(`O primeiro elemento do vetor é ${num[0]}.`) // Retorna o primeiro elemento do vetor
num.sort() // Ordena o vetor

console.log(`Nosso vetor é o ${num}`)

for (let pos in num) {
    console.log(`A posição ${pos} tem o valor ${num[pos]}.`)
}
console.log(`O vetor tem o valor 3? ${num.indexOf(3)}`) // Retorna a posição do elemento 3 no vetor, ou -1 se não encontrar
console.log(`O vetor tem o valor 100? ${num.indexOf(100)}`) // Retorna a posição do elemento 100 no vetor, ou -1 se não encontrar