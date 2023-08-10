#include <stdio.h>
#define MAX 100

void LeMatriz(int n, int m, int M[MAX][MAX]) {
    
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < m; ++col) {
            scanf("%d ", &M[row][col]);
        }
    }
}

int ContaLinhasNulas(int n, int m, int M[MAX][MAX]) {
    int rowCount = 0, total = 0;
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < m; ++col) {
            total += M[row][col];
        }
        if (total == 0) rowCount++;
        total = 0;
    }
    return rowCount;
}

int ContaColunasNulas(int n, int m, int M[MAX][MAX]. int &colCount) {
    for (int col = 0; col < m; ++col) {
        for (int row = 0; row < n; ++row) {
            total += M[row][col];
        }
        if (total == 0) colCount++;
        total = 0;
    }
    return colCount;
}

int main() {
    int n, m, M[MAX][MAX], rowCount = 0, colCount = 0, total = 0;
        scanf("%d %d", &n, &m);
            M[MAX][MAX] = LeMatriz();
                rowCount = ContaLinhasNulas(n, m, M[MAX][MAX]);
                colCount = ContaLinhasNulas(n, m, M[MAX][MAX], colCount);
                
        printf("%d %d", rowCount, colCount);
        
    return 0;
    
}
