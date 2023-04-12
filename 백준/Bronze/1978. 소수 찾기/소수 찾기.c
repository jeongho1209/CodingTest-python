#include <stdio.h>

int main() {
    int N = 0, num = 0, count = 0, i = 0;

    scanf("%d", &N);

    while (N--) {
        scanf("%d", &num);
        for (i = 2; i < num; i++) { // 소수 = 1과 자기 자신만을 약수로 가지는 수 예를 들어 2, 3, 5, 7
            if (num % i == 0) break;
        }
        if (i == num) count++;
    }

    printf("%d", count);

}