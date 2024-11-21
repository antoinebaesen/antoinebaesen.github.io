#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//def de la taille de la matrice
#define SIZE 3

//prototypes
void createMatrix(int * matrice);
void printMatrix(int * matrice);
void multiplyMatrix(int * matriceA, int * matriceB, int * matriceC);
void mm(int * matriceA, int * matriceB, int * matriceC, int size);

int main()
{
    int matriceA[SIZE * SIZE];
    int matriceB[SIZE * SIZE];

    int matriceC[SIZE * SIZE];
    // rempli la matrice de 0

    memset(matriceC, 0, sizeof(int) * SIZE * SIZE);

    createMatrix(matriceA);
    createMatrix(matriceB);

    multiplyMatrix(matriceA, matriceB, matriceC);

    printMatrix(matriceC);

    //printMatrix(matriceA);
}

void createMatrix(int * matrice)
{
    int i, j;
    for(i = 0; i < SIZE; i++)
    {
        for(j = 0; j < SIZE; j++)
        {
            matrice[i * SIZE + j] = i * SIZE + j;
        }
    }
}

void printMatrix(int * matrice)
{
    int i, j;
    for(i = 0; i < SIZE; i++)
    {
        for(j = 0; j < SIZE; j++)
        {
            printf("%d ", matrice[i * SIZE + j]);
        }
        printf("\n");
    }
}

void multiplyMatrix(int * matriceA, int * matriceB, int * matriceC)
{
    int i, j, k;
    for(i = 0; i < SIZE; i++)
    {
        for(j = 0; j < SIZE; j++)
        {
            for(k = 0; k < SIZE; k++)
            {
                matriceC[i * SIZE + j] += matriceA[i * SIZE + k] * matriceB[k * SIZE + j];
            }
        }
    }
}

// mm est une multiplication de matrice récursive
void mm(int * matriceA, int * matriceB, int * matriceC, int size)
{
    
}
