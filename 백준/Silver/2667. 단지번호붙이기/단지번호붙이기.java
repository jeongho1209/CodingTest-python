import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static ArrayList<Integer>[] a;

    static ArrayList<Integer>[] arrayList;

    static int[][] array;

    static int[] Danji;

//    public static void main1(String[] args) {
//        Scanner scanner = new Scanner(System.in);
//        int x = scanner.nextInt();
//
//        while (x-- > 0) {
//            int n = scanner.nextInt();
//            int m = scanner.nextInt();
//
//            int[] arr = new int[n + 1];
//
//            a = new ArrayList[n + 1];
//
//            for (int i = 1; i <= n; i++) {
//                a[i] = new ArrayList<>();
//            }
//
//            for (int i = 1; i <= m; i++) {
//                int u = scanner.nextInt();
//                int v = scanner.nextInt();
//
//                a[u].add(v);
//                a[v].add(u);
//            }
//            for (int i = 1; i <= n; i++) {
//                arr[i] = 0;
//            }
//
//            for (int i = 1; i <= n; i++) {
//                if (arr[i] == 0) {
//                    dfs(i, arr, 1);
//                }
//            }
//
//            int YesOrNo = 1;
//
//            for (int i = 1; i <= n; i++) {
//                for (int j = 0; j < a[i].size(); j++) {
//                    if (arr[i] == arr[a[i].get(j)]) {
//                        YesOrNo = 0;
//                        break;
//                    }
//                }
//            }
//            if (YesOrNo == 1)
//                System.out.println("YES");
//            else
//                System.out.println("NO");
//        }
//    }
//
//    private static void dfs(int x, int[] check, int c) {
//        check[x] = c;
//        for (int i : a[x]) {
//            if (check[i] == 0) {
//                dfs(i, check, 3 - c);
//            }
//        }
//    }

    static void dfs(int i, int j, int N, int cnt) {
        if (array[i][j] == 1) {
            array[i][j] = 0;
            Danji[cnt]++;
            if (i - 1 >= 0) dfs(i - 1, j, N, cnt);
            if (i + 1 < N) dfs(i + 1, j, N, cnt);
            if (j - 1 >= 0) dfs(i, j - 1, N, cnt);
            if (j + 1 < N) dfs(i, j + 1, N, cnt);
        }
    }

    public static void main(String[] args) {
        int cnt = 0;
        Scanner sc = new Scanner(System.in);

        int N = Integer.parseInt(sc.nextLine());
        Danji = new int[1000];

        array = new int[1000][1000];

        for (int i = 0; i < N; i++) {
            String[] split = sc.nextLine().split("");
            for (int j = 0; j < split.length; j++) {
                array[i][j] = Integer.parseInt(split[j]);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (array[i][j] == 1) {
                    cnt++;
                    dfs(i, j, N, cnt);
                }
            }
        }

        System.out.println(cnt);

        Arrays.stream(Danji)
                .sorted()
                .filter(value -> value != 0)
                .forEach(System.out::println);
    }
}
