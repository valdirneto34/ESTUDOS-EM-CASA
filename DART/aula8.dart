// ignore_for_file: dead_code

void main() {
  bool condicao = false;
  String nome = 'Valdir';
  String clima = 'Sol';

  print(condicao ? 'Condicao Verdadeira' : 'Condicao Falsa');

  print( 2 > 3 ? 'Menor':'Maior ou igual');

  print(nome == 'Daves' ? 'Nome OK':'Nome Errado');

  String cliente = nome == 'Daves' ? 'Nome OK' : 'Nome Errado';
  print(cliente);

  String mensagem = clima == 'Sol'
      ? 'Lindo dia ensolarado'
      : 'Tomara que saia sol';
  print(mensagem);
}
