#include<bits/stdc++.h>
using namespace std;

#include "../Solutions/SampleSolution.cpp"

int main() {
    Solution sol;
    vector<int> arr = {2, 7, 11, 15};
    vector<int> ss = sol.twoSum(arr, 9);

    for (int num : ss) {
        cout << num << " ";
    }
    cout << endl;
}