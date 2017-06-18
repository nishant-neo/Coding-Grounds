#include <iostream>
#include <vector>
#include <stack>

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

void DFSVisit( Graph G, int s, bool visited[], int oldp[],int discover[] , stack <int> &st )
{
    visited[s] = true;
    time = time+1;
    discover[s] = time;
    oldp[s] = time;
    st.push(s);
    cout<<s<< " in time: "<<time<<endl;
    vector<int>::iterator i;
    int u = s;
    for(i = G.adjacent[s].begin(); i != G.adjacent[s].end(); i++)
    {
//        int u = s;
        int v = *i;
        if (!visited[v])
        {
            DFSVisit(G, *i, visited,  oldp, discover, st);
            oldp[u]  = min(oldp[u], oldp[v]);
        }
        else if (visited[v])
            oldp[u]  = min(oldp[u], oldp[v]);
    }

    int x = 0;
    if (oldp[u] == discover[u])
    {
        while (st.top() != u)
        {
            x = (int) st.top();
            cout << x << " ";
            visited[x] = 1;
            st.pop();
        }
        x = (int) st.top();
        cout << x<< "\n";
        visited[x] = 0;
        st.pop();
    }

}
void DFS(Graph G, int s)
{
    //int V =G.V;
    stack <int> st;
    int time = 0;
    int oldp[G.V];
    int discover[G.V];
    bool visited[G.V];
    for( int i = 0; i < G.V; i++){
        visited[i] = false;
        oldp[i] = i;
        discover[i] = 0;

    }
    DFSVisit(G, s, visited,  oldp, discover, st);
}
int main()
{

    /*int t;
    cin>>t;
    while( t--)
    {
        int n,m;
        cin>>n>>m;
        while( m-- )
        {
            int a,b,c;
            cin>>a>>b>>c;
            if( c == 1)
                G.addedge(a, b, 0 )
        }

    }*/
    Graph G(4);
    G.addEdge(0, 1);
    G.addEdge(0, 2);
    G.addEdge(1, 2);
    G.addEdge(2, 0);
    G.addEdge(2, 3);
    G.addEdge(3, 3);
    cout<< "The DFS Traversal of the Graph is \n";
    DFS(G,2);
}
