#include <iostream>
using namespace std;

class Stack
{
    int top = 0; int lst[100];
public:
    Stack ()
    {}

    void push(int x)
    {top++; lst[top] = x;}

    void pop(void)
    {top--;}

    int peek(void)
    {return lst[top];}

    int Size(void)
    {return top;}

    bool is_Empty(void)
    {if(top == 0){return false;}
     else {return true;}
    }

};

int main()
{
    int N; cin >> N;
    Stack Max();
    int t; int i;
    for(i = N; i > 0; i--)
    {
        cin>>t;
        if (t == 1)
        {
            cin>>t;
            if (Max.is_Empty()|| (Max.peek() < t))
            { Max.push(t);}
            else
            { Max.push(Max.peek());}
        }
        else if (t == 2)
        { Max.pop();}
        else
        { cout<< Max.peek()<<endl; }
    }
    return 0;
}
