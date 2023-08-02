#include <cstdio>
int numero, ultimo_digito, novo_num, penultimo_digito, soma;

using namespace std;

int main() {
    
    printf("Digite um número inteiro: ");
    scanf("%d", &numero);
    
    ultimo_digito = numero%10;
    novo_num = numero/10;
    penultimo_digito = novo_num%10;
    soma = ultimo_digito + penultimo_digito;
    
    printf("A soma dos dois últimos dígitos do número %d", numero);
    printf(" é: %d\n", soma);
       
}
