#include <stdio.h>
#include <stdlib.h>

/*

Here lies a lot of Linked Lists content.
Most of those are either copied from https://www.ime.usp.br/~pf/algoritmos/aulas/lista.html 
or simply solutions to the exercises in there.

To fully understand each function, abstraction is the best way. The more you abstract, the more you understand

*/

struct node {
    int id;
    node *next;
};

void recursivePrint(node *list) {
    if (list != NULL) {
        printf("%d ", list->id);
        recursivePrint(list);
    }
}

void iterativePrint(node *list) {
    for(node *p = list; p != NULL; p = p->next)
        printf("%d ", p->id);
}

void printHeadless(node *headless) {
    node *p = headless;
    for(p = headless->next; p != NULL; p = p->next) 
        printf("%d", p->id);
}

int countNodes(node *list) {
    int nodeCounter = 0;
    for(node *p = list; p != NULL; p = p->next) 
        nodeCounter++;

    return nodeCounter;
}

int getNodeHeight(node *list, int nodeID) {
    int height = 0, flagID = 0;
    for(node *p = list; p != NULL; p = p->next) {
        if (p->id == nodeID) flagID = 1;
        if (flagID) height++;
    }
}

int getNodeDepth(node *list, int nodeID) {
    int depth = 0, flagID = 0;
    node *p = list;
    while(p->id != nodeID) {
        depth++;
        p = p->next;
    }
}

node* iterativeSearch(node* list, int lookFor) {
    node *p = list;
    while (p != NULL && p->id != lookFor)
        p = p->next;
    return p;
}

node* recursiveSearch(node *list, int lookFor) {
    if (list == NULL) return NULL;
    if (list->id == lookFor) return list;
    recursiveSearch(list->next, lookFor);
}

node* itHeadlessSearch(node *headless, int lookFor) {
    node *p = headless->next;
    while (p != NULL && p->id != lookFor) 
        p = p->next;
    return p;
}

node* recHeadlessSearch(node *headless, int lookFor) { // ? ? ?
    if(headless->next == NULL) return NULL;
    if (headless->next->id == lookFor) return headless;
    recHeadlessSearch(headless->next, lookFor);
}

bool iterativeAscending(node *list) {
    node *q = list, *p = list;
    p = p->next; 
    bool ascending = 1;

    while(p != NULL) {
        if(q->id > p->id) ascending = 0;
    }

    return ascending;
}

bool recursiveAscending(node *list) {
    if(list == NULL) return 1;
    if (list->id > list->next->id) return 0;
    return recursiveAscending(list->next);
}

/*
There is an exercise that asks for a search on an ascending linked list.
I assume this is the same as normal search (with an obvious stop), of course, not counting a binary search.
*/

node* iterativeAscSearch(node *list, int lookFor) {
    node *p = list, *q = list;
    p = p->next;
    while(p != NULL && q->id < p->id) {
        if (q->id == p->id) return q;
        p = p->next;
    }
}

node* recursiveAscSearch(node *list, int lookFor) {
    if (list == NULL || list->id > lookFor) return NULL;
    if (list->id == lookFor) return list;
    return recursiveAscSearch(list->next, lookFor);
}

/*
By any means, I don't think this is really what the exercise was asking for.
*/ 

node* iterativeMin(node *list) {
    node *p = list, *q = list;
    p = p->next;
    while(p != NULL) {
        if (p->id < q->id) 
            q = p;
        p = p->next;
    }

    return q;
}

node* recursiveMin(node *list, node *minNode) { // ??? This might be wrong ???
    if(list == NULL) return minNode;
    if(list->id < minNode->id) minNode = list;
    return recursiveMin(list, minNode);
}

bool iterativeEqual(node *list, node *copy) {
    node *p = list, *q = copy;
    bool equal = 1;
    while(p != NULL || q != NULL) { // Might change this to an && (*)
        if (p->id != q->id) equal = 0; // if (*), change this to return 0;
        p = p->next;
        q = q->next;
    }    

    return equal; // if (*), change this to return 1;
}

bool recursiveEqual(node *list, node *copy) {
    if(list == NULL && copy == NULL) return 1;
    if(list->id != copy->id) return 0;
    return recursiveEqual(list->next, copy->next);
}

node* getMiddleNode(node *list, node *limit) {
    node *twice = list->next, *once = list;

    while(twice != limit) {
        twice = twice->next;
        if(twice != limit) {
            twice = twice->next;
            once = once->next;
        }
    }

    return once;
}
/*

!!!                                                          !!!
!!! Starting from here, there are a lot of exercises missing !!!
!!!                                                          !!!

*/
void insertNode(node *list, int element) {
    node *p;
    p = (node*)malloc(sizeof (node));
    p->id = element;
    p->next = list->next;
    list->next = p;
}

void removeNode(node *list) { // This function assumes list != NULL and list->next != NULL
    node *trash;
    trash = list->next;
    list->next = trash->next;
    free(trash);
}

void searchAndRemove(node *list, int element) {
    node *p = list, *q = list;
    p = p->next;
    while(p != NULL && p->id != element) {
        q = p;
        p = p->next;
    }

    if (p != NULL) {
        q->next = p->next;
        free(p);
    }
}

void searchAndInsert(node *list, int element, int beforeWho) {
    node *p, *q, *insert;
    insert = (node*)malloc(sizeof (node));
    q = list;
    p = list->next;

    while(p != NULL && p->id != beforeWho) {
        q = p;
        p = p->next;
    }
    insert->next = p;
    q->next = insert;
}

int main() {
    node *headless;
    headless = (node*)malloc(sizeof (node));

}
