function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        //Bom dia
        img.src = 'images/fotomanha.jpg'
        document.body.style.background = '#e2cd9f'
    } else if (hora >= 12 && hora < 18) {
        //Boa tarde
        img.src = 'images/fototarde.jpg'
        document.body.style.background = '#6f98b9'
    } else {
        //Boa noite
        img.src = 'images/fotonoite.jpg'
        document.body.style.background = '#515154'
    }
}