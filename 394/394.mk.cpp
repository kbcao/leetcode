#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution {
 public:
  string decodeString(string s) {
    string re;
    string temp = "";
    stack<string> st;
    for (int i = 0; i < s.length(); i++) {
      if (s[i] >= '0' && s[i] <= '9') {
        while (s[i] >= '0' && s[i] <= '9') {
          temp += s[i];
          i++;
        }
        // cout << temp;
        // cout << ';';
        st.push(temp);
        st.push("[");
        i++;
        temp = "";
      }
      if (s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z') {
        while (s[i] >= 'a' && s[i] <= 'z' || s[i] >= 'A' && s[i] <= 'Z') {
          temp += s[i];
          i++;
        }
        if (s[i] >= '0' && s[i] <= '9') i--;
        // cout << temp;
        // cout << ';';
        st.push(temp);
        temp = "";
      }
      if (s[i] == ']') {
        string top = st.top();
        st.pop();
        st.pop();
        int num = stoi(st.top());
        st.pop();
        // cout << top;
        // cout << "top";
        // cout << num;
        // cout << "num";
        // cout << endl;
        temp = "";
        // cout<<st.size();
        for (int i = 0; i < num; i++) temp += top;
        if (!st.size()) {
          // cout<<st.size();
          st.push(temp);
          // cout<<st.size();
        } else {
          string temp2 = st.top() + temp;
          st.pop();
          st.push(temp2);
        }
        temp = "";
      }
    }
    //cout << st.size();
    for (int i = 0; i < st.size()-1; i++) {
      string temp2;
      temp = st.top();
      st.pop();
      temp2 = st.top();
      st.pop();
      st.push(temp2 + temp);
    }
    return st.top();
  }
};

int main() {
  Solution a;
  cout << a.decodeString("");
  return 0;
}