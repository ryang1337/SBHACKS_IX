#include <iostream>
#include <string>
// #ifdef _WIN32
// #include <Windows.h>
// #else
#include <unistd.h>
// #endif

using namespace std;

int main (){
    while (true){
        cout << "enter ur equation sir" << endl;
        string str;
        getline(cin, str);
        // cin >> ws;
        cout << "calculating...." << endl;
        sleep(2);
        cout << endl;
        cout << "idk ehe try again? (Y/N)" <<endl;

        // cout << "" << endl;

        char c;
        cin >> c;
        getline(cin, str);        
        while (c != 'Y'&& c!= 'N'){
            // cout << c;
            cout << "wtf does that mean" << endl;
            
            cin >> c;
            getline(cin, str);   
        }
        
        if (c== 'N'){
            return 0;
        }
        cout << endl;
    }
}