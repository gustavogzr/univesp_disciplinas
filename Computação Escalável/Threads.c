#include <omp.h>

main() {
    int nthreads, tid; // Variáveis locais

    #pragma omp parallel private(nthreads, tid) // Início da região paralela
    {
        tid = omp_get_thread_num(); // Obtém o ID da thread
        printf("Hello World from thread = %d\n", tid); // Imprime a mensagem

        if tid == 0 // verifica se é o master thread
        {
            nthreads = omp_get_num_threads(); // Obtém o número de threads
            printf("Number of threads = %d\n", nthreads); // Imprime o número de threads
        }
    } // Fim da região paralela
}

/* para compilar o código acima, utilize o comando abaixo:
gcc -o Threads Threads.c -fopenmp
 */