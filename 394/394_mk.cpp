//这道题用栈即可解决，
//如果当前的字符为数位，解析出一个数字（连续的多个数位）并进栈
//如果当前的字符为字母或者左括号，直接进栈
//如果当前的字符为右括号，开始出栈，一直到左括号出栈，出栈序列反转后拼接成一个字符串，此时取出栈顶的数字（此时栈顶一定是数字，想想为什么？），就是这个字符串应该出现的次数，我们根据这个次数和字符串构造出新的字符串并进栈

#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution
{
public:
  string decodeString(string s)
  {
    string re;
    string temp = "";
    stack<string> st;
    if (s.length() == 0)
      return "";
    for (int i = 0; i < s.length(); i++)
    {
      cout << "S[" << i << "]=" << s[i] << '.';
      if (s[i] >= '0' && s[i] <= '9')
      { //数字的判断
        while (s[i] >= '0' && s[i] <= '9')
        {
          temp += s[i];
          i++;
        }
        cout << temp;
        cout << ';';
        st.push(temp);
        st.push("[");
        //i++;
        temp = "";
      }
      if (s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z')
      { //字母的判断
        while (s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z')
        {
          temp += s[i];
          i++;
        }
        if (s[i] >= '0' && s[i] <= '9')
          i--;
        cout << temp;
        cout << ';';
        st.push(temp);
        temp = "";
      }
      if (s[i] == ']')
      { //判断到]开始出栈
        string top = "";
        while (st.top() != "[")
        {
          string temp2 = st.top();
          top = temp2 + top;
          cout << top;
          st.pop();
        }
        st.pop();
        int num = stoi(st.top());
        st.pop();
        cout << "top:";
        cout << top << ';';
        cout << "num:";
        cout << num << ';';
        temp = "";
        // cout<<st.size();
        for (int i = 0; i < num; i++)
          temp += top;
        st.push(temp);
        cout << temp;
        cout << endl;
        /*if (!st.size())
        { //为空直接入栈，不为空说明前面有字符串，需要拼接
          // cout<<st.size();
          st.push(temp);
          // cout<<st.size();
        }
        else
        {
          string temp2 = st.top() + temp;
          st.pop();
          st.push(temp2);
        }*/
        temp = "";
      }
    }
    if (st.size() != 1)
    {
      int x = st.size();
      cout << x << ';';
      for (int i = 0; i < x; i++)
      { //将栈中所有字符串拼接，针对3[a]bc的情况
        string temp2 = "";
        temp = "";
        temp = st.top();
        st.pop();
        temp2 = st.top();
        st.pop();
        st.push(temp2 + temp);
        cout << st.top() << ';';
        if(i>=(x-2)) return st.top();
      }
    }
    else
      return st.top();
    cout << st.top();
    return st.top();
  }
};

int main()
{
  Solution a;
  cout << a.decodeString("2[a]3[b]4[c]5[d]");
  return 0;
}