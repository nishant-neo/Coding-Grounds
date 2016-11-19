#include<bits/stdc++.h>
#define INF 1000000
using namespace std;

typedef pair<int, int> iPair;

class Graph
{
public:
    int V;
    list< pair<int, int> > *adj;
    Graph(int V);
    void addEdge(int u, int v, int w);
    void primMST();
};

Graph::Graph(int V)
{
    this->V = V;
    adj = new list<iPair> [V];
}

void Graph::addEdge(int u, int v, int w)
{
    adj[u].push_back(make_pair(v, w));
    adj[v].push_back(make_pair(u, w));
}

void MST(Graph G, int s)
{
    priority_queue< iPair, vector <iPair> , greater<iPair> > pq;
    vector<int> key(G.V, INF);
    vector<int> parent(G.V, -1);
    vector<bool> inMST(G.V, false);
    pq.push(make_pair(0, s));
    key[s] = 0;
    while (!pq.empty())
    {
        int u = pq.top().second;
        pq.pop();
        inMST[u] = true;
        list< pair<int, int> >::iterator i;
        for (i = G.adj[u].begin(); i != G.adj[u].end(); ++i)
        {
            int v = (*i).first;
            int w = (*i).second;
            cout<< v <<" " <<w<<endl;
            if (inMST[v] == false && key[v] > w)
            {
                key[v] = w;
                pq.push(make_pair(key[v], v));
                parent[v] = u;
            }
        }
    }
    for (int i = 1; i < G.V; ++i)
        printf("%d - %d\n", parent[i], i);
}
int main()
{
    int V = 9;
    Graph G(V);
    G.addEdge(0, 1, 4);
    G.addEdge(0, 7, 8);
    G.addEdge(1, 2, 8);
    G.addEdge(1, 7, 11);
    G.addEdge(2, 3, 7);
    G.addEdge(2, 8, 2);
    G.addEdge(2, 5, 4);
    G.addEdge(3, 4, 9);
    G.addEdge(3, 5, 14);
    G.addEdge(4, 5, 10);
    G.addEdge(5, 6, 2);
    G.addEdge(6, 7, 1);
    G.addEdge(6, 8, 6);
    G.addEdge(7, 8, 7);
    MST(G, 0);
    return 0;
}
