#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
  FILE *note;

  char name[100], *content;

  content = (char *)malloc(1024);

  printf("Write the name of your file : ");

  scanf("%s", name);

  note = fopen(name, "w");

  printf("\nWrite the content of your file : ");

  scanf(" %[^\n]s", content);

  fprintf(note, "%s", content);

  printf("\nContent has been written to file!\n\n");

  free(content);

  fclose(note);

  return 0;
}