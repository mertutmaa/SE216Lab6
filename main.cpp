#include <iostream>


using namespace std;

double sum(double n){
	if (n == 1.0) return 1.0;
	return ((1 / n) + sum(n - 1) );
}

double sum() {
	double n;
	cout << "please enter a number: " << endl;
	cin >> n;
	double val = sum(n);
	return val;
}

int main(){
	double x = sum();
	cout << x << endl;
	return 0;
}
