#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <pthread.h>
#include <math.h>

#define num_threads 48

struct args {
  int t_id;
  int stop;
};

int hashmat[] = {1,116,124,151,134,21,68,60,60,43,33,141,103,128,43,134,143,63,136,177,130,90,111,128,167,121,74,151,175,34,39,193,94,32,97,107,36,50,155,40,158,61,163,58,52,175,180,191,74,17};
int vs[] = {146,23,167,5,59,97,193,22,186,27,170,33,170,85,42,57,170,130,8,143,200,39,10,160,169,178,137,40,65,173,105,24,130,148,187,168,64,172,194,37,89,162,74,39,27,74,180,36,10,58};
int dif;

void *Thread_vs(void *input) {
    int stop = ((struct args*)input)->stop;
    int t_id = ((struct args*)input)->t_id;

    printf("t_id %d %d\n", t_id, stop);

    for (int i = 0; i < stop; i++) {
        dif = abs(hashmat[i] - vs[i]);
    }
    pthread_exit(NULL);
}

int main (int argc, char *argv[]) {

    clock_t uptime_ini = clock();

    pthread_t threads[num_threads];
    long i;

    int step = round(sizeof(vs) / (sizeof(vs[0]) * num_threads));
    printf("step = %d size: %lu\n", step, sizeof(vs[0]));

    for (i = 0; i < num_threads; i++) {
      struct args *marquito = (struct args *) malloc(sizeof(struct args));
      marquito->t_id = i;
      marquito->stop = (i+1) * step;
      pthread_create(&threads[i], NULL, Thread_vs, (void*) marquito);
      pthread_join(threads[i], NULL);
    }
    clock_t uptime_fim = clock();

    printf("%Lf\n", (long double)(uptime_fim - uptime_ini));
    pthread_exit(NULL);

}