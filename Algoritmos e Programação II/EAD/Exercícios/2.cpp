#include <cstdio>

int main() {
    int mat;
    char turma;
    double nota;
        std::scanf("%d %c %lf", &mat, &turma, &nota);
        
        std::printf("O estudante de matrícula %d da turma %c tem nota %.1f", mat, turma, nota);
    return 0;
}
