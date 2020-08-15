#include <stdio.h>

bool isPalindrome(char *s){
    int bias_left = 0;
    int bias_right = 1;

    int str_len = strlen(s);
    for(int i=0; i<str_len; i++){
        //알파벳이나 숫자가 아닌 경우 계속 뛰어넘기
        while(!isalnum(s[i+bias_left])){
            bias_left++;
            if(i+bias_left == str_len) 
                return true;
        }
        while (!isalnum(s[str_len-i-bias_right])){
            bias_right++;
        }

        if(i+bias_left >= str_len - i - bias_right)
            break;
        //팰린드롬 비교
        if (tolower(s[i+bias_right]) != tolower(s[str_len-i-bias_right]))
            return false;
    }
    return true;
}
