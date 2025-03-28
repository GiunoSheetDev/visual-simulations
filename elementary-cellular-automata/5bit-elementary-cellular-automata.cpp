#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>
#include <sstream>
#include <algorithm>


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


vector<string> generateAllPossibleCombinations(int numBits) {
    vector<string> result;
    
    // Handle edge case where numBits is 0
    if (numBits <= 0) {
        return result;
    }
    
    // Generate all possible combinations
    int maxNumber = (1 << numBits);  // 2^numBits
    
    for (int i = 0; i < maxNumber; i++) {
        stringstream ss;
        
        // Convert number to binary and pad with leading zeros
        int temp = i;
        for (int j = 0; j < numBits; j++) {
            ss << ((temp >> (numBits - 1 - j)) & 1);
        }
        
        result.push_back(ss.str());
    }
    
    return result;
}

string intTo32bitBinary(long num) {

    vector<long> powerOfTwos = {};
    
    for (int i = 32; i > 0; i--) {
        powerOfTwos.push_back(pow(2, i));
    }

    

    string out = string(32, ' ');

    while (num > 0) {
        

        for (int index = 0; index < out.length(); index ++) {
            if (powerOfTwos[index]> num) {
               continue; 
            }  
            
            num = num - powerOfTwos[index];
            
            out.at(out.length()-1-index) = '1';   
        }
    }

    string reverseout = string(out.rbegin(), out.rend());

    return reverseout;
}




unordered_map<string, string> generateDict(string ruleInBinary) {
    unordered_map<string, string> out;
    vector<string> possibleRules = generateAllPossibleCombinations(5);
    
    for (int i = possibleRules.size()-1; i >= 0; i --) {
        replace(possibleRules[i].begin(), possibleRules[i].end(), '0', ' ');
        out[possibleRules[i]] = string(1, ruleInBinary[i]);
        

    }

    return out;
}


string calculateState(unordered_map<string, string> ruleDict, char left2Char, char leftChar, char currentChar, char rightChar,  char right2Char){
    string neighborhood({left2Char, leftChar, currentChar, rightChar, right2Char});
    string out = ruleDict[neighborhood];
    return out;

}



string updateCells(string grid, unordered_map<string, string> ruleDict) {
    string nextGrid = generateGrid(grid.length(), false);

    for (int i =0; i < grid.length(); i++) {
        char left2Char = grid[(i-2+grid.length()) % grid.length()]; 
        char leftChar = grid[(i-1+grid.length()) % grid.length()];
        char rightChar = grid[(i+1+grid.length()) % grid.length()];
        char right2Char = grid[(i+2+grid.length()) % grid.length()];
        char currentChar = grid[i];

      

        string nextState = calculateState(ruleDict, left2Char, leftChar, currentChar, rightChar, right2Char);
        nextGrid.at(i) = nextState[0]; //convert from string to char

    }

    return nextGrid;

}



void cellularAutomata(int rule, int rows) {
    string ruleInBinary = intTo32bitBinary(rule);
    unordered_map<string, string> ruleDict = generateDict(ruleInBinary);
    string grid = generateGrid(201, true);

    for (int y =0; y < rows; y++) {
        cout << grid << endl;
        string nextGrid = updateCells(grid, ruleDict);
        grid = nextGrid;
        
    }

}



int main() {
    

    long rule = 204;
    string ruleBinary = intTo32bitBinary(rule);
    
    
    
    cellularAutomata(rule, 200);
    

    return 0;
}













