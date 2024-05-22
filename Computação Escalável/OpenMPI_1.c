#include "mpi.h"
#include <stdio.h>

int main(int argc, char **argv) {
    int rc;
    rc = MPI_Init(&argc, &argv);
    if (rc == MPI_SUCCESS) {
        printf("MPI iniciou corretamente\n");
    }

    MPI_Finalize();
    return 0;
}