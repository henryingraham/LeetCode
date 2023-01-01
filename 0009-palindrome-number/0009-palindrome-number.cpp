class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0){
            return false;
        }
        unsigned int result = 0;
        unsigned int remainder;
        unsigned int y = x;
        while(y != 0){
            remainder = y % 10;
            result = result*10 + remainder;
            y /= 10;
        }
        if(result == x){
            return true;
        }
        else{
            return false;
        }
        
    }
};