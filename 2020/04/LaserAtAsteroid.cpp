/*

The player fires a laser at a spherical asteroid. Implement a function that returns true if the laser hits

Sample input:
laser start = 1, 0, 0
laser direction = 0.5, 1, 0
asteroid position = 2, 4, 1
asteroid radius = 4

Sample OUT
1


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
bool LaserHitsAsteroid( float laserStart[3], float laserDir[3], float asteroidPos[3], float asteroidRadius )
{

}


/*

int main() {
    FILE *f = fopen(getenv("OUTPUT_PATH"), "w");
    bool res;
    
    float _laserStart[3];
    float _laserDir[3];
    float _asteroidPos[3];
    float _asteroidRadius;
    
    int argCount = scanf( "%f, %f, %f\n%f, %f, %f\n%f, %f, %f\n%f", &_laserStart[0], &_laserStart[1], &_laserStart[2], &_laserDir[0], &_laserDir[1], &_laserDir[2], &_asteroidPos[0], &_asteroidPos[1], &_asteroidPos[2], &_asteroidRadius );
    
    if ( argCount == 10 )
    {
        res = LaserHitsAsteroid( _laserStart, _laserDir, _asteroidPos, _asteroidRadius );
        fprintf(f, "%d\n", res ? 1 : 0);
    }
    else
    {
        fprintf( f, "Expected input format:\nx y z, x y z, x y z, radius\n" );
    }
    
    fclose(f);
    return 0;
}

*/