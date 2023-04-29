class Solution {
public:
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        int size=security.size(),cnt=1;
        vector<int>pre(size,0),suf(size,0);
        pre[0]=1;
        for(int i=1;i<size;i++){
            if(security[i]<=security[i-1])
                cnt++;
            else
                cnt=1;
             pre[i]=cnt;
        }
        suf[size-1]=1;cnt=1;
        for(int i=size-2;i>=0;i--){
            if(security[i]<=security[i+1])
                cnt++;
            else
                cnt=1;
            suf[i]=cnt; 
        }
        vector<int>ans;
        for(int i=0;i<size;i++)
            if(pre[i]-1>=time && suf[i]-1>=time)
                ans.push_back(i);
        return ans;
    }
};