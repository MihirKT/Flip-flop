#include <stdio.h>

int d_flip_flop(int d, int clk, int* q, int* q_bar) {
    static int prev_clk = 0;
    if (clk == 1 && prev_clk == 0) {
        *q_bar = !d;
        *q = d;
        return 1;
    }
    prev_clk = clk;
    return 0;
}

int main() {
    int q = 0, q_bar = 1;
    int clk = 0, d = 0;
    printf("D flip-flop\n");
    while (1) {
        printf("Enter D and CLK (0 or 1):\n");
        scanf("%d %d", &d, &clk);
        d_flip_flop(d, clk, &q, &q_bar);
        printf("Q = %d, Q' = %d\n", q, q_bar);
    }
    return 0;
}
