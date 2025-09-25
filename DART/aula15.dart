void main() {
  Pessoa pessoa1 = Pessoa();

  pessoa1.nome = 'Daves';
  pessoa1.idade = 30;
  pessoa1.telefone = '11987654321';

  //print(pessoa1.nome);
  pessoa1.apresenta();
}

class Pessoa {
  // Propriedades da Classe = Variáveis
  String nome = '';
  int idade = 0;
  String telefone = '';

  // Métodos da Classe = Funções

  void apresenta() {
    print('Meu nome é ${this.nome}');
  }
}
