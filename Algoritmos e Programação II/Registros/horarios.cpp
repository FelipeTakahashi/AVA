#include <stdio.h>
#include <math.h>

using namespace std;

int main() {
    int h, m, s, firstDaySum = 0; 
        scanf("%d:%d:%d", &h, &m, &s);
        
    int h2, m2, s2, secondDaySum = 0;
        scanf("%d:%d:%d", &h2, &m2, &s2);
        
    firstDaySum = (h*3600) + (m*60) + s;
    secondDaySum = (h2*3600) + (m2*60) + s2;
    
    int daysDifference = abs(firstDaySum - secondDaySum);
        int finalHours = daysDifference / 3600;
        int finalMinutes = (daysDifference % 3600) / 60;
        int finalSeconds = (daysDifference% 3600) % 60;
        
    printf("%02d:%02d:%02d", finalHours, finalMinutes, finalSeconds);
    
    return 0;
}
