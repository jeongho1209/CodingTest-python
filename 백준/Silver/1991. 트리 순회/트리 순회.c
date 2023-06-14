#include <stdio.h>

int a[50][2];

void preorder(int x) {
    // root -> left -> right
    if (x == -1) return;
    printf("%c", x + 'A');
    preorder(a[x][0]);
    preorder(a[x][1]);
}

void inorder(int x) {
    // left -> root -> right
    if (x == -1) return;
    inorder(a[x][0]);
    printf("%c", x + 'A');
    inorder(a[x][1]);
}

void postorder(int x) {
    // left -> right -> root
    if (x == -1) return;
    postorder(a[x][0]);
    postorder(a[x][1]);
    printf("%c", x + 'A');
}

int main() {

    int n = 0;

    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        char x, y, z;

        getchar();

        scanf("%c %c %c", &x, &y, &z);

        x = x - 'A';

        if (y == '.') {
            a[x][0] = -1;
        } else {
            a[x][0] = y - 'A';
        }
        if (z == '.') {
            a[x][1] = -1;
        } else {
            a[x][1] = z - 'A';
        }
    }

    preorder(0);
    printf("\n");
    inorder(0);
    printf("\n");
    postorder(0);
}
