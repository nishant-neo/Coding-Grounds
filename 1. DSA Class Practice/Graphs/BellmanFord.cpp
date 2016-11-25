#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;
class GraphNode
{
public:
    int u;
    int v;
    int w;

};
class VertexNode
{
public:
    int weight;
    int p;
    int n;
};
class Graph
{
public:
    int V;
    int E;
    vector <GraphNode> edges;
    Graph(int V, int E)
    {
        this->V = V;
        this->E = E;
    }
    void addEdge(int u, int v, int w)
    {
        struct GraphNode gnode;
        gnode.u = u;
        gnode.v = v;
        gnode.w = w;
        edges.push_back(gnode);
    }
};
int BellmanFord( Graph G, int s)
{
    vector <VertexNode> vertices(G.V);
    for( int i = 0; i < G.V; i++)
    {
        vertices[i].weight = INT_MAX-1000;
        vertices[i].p = s;
        vertices[i].n = 1;
    }
    vertices[s].weight = 0;
    for( int k = 1; k < G.V; k++)
    {
        for( int i = 0; i < G.E; i++ )
        {
            GraphNode temp = G.edges[i];
            int u = temp.u;
            int v = temp.v;
            int w = temp.w;
            if( vertices[v].weight > vertices[u].weight + w){
                vertices[v].weight = vertices[u].weight + w;
                vertices[v].p = u;
                vertices[v].n = vertices[u].n;
            }
            else if( vertices[v].weight == vertices[u].weight + w)
                vertices[v].n = vertices[u].n + vertices[v].n;
        }
    }
    for (int i = 0; i < G.E; i++)
    {
        GraphNode temp = G.edges[i];
        int u = temp.u;
        int v = temp.v;
        int w = temp.w;
        if (vertices[v].weight != INT_MAX && vertices[v].weight > vertices[u].weight + w)
            cout<<"Graph contains negative weight cycle"<<endl;
    }
    for( int i = 0; i < G.V; i++){
        cout<<"Vertex "<<i<< " is at distance: "<<vertices[i].weight<<" and the number of paths : "<<vertices[i].n<<endl;
    }
}
int main()
{
    int V = 5;
    int E = 8;
    Graph G( V,  E);
    G.addEdge(0,1,-1);
    G.addEdge(0,2,4);
    G.addEdge(1,2,3);
    G.addEdge(1,3,2);
    G.addEdge(1,4,2);
    G.addEdge(3,2,5);
    G.addEdge(3,1,1);
    G.addEdge(4,3,-3);
    BellmanFord(G, 0);
    return 0;
}
