#include <iostream>
#include <vector>
#include <stdlib.h>
#include <queue>
using namespace std;
int time = 0;
struct GraphNode
{
public:
    int v;
    int w;
};
struct VertexNode
{
public:
    int id;
    int d;
    int p;
};
class Graph
{
public:
    int V;
    vector <GraphNode> *adjacent;

    Graph(int V);
    void addEdge( int u, int v, int w);
};
Graph::Graph(int V)
{
    this->V = V;
    adjacent = new vector<GraphNode>[V];
    //Vertices = new vector<VertexNode>(V);
}
void Graph::addEdge(int u, int v, int w)
{
    struct GraphNode gnode;
    gnode.v = v;
    gnode.w = w;
    adjacent[u].push_back(gnode);
}
//bool operator<(const VertexNode& lhs, const VertexNode& rhs)
//    {
//        return lhs.d < rhs.d;
//    }
class CompareVertex {
public:
    bool operator()(const VertexNode& lhs, const VertexNode& rhs) // t2 has highest prio than t1 if t2 is earlier than t1
    {
       return lhs.d > rhs.d;
    }
};
void Dijkstra( Graph G, int s )
{
    vector <VertexNode> Vertices(G.V);
    for( int i = 0; i < G.V; i++)
    {
        Vertices[i].d = 100000;
        Vertices[i].id = i;
        Vertices[i].p = -1;
    }

    Vertices[s].d = 0;
    priority_queue<VertexNode, vector <VertexNode>, CompareVertex > pq;
    for( int i = 0; i < G.V; i++)
    {
        pq.push(Vertices[i]);
    }
    while( !pq.empty())
    {

        VertexNode u1 = pq.top();
        cout<<"GF"<<u1.d<<" " <<u1.id<<endl;
        pq.pop();
        vector<GraphNode>::iterator i;
        for(i = G.adjacent[u1.id].begin(); i != G.adjacent[u1.id].end(); ++i)
        {
            //cout<< " -> "<< (*i).v<<'('<<i->w<<')'<<endl;
            //cout<<Vertices[(*i).v].d<<" " << u1.d <<" "<< (*i).w;
           if( Vertices[(*i).v].d > u1.d + (*i).w)
           {
               Vertices[(*i).v].d = u1.d + (*i).w;
           }
        }

    }

    for( int i = 0; i < G.V; i++)
    {
        cout<<Vertices[i].d<<endl;
    }
}
void printGraph( Graph G)
{
    for (int v = 0; v < G.V; ++v)
    {
        cout<<"head :"<<  v;
        vector<GraphNode>::iterator i;
        for(i = G.adjacent[v].begin(); i != G.adjacent[v].end(); ++i)
        {
           cout<< " -> "<< (*i).v<<'('<<i->w<<')';
        }
        cout<<endl;
    }
}
int main()
{
    Graph G(9);
    G.addEdge( 0, 1, 4);
    G.addEdge( 0, 7, 8);
    G.addEdge( 1, 2, 8);
    G.addEdge( 1, 7, 11);
    G.addEdge( 2, 3, 7);
    G.addEdge( 2, 8, 2);
    G.addEdge( 2, 5, 4);
    G.addEdge( 3, 4, 9);
    G.addEdge( 3, 5, 14);
    G.addEdge( 4, 5, 10);
    G.addEdge( 5, 6, 2);
    G.addEdge( 6, 7, 1);
    G.addEdge( 6, 8, 6);
    G.addEdge( 7, 8, 7);
    printGraph(G);
    cout<< "The BFS Traversal of the Graph is \n";
    Dijkstra( G, 3 );
    return 0;

}


