#include "mpi.h"
#include <stdio.h>

int main(int argc, char **argv) {
    int numtasks, rank, rc;
    rc = MPI_Init(&argc, &argv);
    if (rc == MPI_SUCCESS) {
        MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
        MPI_Comm_rank(MPI_COMM_WORLD, &rank);
        printf("Sou o processo %d de %d\n", rank, numtasks);
    }

    MPI_Finalize();
    return 0;
}