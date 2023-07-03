#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>
#include <math.h>

#define num_threads 16

struct args {
    int n1;
    int n2;
};


int array1[] = {1,2,3,4,5,6,7,8,9,10};
int array2[] = {1,2,3,4,5,6,7,8,9,10};
long long tmp, tmp2, n1, n2;

void *Thread(void *input) {
    for (tmp = 0; array1[n1] > 1; n1--) {
       tmp = tmp * n1;
    }
    for (tmp2 = 0; array2[tmp2] > 1; n2--) {
        tmp2 = tmp2 * n2;
    }
    long long vf = tmp + tmp2;
    printf("Valor %lld\n", vf);

}

int main (int argc, char *argv[]) {

    clock_t uptime_ini = clock();

    pthread_t threads [num_threads];
    long i;

    for (i = 0; i < num_threads; i++) {
        struct args *marquito = (struct args *) malloc(sizeof(struct args));
        marquito->n1 = 7;
        marquito->n2 = 3;
        pthread_create(&threads[i], NULL, Thread, (void*)marquito);
        pthread_join(threads[i], NULL);
    }

    clock_t uptime_fim = clock();
    printf("%Lf\n", (long double)(uptime_fim - uptime_ini));


    pthread_exit(NULL);
}