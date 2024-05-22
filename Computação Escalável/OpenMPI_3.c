#include "mpi.h"
#include <stdio.h>

int main(int argc, char * argv[]) {
    int processId; // Identificador do processo
    int numProcesses; // Número de processos
    int nameSize; // Tamanho do nome da máquina
    char computerName[MPI_MAX_PROCESSOR_NAME]; // Nome da máquina

    MPI_Init(&argc, &argv); // Inicializa o ambiente MPI
    MPI_Comm_size(MPI_COMM_WORLD, &numProcesses); // Número de processos
    MPI_Comm_rank(MPI_COMM_WORLD, &processId); // Identificador do processo
    MPI_Get_processor_name(computerName, &nameSize); // Nome da máquina

    fprintf(stderr,"Hello from process %d on %s\n", processId, computerName);

    MPI_Finalize(); // Finaliza o ambiente MPI
    return 0;
}