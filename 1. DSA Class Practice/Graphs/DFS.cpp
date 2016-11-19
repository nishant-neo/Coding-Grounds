#include <iostream>
#include <vector>

using namespace std;
int time = 0;
class Graph
{
public:
    int V;
    vector <int> *adjacent;
    Graph(int V);
    void addEdge( int u, int v);
};
Graph::Graph(int V)
{
    this->V = V;
    adjacent = new vector<int>[V];
}
void Graph::addEdge(int u, int v)
{
    adjacent[u].push_back(v);
}
void DFSVisit( Graph G, int s, bool visited[], int finish[],int discover[] )
{
    visited[s] = true;
    time = time+1;
    discover[s] = time;
    cout<<s<< " in time: "<<time<<endl;
    vector<int>::iterator i;
    for(i = G.adjacent[s].begin(); i != G.adjacent[s].end(); ++i)
    {
        if( !visited[*i])
            DFSVisit(G, *i, visited,  finish, discover);
    }
    time = time+1;
    finish[s] = time;

}
void DFS(Graph G, int s)
{
    //int V =G.V;
    int time = 0;
    int finish[G.V];
    int discover[G.V];
    bool visited[G.V];
    for( int i = 0; i < G.V; i++){
        visited[i] = false;
        finish[i] = 0;
        discover[i] = 0;

    }
    DFSVisit(G, s, visited,  finish, discover);
}
int main()
{
    Graph G(4);
    G.addEdge(0, 1);
    G.addEdge(0, 2);
    G.addEdge(1, 2);
    G.addEdge(2, 0);
    G.addEdge(2, 3);
    G.addEdge(3, 3);
    cout<< "The BFS Traversal of the Graph is \n";
    DFS(G,2);
    return 0;

}

