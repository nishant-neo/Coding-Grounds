#include <stdio.h>

int main()
{
    int i=0;
    printf("Helllllo %nworld\n", &i); /* the %n stores into i */
    printf("i=%d\n",i);
    return 0;
}
