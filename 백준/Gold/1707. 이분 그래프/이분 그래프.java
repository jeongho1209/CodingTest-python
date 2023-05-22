import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer>[] a;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();

        while (x-- > 0) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();

            int[] arr = new int[n + 1];

            a = new ArrayList[n + 1];

            for (int i = 1; i <= n; i++) {
                a[i] = new ArrayList<>();
            }

            for (int i = 1; i <= m; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();

                a[u].add(v);
                a[v].add(u);
            }
            for (int i = 1; i <= n; i++) {
                arr[i] = 0;
            }

            for (int i = 1; i <= n; i++) {
                if (arr[i] == 0) {
                    dfs(i, arr, 1);
                }
            }

            int YesOrNo = 1;

            for (int i = 1; i <= n; i++) {
                for (int j = 0; j < a[i].size(); j++) {
                    if (arr[i] == arr[a[i].get(j)]) {
                        YesOrNo = 0;
                        break;
                    }
                }
            }
            if (YesOrNo == 1)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }

    private static void dfs(int x, int[] check, int c) {
        check[x] = c;
        for (int i : a[x]) {
            if (check[i] == 0) {
                dfs(i, check, 3 - c);
            }
        }
    }
}