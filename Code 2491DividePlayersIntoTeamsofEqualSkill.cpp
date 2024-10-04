class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end()); 
        int Sum_ans = skill[0] + skill[skill.size() - 1];
        vector<vector<int> > ans;

        for (int i = 0; i < skill.size() / 2; i++ ){
            int tmp = skill[i] + skill[skill.size() - 1 - i];
            if (tmp != Sum_ans)
                return -1;
            else{
                int ans1 = skill[i];
                ans.push_back(vector<int>());
                ans[i].push_back(ans1);
                ans[i].push_back(skill[skill.size() - 1 - i]);
            }
        }

        long long sum = 0;
        for (int i = 0; i < ans.size(); i++ ){
            sum += (ans[i][0]*ans[i][1]);
        }

        // for (auto x : skill) 
        //     cout << x << " ";

        // for(auto lst : ans){
        //     for(auto e : lst){
        //         cout<<e<<" ";
        //     }
        //     cout<<endl;
        // }

        return sum; 
    }
};
