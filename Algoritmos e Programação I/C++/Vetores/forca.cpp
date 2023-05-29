#include <iostream>
#include <iomanip>

int main() {
    double FirstV[3], SecondV[3], AnswerV[3];
        std::cin >> FirstV[0] >> FirstV[1] >> FirstV[2];
        std::cin >> SecondV[0] >> SecondV[1] >> SecondV[2];

    for (int i = 0; i < 3; i++) {
        AnswerV[i] = FirstV[i] + SecondV[i];
        std::cout << std::fixed << std::setprecision(2) << AnswerV[i] << " ";
    }

    std::cout << std::endl;
}
