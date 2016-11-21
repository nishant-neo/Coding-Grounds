#include <iostream>
#include <vector>
#include <stdlib.h>
#include <algorithm>

using namespace std;

struct Edge
{
    int weight;
    int u;
    int v;
};
class Graph
{
    public:
    int E, V;
    vector<Edge> edge;
    void addEdge( int u, int v, int weight)
    {
        struct Edge temp;
        int tol = edge.size()-1;
        temp.u = u;
        temp.v = v;
        temp.weight = weight;
        edge.push_back(temp);
    }
    Graph(int E, int V)
    {
        this->V = V;
        this->E = E;
        //this->edge = new vector<Edge> (E);
    }
};
int find( int parent[], int i)
{
    if( parent[i] == -1)
        return i;
    return find( parent, parent[i]);
}
void Union( int parent[], int x, int y)
{
    int xSet = find(parent, x);
    int ySet = find(parent, y);
    parent[xSet] = ySet;
}
struct less_than_key
{
    inline bool operator() (const Edge& struct1, const Edge& struct2)
    {
        return (struct1.weight < struct2.weight);
    }
};
void isCycle( Graph G )
{
    int V = G.V;
    struct Edge result[V];
    int e = 0;  // An index variable, used for result[]
    int i = 0;  // An index variable, used for sorted edges
    sort(G.edge.begin(), G.edge.end(), less_than_key());
    int parent[G.V];
    for(int k = 0; k < G.V; ++k)
        parent[k] = -1;
    while (e < V - 1)
    {
        struct Edge next_edge = G.edge[i++];
        int x = find(parent, next_edge.u);
        int y = find(parent, next_edge.v);
        // If including this edge does't cause cycle, include it
        // in result and increment the index of result for next edge
        if (x != y)
        {
            result[e++] = next_edge;
            Union(parent, x, y);
        }
        // Else discard the next_edge
    }

    // print the contents of result[] to display the built MST
    cout<<"Following are the edges in the constructed MST\n";
    for (i = 0; i < e; ++i)
        cout<< result[i].u<<" "<< result[i].v<<" "<<result[i].weight<<endl;
    return;
}
int main()
{
    int V = 4, E = 3;
    Graph G(E, V);
    G.addEdge(0,1,10);
    G.addEdge(0,2,6);
    G.addEdge(0,3,5);
    G.addEdge(1,3,15);
    G.addEdge(2,3,4);

    isCycle(G);;

}

