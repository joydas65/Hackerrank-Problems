#include <bits/stdc++.h>

using namespace std;

// Complete the maximizingXor function below.
int FindMax(int a, int b){
    return a>b?a:b;
}
int maximizingXor(int l, int r) {
    int ans = 0;
    for(int i = l; i <= r; i++){
        for(int j = i; j <= r; j++){
            if(i==j)
            continue;
            ans = FindMax(ans, i^j);
        }
    }
    return ans;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int l;
    cin >> l;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int r;
    cin >> r;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = maximizingXor(l, r);

    fout << result << "\n";

    fout.close();

    return 0;
}
