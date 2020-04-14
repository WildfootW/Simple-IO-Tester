/*
 * Version 
 * Author: WildfootW
 * GitHub: github.com/WildfootW
 * Copyleft (C) 2020 WildfootW all rights reversed
 *
 */


#include <iostream>

using namespace std;

char shift_char(char in, int shift)
{
    if('A' <= in && in <= 'Z')
        return (in + shift - 'A') % 26 + 'A';
    if('a' <= in && in <= 'z')
        return (in + shift - 'a') % 26 + 'a';
    if('0' <= in && in <= '9')
        return (in + shift - '0') % 10 + '0';
    return in;
}

int main()
{
    string str;
    while(getline(cin, str))
    {
        for(int i = 0;i < str.length();++i)
        {
            cout << shift_char(str[i], 7);
        }
        cout << endl;
    }

    return 0;
}

