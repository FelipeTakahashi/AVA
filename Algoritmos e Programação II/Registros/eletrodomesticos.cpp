#include <stdio.h>
#define MAXL 15

using namespace std;

struct {
    char name[MAXL+1];
    double power, time;
} products[5];

int main() {
    
    for (int i = 0; i < 5; ++i) {
        scanf("%s %lf %lf", products[i].name, &products[i].power ,&products[i].time);
    }    
    
    int days;
        scanf("%d", &days);
    
    double totalWasted = 0;
    for (int i = 0; i < 5; ++i) {        
        totalWasted += (products[i].time * days * products[i].power);
    }   
    
    printf("%.2lf\n", totalWasted);
    for (int i = 0; i < 5; ++i) {
        double ans;
            ans = (products[i].time * days * products[i].power * 100)/totalWasted;
        printf("%.2lf\n", ans);
    }
    return 0;  
}
