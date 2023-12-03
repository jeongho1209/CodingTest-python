#include <stdio.h>

long long int arr[10000] = {0,};

long long int fibo(long long int n) {
    if (n <= 1) return n;
    else {
        if (arr[n] != 0) { return arr[n]; }
        arr[n] = fibo(n - 1) + fibo(n - 2);
        return arr[n];
    }
}

int main() {
    int n;
    scanf("%d", &n);

    fibo(n);
    printf("%lld", fibo(n));
}
