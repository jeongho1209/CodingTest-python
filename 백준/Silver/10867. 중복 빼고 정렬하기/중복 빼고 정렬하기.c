#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100000

int comp(const void *a, const void *b) {
    return (*(int *) a - *(int *) b);
}

int main() {
    int N = 0;

    scanf("%d", &N);

    int arr[MAX_SIZE];

    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }

    qsort(arr, N, sizeof(int), comp);

    for (int j = 0; j < N; j++) {
        if (arr[j] != arr[j + 1]) {
            printf("%d ", arr[j]);
        }
    }

}