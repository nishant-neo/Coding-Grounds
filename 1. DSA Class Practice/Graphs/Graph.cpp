#include <iostream>
#include <vector>
#include <queue>
#include <limits>
using namespace std;

enum {
    INFINITY = 10000
};
enum Color {
    WHITE,
    GREY,
    BLACK
};
class Vertex {
public:
    int id;
    // BFS properties
    Color color;
    int discovery;
    Vertex* parent;
    // DFS properties
    int finish;
};
class Graph {
    public:
    int V;
    vector<Vertex> vertices;
    vector< std::vector<Vertex*> > adjacent;
    Graph(int V);
    void addEdge(int v, int w);
};

Graph::Graph( int V )
{
    this->V = V;
    this->vertices = new vector<Vertex>[V];
    int id = 0;

    for(std::vector<Vertex>::iterator it=vertices.begin() ; it < vertices.end(); it++ ) {
        (*it).id = id++;
    }
    adjacent = new vector< std::vector<Vertex*> >[V];
}
void Graph::addEdge(int v, int w)
{
    adjacent[v].push_back(&vertices[w]); // Add w to v’s list.
}
void BFS( Graph G, Vertex* s)
{
    for (auto& v: G.vertices)
        if (v.id == s->id)
            continue;
        v.color = WHITE;
        v.discovery = INFINITY;
        v.parent = nullptr;
    }
    s->color = GRAY;
    s->discovery = 0;
    s->parent = nullptr;
    queue<Vertex*> q;
    q.push_back(s);
    while (!q.empty()) {
        auto u = q.front();
        q.pop();
        for (auto v: G.adjacent[u->id])) {
            if (v->color == WHITE) {
                v->color = GRAY;
                v->discovery = u->discovery + 1;
                v->parent = u;
                q.push(v);
            }
        }
        u->color = BLACK;
    }

}
int main(){
    Graph G(4);
    G.addEdge(0, 1);
    G.addEdge(0, 2);
    G.addEdge(1, 2);
    G.addEdge(2, 0);
    G.addEdge(2, 3);
    G.addEdge(3, 3);
    cout << "Following is Depth First Traversal (starting from vertex 2) \n";
    g.BFS(G,&G.vertices[2]);
    return 0;
}
