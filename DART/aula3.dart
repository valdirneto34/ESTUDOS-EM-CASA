void main() {
  
  // Produtos
  
  int codigo = 3;
  
  double preco = 3.1415;
  String nome = 'Pendrive'; 
  bool venda = true;
  
  var variavel = 1;
  dynamic variavel2 = 1;
  variavel2 = 'Daves';
  
  print(codigo);
  print(preco);
  print(nome);
  print(venda);
  print(variavel);
  print(variavel2);
  
  
  print( 'Código codigo' );
  print( 'Código $codigo' );
  print( 'Código ${codigo * 2}' );
  
  
  print( 'Produto de código ' + codigo.toString() + ' é ' + nome + ' e o valor do produto em dobro é ' + (preco * 2).toString() );
  
}