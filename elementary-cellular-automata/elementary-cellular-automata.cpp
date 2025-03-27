#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>



using namespace std;


void printVector(vector<string> vector) {
    for (int y= 0; y < vector.size(); y++) {
        cout << vector[y] << endl;
    }
}


string generateGrid(int stringLen, bool isStartingGrid) {
    string out(stringLen, ' ');
    if (isStartingGrid == true) out.at((stringLen / 2)+1) = '1';
    return out;
}


string intTo8bitBinary(long num) {
    // max is 8 bits since there are 256 rules
    vector<long> powerOfTwos = {128, 64, 32, 16, 8, 4, 2, 1};

    string out = "        ";

    while (num > 0) {
        

        for (int index = 0; index < 8; index ++) {
            if (powerOfTwos[index]> num) {
               continue; 
            }  
            
            num = num - powerOfTwos[index];
            
            out.at(7-index) = '1';   
        }
    }

    string reverseout = string(out.rbegin(), out.rend());

    return reverseout;
}


unordered_map<string, string> generateDict(string ruleInBinary) {
    unordered_map<string, string> out = {
        {"111", string(1, ruleInBinary[0])},
        {"11 ", string(1, ruleInBinary[1])},
        {"1 1", string(1, ruleInBinary[2])},
        {"1  ", string(1, ruleInBinary[3])},
        {" 11", string(1, ruleInBinary[4])},
        {" 1 ", string(1, ruleInBinary[5])},
        {"  1", string(1, ruleInBinary[6])},
        {"   ", string(1, ruleInBinary[7])}
    };

    return out;
}


string calculateState(unordered_map<string, string> ruleDict, char leftChar, char currentChar, char rightChar){
    string neighborhood({leftChar, currentChar, rightChar});
    string out = ruleDict[neighborhood];
    return out;

}



string updateCells(string grid, unordered_map<string, string> ruleDict) {
    string nextGrid = generateGrid(grid.length(), false);

    for (int i =0; i < grid.length(); i++) {
        char leftChar = grid[(i-1+grid.length()) % grid.length()];
        char rightChar = grid[(i+1+grid.length()) % grid.length()];
        char currentChar = grid[i];

        string nextState = calculateState(ruleDict, leftChar, currentChar, rightChar);
        nextGrid.at(i) = nextState[0]; //convert from string to char

    }

    return nextGrid;

}



void cellularAutomata(int rule, int rows) {
    string ruleInBinary = intTo8bitBinary(rule);
    unordered_map<string, string> ruleDict = generateDict(ruleInBinary);
    string grid = generateGrid(201, true);

    for (int y =0; y < rows; y++) {
        cout << grid << endl;
        string nextGrid = updateCells(grid, ruleDict);
        grid = nextGrid;
        
    }

}

int main() {
    

    int rule = 22;
    string ruleBinary = intTo8bitBinary(rule);
    cellularAutomata(rule, 200);
    

    return 0;
}