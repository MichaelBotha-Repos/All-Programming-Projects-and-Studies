#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int test;
    string test2 = "Hello";

    cout << "Please enter a value:" << endl;
    cin >> test;

    cout << "Value multiplied by 100 is:\n" << test * 100;

    cout << test2;
    return 0;
}