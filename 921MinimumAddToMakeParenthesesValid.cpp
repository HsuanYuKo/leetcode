class Solution {
public:
    int minAddToMakeValid(string s) {
        vector<char> arr;
        for (int i = 0 ; i < s.length() ; i++){
            if (arr.size() > 0 && arr[arr.size() - 1] == '(' && s[i] == ')'){
                arr.pop_back();
            }
            else{
                arr.push_back(s[i]);
            }
        }
        return arr.size();
    }
};
