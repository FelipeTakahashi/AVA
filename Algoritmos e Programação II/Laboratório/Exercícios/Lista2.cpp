/*#include <iostream>

void Imprime() {
    int i = 0, counter = 0;
        while (counter < 100) {
            std::cout << i << " ";
            counter++;
            i += 3;
        }
}

int main() {
    int counter = 0, i = 0;
        while (counter < 100) { // Imprime();
            std::cout << i << " ";
            counter++;
            i += 3;
        }
    std::cout << std::endl << counter;
    
    return 0;
}

#include <iostream>
#include <string>
#include <iomanip> 

int LeValor() {
    int n;
        std::cin >> n;
    return n;
}

int UltimoDigito(int n) {
    return n % 10;
}

int AtualizaValor(int n) {
    return n / 10;
}

void LeValorDois(int &n) {
     // return;
}

void UltimoDigitoDois

int main() {
    int n, counter = 0, pCounter = 0, pSum = 0;
        std::cin >> n;
        
    while (n) {
        int digit = n % 10;
            if (digit % 2 == 0) {
                pCounter++;
                pSum++;
            }
        counter++;
        n /= 10;
    }
    
    cout << "dígitos foram o número informado\n";
    
    if (pCounter) std::cout << "Média dos dígitos pares existentes: " << std::setprecision(2) << pSum/pCounter << std::endl;
    
    else std::cout << "Não existem dígitos pares no número informado"
    
    return 0;
}

#include <iostream>
#define MAX 100

int n, M[MAX][MAX], mSum, sSum;

int LeDimensao() {
    std::cin >> n;
        return n;
}

void LeMatriz(int n, int M[MAX][MAX]) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            std::cin << M[i][j];
        }
    }
    return M[MAX][MAX];
}

void SomaDPrincipal(int M[MAX][MAX], int n) {
    int mSum = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if (i == j) mSum += M[i][j];
        }
    }
    return mSum;
}

void SomaDSecundaria(int n, int M[MAX][MAX){
    int sSum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i+j == n+1) sSum += M[i][j];     
        }
    }
    std::cout << sSum << std::endl;
}

void ImprimeMatriz(int n, int M[MAX][MAX]) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            std::cout << M[i][j]; // Não tem espaçamento
        }
    }
}

void ImprimeSomas(int n, M[MAX][MAX]) {
    std::cout << SomaDPrincipal() << std::endl;
    SomaDSecundaria();
}

int main() {
    
}*/
