void main() {
  /*
  List<String> = [];
  
  KEY  VALUE
   0   João
   1   Maria
   */

  Map<int, String> numeros = Map();

  numeros[1] = 'Um';
  numeros[2] = 'Dois';
  numeros[3] = 'Três';
  numeros[100] = 'Cem';

  Map<String, String> estados = Map();
  estados['SP'] = 'São Paulo';
  estados['RJ'] = 'Rio de Janeiro';

  print(estados.keys);
  print(estados.values);

  estados.forEach((String sigla, String estado) {
    print('$estado - $sigla');
  });
}
