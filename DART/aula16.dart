void main() {
  Pessoa pessoa1 = Pessoa('Daves', 30, '11987654321');
  pessoa1.apresenta();

  Pessoa pessoa2 = Pessoa('João', 40, '21987656764');
  pessoa2.apresenta();
}

class Pessoa {
  // Propriedades da Classe = Variáveis
  String nome = '';
  int idade = 0;
  String telefone = '';

  Pessoa(this.nome, this.idade, this.telefone);

  // Métodos da Classe = Funções

  void apresenta() {
    print(
      'Meu nome é ${this.nome}, tenho $idade anos e meu telefone é $telefone',
    );
  }
}
