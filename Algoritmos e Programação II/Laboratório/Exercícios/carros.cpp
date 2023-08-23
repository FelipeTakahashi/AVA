#include <stdio.h>
#define MAXNAME 15
#define MAXSIZE 30

using namespace std;

struct Cars {
    char BRAND[MAXNAME];
    int YEAR;
    double PRICE;
}cars[MAXSIZE];

void setData(Cars cars[MAXSIZE], int n) {
    for (int i = 0; i < n; i++) {
        scanf("%s %d %lf", cars[i].BRAND, &cars[i].YEAR, &cars[i].PRICE);
    }
    return;
}

void getData(Cars cars[MAXSIZE], int n) {
    for (int i = 0; i < n; i++) {
        printf("Marca: %s\nAno: %d\nPreço: %lf", cars[i].BRAND, cars[i].YEAR, cars[i].PRICE);
    }
    return;
}

double getAverage(Cars cars[MAXSIZE], int n, int year) {
    double sum = 0; int carsThatYear = 0;
    for (int i = 0; i < n; i++) {
        if (cars[i].YEAR == year) {
            sum += cars[i].PRICE;
            carsThatYear++;
        }
    }
    return sum/carsThatYear;
}

void menu() {
  printf("\n[1] Cadastrar um carro\n");
	printf("[2] Listar carros\n");
	printf("[3] Media de precos de um ano\n");
	printf("Opcao: ");
}

int main() {
    int opt, year, n;
      printf("Quantos carros serão registrados: ");
      scanf("%d", &n)
    do {
        menu();
        scanf("%d", &opt);

        if(opt == 1) setData(cars, n);
        else if (opt == 2) getData(cars, n);
        else if (opt == 3) {
            printf("Insira o ano: ")
            scanf("%d", &year);
            print("%.2lf", getAverage(cars, n, year));
        }
    }while (0 < opt && opt < 4);

    return 0;

}
