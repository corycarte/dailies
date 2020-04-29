struct PathNode
{
    float pos[2]; // required
    bool isSpawner; // required
    
    // Add additional fields here if needed.
    bool reachable;
    int id;
};

float EuclideanDistance (float A[2], float B[2])
{
    float x1 = max(A[0], B[0]);
    float x2 = min(A[0], B[0]);

    float y1 = max(A[1], B[1]);
    float y2 = min(A[1], B[1]);

    return sqrt((pow((x1 - x2), 2)) + (pow((y1 - y2), 2)));
}

bool TestPoint(float A[2], float B[2])
{
    return (EuclideanDistance(A, B) <= 16);
}

void Merge(int a[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for(i = 0; i < n1; ++i)
        L[i] = a[l+i];

    for(j = 0; j < n2; ++j)
        R[j] = a[m+1+j];

    i = j = 0;
    k = l;

    while (i < n1 && j < n2) {
        if (L[i] < R[j]) {
            a[k] = L[i++];
        }
        else {
            a[k] = R[j++];
        }
        ++k;
    }

    while (i < n1)
        a[k++] = L[i++];

    while (j < n2)
        a[k++] = R[j++];
}

void MergeSort(int a[], int l, int r)
{
    if (l < r) {
        int m = (l + r) / 2;
        MergeSort(a, l, m);
        MergeSort(a, m+1, r);
        Merge(a, l, m, r);
    }
}

void ResizeSolutionArray(int* a, int* resCount)
{
    std::cout << "Calling resize\n";
    int* temp = new int[*resCount * 2];
    for(int i = 0; i < *resCount; ++i) {
        temp[i] = a[i];
    }
    *resCount *= 2;
    a = temp;
}

/*
 * Complete the function below.
 */
int* GetReachableNodes( int nodeCount, PathNode* nodes, int* resultIndexCount )
{
    
    std::queue<int> proc;
    std::unordered_map<int, std::unordered_map<int, int>> availableX;
    std::unordered_map<int, std::unordered_map<int, int>> availableY;
    std::set<int>solTemp;
    
    // Collect Spawn Points
    for(int i = 0; i < nodeCount; ++i) {
        if (nodes[i].isSpawner) {
            proc.push(i);
            solTemp.insert(i);
        }
        else {
            availableX[nodes[i].pos[0]][nodes[i].pos[1]] = i;
            availableY[nodes[i].pos[1]][nodes[i].pos[0]] = i;
        }
    }

    std::unordered_map<int, std::unordered_map<int, int>>::iterator search;

    while(!proc.empty()) {
        int curr = proc.front();
        proc.pop();

        float relativeX = nodes[curr].pos[0] - 16;
        float relativeY = nodes[curr].pos[1] - 16;

        while (relativeX <= nodes[curr].pos[0] + 16) {
            search = availableX.find(relativeX);
            if (search != availableX.end()) {
                for(auto& y : availableX[search->first]) {
                    float testPoint[2] = { relativeX, (float)y.first };
                    if(TestPoint(nodes[curr].pos, testPoint)) {
                            proc.push(y.second);
                            solTemp.insert(y.second);
                            availableX[search->first].erase(testPoint[1]);
                    }
                }
            }
            ++relativeX;
        }

        relativeX = nodes[curr].pos[0];
        relativeY = nodes[curr].pos[1] - 16;

        while (relativeY <= nodes[curr].pos[1] + 16) {
            search = availableY.find(relativeY);
            if (search != availableY.end()) {
                for(auto& x : availableY[search->first]) {
                    float testPoint[2] = { (float)x.first, (float)search->first };
                    if(TestPoint(nodes[curr].pos, testPoint)) {
                            proc.push(x.second);
                            solTemp.insert(x.second);
                            availableY[search->first].erase(testPoint[0]);
                    }
                }
            }
            ++relativeY;
        }
    }

    int* result = new int[solTemp.size()];

    int i = 0;
    for(auto& j : solTemp)
        result[i++] = j;

    *resultIndexCount = solTemp.size();
    MergeSort(result, 0, *resultIndexCount - 1);

    return result;
}