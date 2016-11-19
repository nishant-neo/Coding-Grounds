#include <iostream>
#include <vector>
#include <stack>
#define SIZE 5

using namespace std;
int time = 0;
class Graph
{
public:
    int V;
    vector <int> *adjacent;
    Graph(int V);
    void addEdge( int u, int v);
    Graph getTranspose();
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
Graph Graph::getTranspose()
{
    Graph g(V);
    for (int v = 0; v < V; v++)
    {
        vector<int>::iterator i;
        for(i = adjacent[v].begin(); i != adjacent[v].end(); ++i)
        {
            g.adjacent[*i].push_back(v);
        }
    }
    return g;
}
void DFSVisit( Graph G, int s, bool visited[], stack <int> &st )
{
    visited[s] = true;

    cout<<s<< " ";
    vector<int>::iterator i;
    for(i = G.adjacent[s].begin(); i != G.adjacent[s].end(); ++i)
    {
        if( !visited[*i]){
                //cout<<"GV";
            DFSVisit(G, *i, visited, st);
        }
    }
    st.push(s);

}
void DFS(Graph G, int s, stack <int> &st)
{
    bool visited[G.V];
    for( int i = 0; i < G.V; i++){
        visited[i] = false;
    }
    DFSVisit(G, s, visited,  st);
    /*cout<<endl;
    while( !st.empty())
    {
        cout<<st.top()<<" ";
        st.pop();
    }*/
    cout<<endl;
}
int main()
{
    stack <int> st;
    stack <int> st2;
    Graph G(SIZE);
    G.addEdge(1, 0);
    G.addEdge(0, 2);
    G.addEdge(2, 1);
    G.addEdge(0, 3);
    G.addEdge(3, 4);
    cout<< "The BFS Traversal of the Graph is \n";
    //int order[SIZE];
    DFS(G,2,st);
    Graph GT = G.getTranspose();// got the transposed graph
    bool visited[SIZE];
    for(int i = 0; i < SIZE; i++)
        visited[i] = false;
    cout<< "The strongly connected compomnents \n";
    while (st.empty() == false) // now applying DFS in the stack's order
    {
        int v = st.top();
        st.pop();
        if (visited[v] == false)
        {
            DFSVisit(GT, v, visited, st2);
            cout << endl;
        }
    }
    return 0;

}

