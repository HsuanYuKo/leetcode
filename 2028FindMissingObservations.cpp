class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int sum_roll = rolls.size() + n;
        int sum=0;
        for (int i = 0; i<rolls.size();i++){
            sum+=rolls[i];
        }
        int lack = (sum_roll*mean)-sum;
        vector<int> ans;
        if (lack>n*6 || lack <0||lack/n==0){
            return ans;
        }
        else{
            for (int i=0;i<n;i++){
                ans.push_back(lack/n);
            }
            if (lack%n!=0){
                for (int i=0;i<lack%n;i++){
                    ans[i]+=1;
                }
            }
        }
        return ans;
    }
};
