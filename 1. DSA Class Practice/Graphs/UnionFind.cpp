#include <iostream>
#include <vector>

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
int isCycle( Graph G )
{
    int parent[G.V];
    for(int i = 0; i < G.V; ++i)
        parent[i] = -1;
    for(int i = 0; i < G.E; ++i)
    {
        int x = find(parent, G.edge[i].u);
        int y = find(parent, G.edge[i].v);
        if (x == y)
            return 1;
        Union(parent, x, y);
    }
    return 0;
}
int main()
{
    int V = 4, E = 3;
    Graph G(E, V);
    G.addEdge(0,1,10);
    G.addEdge(0,2,6);
    G.addEdge(0,3,5);
    //G.addEdge(1,3,15);
    //G.addEdge(2,3,4);

    if (isCycle(G))
        cout<<"Graph contains cycle" ;
    else
        cout<< "Graph doesn't contain cycle" ;

}
