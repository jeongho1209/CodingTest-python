import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[][] array;

    static int[] Danji;

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
