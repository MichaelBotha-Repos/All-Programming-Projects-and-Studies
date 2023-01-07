#include <iostream>
#include <string>

using namespace std;

// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

string solution(string &message, int K) 
{
    string new_string;

    if(message.length() > K)
    {
        message.resize(K);
        message.shrink_to_fit();

    }

    cout << message;

    return message;
}


int main()
{


    return 0;
}