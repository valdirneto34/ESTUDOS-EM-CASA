void main() {
  //Personagem personagem1 = Personagem(10, 10, 'Hero');

  Jogador jogador1 = Jogador(10, 10, 'Hero 2');
  Inimigo inimigo1 = Inimigo(6, 10, 'Inimigo 1');
  jogador1.mostra();
  inimigo1.mostra();

  if (inimigo1.getPosicaoX() == jogador1.getPosicaoX()) {
    print('Luta');
  }

  jogador1.luta();
  inimigo1.luta();
}

abstract class Personagem {
  int posicaoX = 0;
  int posicaoY = 0;
  String nome;

  Personagem(this.posicaoX, this.posicaoY, this.nome);

  void mostra() {
    print('$nome está na posição $posicaoX e $posicaoY');
  }

  int getPosicaoX() => posicaoX;

  int getPosicaoY() => posicaoY;

  void luta() {}
}

class Jogador extends Personagem {
  Jogador(int posicaoX, int posicaoY, String nome)
    : super(posicaoX, posicaoY, nome);

  @override
  void luta() {
    print('Lutando...');
  }
}

class Inimigo extends Personagem {
  Inimigo(int posicaoX, int posicaoY, String nome)
    : super(posicaoX, posicaoY, nome);
}
