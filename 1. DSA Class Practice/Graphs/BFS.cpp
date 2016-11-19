#include <iostream>
#include <vector>
#include <queue>
using namespace std;

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
void BFS(Graph G, int s)
{

    bool *visited = new bool[G.V];
    for(int i = 0; i < G.V; i++)
        visited[i] = false;
    queue<int> q;
    visited[s] = true;
    q.push(s);
    vector<int>::iterator i;
    while(!q.empty())
    {
        s = q.front();
        cout << s << " ";
        q.pop();
        for(i = G.adjacent[s].begin(); i != G.adjacent[s].end(); ++i)
        {
            if(!visited[*i])
            {
                visited[*i] = true;
                q.push(*i);
            }
        }
    }
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
    BFS(G,0);
    return 0;

}
