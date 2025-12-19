
#include <iostream>
#include <string>
using namespace std;


int add(int x, int y);
int sub(int x, int y);
int mult(int x, int y);
int divide(int x, int y);



int main(){

    int num1, num2;
    char operation;
    cout << "Enter first number: ";
    cin >> num1;
    cout << endl << "Enter second number: ";
    cin >> num2;
    cout << "Enter operation (+, -, *, /): ";
    cin >> operation;

    int res;
    switch (operation) {
        case '+':
            res = add(num1, num2);
            cout << res << endl;
            break;

        case '-':
            res = sub(num1, num2);
            cout << res << endl;
            break;

        case '*':
            res = mult(num1, num2);
            cout << res << endl;
            break;

        case '/':
            res = divide(num1, num2);
            cout << res << endl;
            break;

        default:
            cout << "INVALID INPUT PLEASE TRY AGAIN" << endl;
    }








}


int add(int x, int y) {
    return x + y;
}

int sub(int x, int y) {
    return x - y;
}

int mult(int x, int y) {
    return x * y;
}

int divide(int x, int y) {
    if (y == 0) {
        cout << "Error! Divison by 0. Please input another number" << endl;
        return 0;
    }
    else {
        return x / y;
    }
}
