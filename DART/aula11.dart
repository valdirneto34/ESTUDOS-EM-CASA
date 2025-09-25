void main() {
  bool condicao = false;
  int i = 1;

  do {
    print(i);
    i++;

    if (i > 5) {
      condicao = false;
    }
  } while (condicao);

  /*
  while(condicao){
    
    print(i);
    i++;
    
    if(i > 5){
      condicao = false;
    }
  }
  */

  /*
  int i = 1;
  
 while(i < 10){
   print(i);
   i++;
 }
 */
}
