void main() {
  Pessoa pessoa1 = Pessoa('Daves', 30, telefone: '11987654321');

  print(pessoa1.idade);
}

class Pessoa {
  // Propriedades da Classe = Variáveis
  String nome = '';
  int _idade = 0;
  String telefone = '';

  Pessoa(this.nome, int parametroIdade, {this.telefone = ''}) {
    this.idade = parametroIdade;
  }

  void set idade(int idade) {
    if (idade < 120) {
      this._idade = idade;
    }
  }

  int get idade {
    return this._idade;
  }

  // Métodos da Classe = Funções
  void apresenta() {
    print('Meu nome é ${this.nome}, tenho $idade anos');
  }
}
