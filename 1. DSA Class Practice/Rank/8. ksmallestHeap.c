#include <stdio.h>
int A[10000];
int len;

int swap( int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
void topDownHeapify( int i)
{
    int l, r, m;
    while( (2*i + 1) < len)
    {
        l = 2*i + 1;
        r = l+1;
        if( r < len && A[l] < A[r])
            m = r;
        else
            m = l;
        if( A[i] < A[m])
        {
            swap( &A[i],&A[m]);
            i = m;
        }
        else
            i = len;
    }
}
void bottomUpHeapify( int i)
{
    while( i > 0 && A[(i-1)/2] < A[i])
    {
        swap(&A[(i-1)/2], &A[i]);
        i = (i-1)/2;
    }
}
void add(int x)
{
    len++;
    A[len-1] = x;
    bottomUpHeapify(len-1);
}
int deleteMax()
{
    swap( &A[0], &A[len-1]);
    len--;
    topDownHeapify(0);
    return A[len];
}
int maxElement()
{
    return A[0];
}
int main()
{
    len = 0;
    int i;
    /*int x = 10;
    while( x-- )
    {
        int t = rand() % (100) + 1;
        printf("%d ",t);
        add(t);
    }
    printf("\n");
    x = 4;
    while( x > 0 )
    {
        printf("%d ",deleteMax());
        x--;
    }*/
    int k = 4;
    int n = 10;
    for( i = 0; i < n; i++)
    {
        int num = rand() % (100000) + 1;
        printf("%d ",num);
        if( len < k)
            add(num);
        else
            {
                if( maxElement() > num ){
                    A[0] = num;
                    topDownHeapify(0);
                }
                else
                {
                    continue;
                }
            }
    }
    printf("\n%d\n",len);
    int x = 4;
    while( x > 0 )
    {
        printf("%d ",deleteMax());
        x--;
    }
    return 0;
}

