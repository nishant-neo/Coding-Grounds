#include<iostream>
#include <stdio.h>
#define V 4
#define INF 99999
using namespace std;

class GraphNode
{
public:
    int w, p, n;
};
void floydWarshall (int G[][V])
{
    GraphNode D[V][V];
    for (int i = 0; i < V; i++){
        for (int j = 0; j < V; j++){
            D[i][j].w = G[i][j];
            D[i][j].p = i;
            D[i][j].n = (G[i][j] == INF) ? 0 : 1;
        }
    }
    for (int k = 0; k < V; k++){
        for (int i = 0; i < V; i++){
            for (int  j= 0; j < V; j++){
                if (D[i][j].w > D[i][k].w + D[k][j].w){
                    D[i][j].w = D[i][k].w + D[k][j].w;
                    D[i][j].p = k;
                    D[i][j].n = D[i][j].n + D[i][k].n *  D[k][j].n;
                }
                else if( D[i][j].w ==  D[i][k].w + D[k][j].w)
                    D[i][j].n = D[i][j].n + D[i][k].n *  D[k][j].n;
            }
        }
    }
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            if (D[i][j].w == INF)
                printf("%7s", "INF");
            else
                printf ("%7d", D[i][j].w);
        }
        cout<<endl;
    }
}



int main()
{
    int graph[V][V] = { {0,   5,  INF, 10},
                        {INF, 0,   3, INF},
                        {INF, INF, 0,   1},
                        {INF, INF, INF, 0}
                      };
    floydWarshall(graph);
    return 0;
}
