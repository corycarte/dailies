/*

Arguments X and Y are pointers to null-terminated strings containing non-negative base-10 whole numbers

Allocated a return string containing the base 10 representation of the sum of X and Y (leading zeros are ok)

Sample IN
34
152

Sample OUT
186
OR
0186

*/


#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <assert.h>

using namespace std;



/*
 * Complete the function below.
 */
char* AddAsciiIntegers( const char* X, const char* Y)
{

}


int StartAddASCII() {
    FILE *f = fopen("AddASCII_Out.txt", "w");

    cout << "Enter X: ";
    string X;
    getline(cin, X);

    cout << "Enter Y: ";
    string Y;
    getline(cin, Y);
    
    int l = strlen(X.c_str());
    char* g = (char*)malloc( l );
    memset( g, 0xfe, l );
    free( g );
    
    const char* res = AddAsciiIntegers( X.c_str(), Y.c_str() );
    fprintf(f, "%s\n", res);
    
    fclose(f);
    // ignoring memory leak of "res" for flexibility.
    return 0;
}