#include <string>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <sstream>
using namespace std;
int main()
{
  ifstream myfile("bible.txt");
  string line;
  char delim = ' ';
  string token;
  unordered_map<string, int> result;
  if (myfile.is_open())
  {
    while (getline(myfile, line))
    {
      stringstream ss(line);
      while (ss >> token)
      {
        if (result.find(token) == result.end())
        {
          result[token] = 1;
        }
        else
        {
          result[token]++;
        }
      }
    }
  }
  for (auto entry : result)
  {
    cout << entry.first << ": " << entry.second << endl;
  }
  return 0;
}
