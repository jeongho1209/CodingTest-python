#include <stdio.h>

int main() {
    int N = 0, K = 0, fact1 = 1, fact2 = 1, fact3 = 1, sum = 0;

    scanf("%d %d", &N, &K);

    for (int i = 1; i <= N; i++) {
        fact1 *= i; // N!
    }

    for (int j = 1; j <= K; j++) {
        fact2 *= j; // K!
    }

    for (int q = 1; q <= N - K; q++) {
        fact3 *= q; // N-K!
    }

    sum = fact1 / (fact3 * fact2); // N! / (N - K)! * K!

    printf("%d", sum);
}