void main() {
  Pessoa pessoa1 = Pessoa('João', 30);
  pessoa1.apresenta();

  Pai pai1 = Pai('José', 35, 'Carpinteiro');
  pai1.apresenta();

  Filho filho1 = Filho('Pedro', 12, 'Escola da Prefeitura');
  filho1.apresenta();
}

class Pessoa {
  String nome = '';
  int idade = 20;

  Pessoa(this.nome, this.idade);

  void apresenta() {
    print('Meu nome é $nome e minha idade é $idade anos');
  }
}

class Pai extends Pessoa {
  String profissao = '';
  Pai(nome, idade, this.profissao) : super(nome, idade);

  @override
  void apresenta() {
    print(
      'Meu nome é $nome e minha idade é $idade anos e minha profissão é $profissao',
    );
  }
}

class Filho extends Pai {
  String escola = '';
  Filho(nome, idade, this.escola) : super(nome, idade, '');

  @override
  void apresenta() {
    print(
      'Meu nome é $nome e minha idade é $idade anos e estudo na escola $escola',
    );
  }
}
