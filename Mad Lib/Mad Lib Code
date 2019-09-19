/***********************************************************************
* Program:
*    Project 10, Mad Lib 
*    Sister Hansen, CS 124
* Author:
*    Aaron Jones
* Summary: 
*    This program will take in the users response for 
*    each question asked that will replace the original
*    spot in the displayed story. continually this program
*    will check the file that's read into the stories 
*    multi-dimensional array and if it's a question or a 
*    punctuation tag then it will either prompt the user 
*    or change the story to the correct punctuation/whitespace.
*
*    Estimated:  2.25 hrs   
*    Actual:     4.30 hrs
*      The hardest part was getting each whitespace inside of the 
*      array to display correctly. 
************************************************************************/

#include <iostream>
#include <fstream>
using namespace std;

/**********************************************************************
 * Prompting the user for the Mad Lib text file that will contain the
 * original story for the game to be played.
 ***********************************************************************/
void getFileName(char fileName[])
{
   cout << "Please enter the filename of the Mad Lib: ";
   cin  >> fileName;
}

/**********************************************************************
 * Checks to see if the character inside of the array is a punctuation
 * tag and if not returns false.
 ***********************************************************************/
bool isPunctuationTag(char word[])
{
   if (word[0] == ':' && ispunct(word[1]))
      return true;
   else
      return false;
}

/**********************************************************************
 * Checks to see if the character inside of the array is a question
 * tag and if not returns false.
 ***********************************************************************/
bool isQuestionTag(char word[])
{
   if (word[0] == ':' && isalpha(word[1]))
      return true;
   else
      return false;
}

/**********************************************************************
 * Loops through the story array and takes the questions in the original
 * text and redefines these questions so they are readable to the user.
 ***********************************************************************/
void replaceQuestionTag(char word[])
{
   cout << '\t' << (char)toupper(word[1]);
   
   for (int i = 2; word[i]; i++)
   {
      if (word[i] == '_')
      {
         cout << ' ';
      }
      else 
      {
         cout << (char)tolower(word[i]);
      }
   }
   cout << ": ";
   cin.getline(word, 256);
}

/**********************************************************************
 * Reading the Mad Lib file and storing it into the story array.
 * Additionally this function will bypass main and call two different 
 * functions that will prompt the user for certain questions. The users
 * response will be stored into the array and displayed into the final
 * product. 
 ***********************************************************************/
void readFile(char fileName[], char story[][32], int &numWords)
{

   ifstream fin(fileName);
   if (fin.fail())
   {
      cout << "Error reading file \"" << fileName << "\"" << endl;
   }
   while (fin >> story[numWords])
   {
      if (isQuestionTag(story[numWords]))
      {
         replaceQuestionTag(story[numWords]);
      }
      numWords++;
   }
   fin.close();
}

/**********************************************************************
 * Prompting the user if they want to play the Mad Lib game again.
 * this will be passed through a while loop that's inside of Main.
 ***********************************************************************/
bool askplayAgain()
{
   char answer;

   cout << "Do you want to play again (y/n)? ";
   cin  >> answer;
      
   if (answer == 'y')
   {
      return true;
   }
   else 
   {
      return false;
   }
}

/**********************************************************************
 * Displaying the final product to the user by passing in an array of
 * questions as well as words. Punctuation tags will be changed to the 
 * correct format and these tags will check for white space. Lastly
 * this function will check to see if the first character of the array
 * is a word or a punctuation tag and changed accordingly. 
 ***********************************************************************/
void displayStory(char story[][32], int numWords)
{
   cout << "\n";
   
   for (int i = 0; i < numWords; i++)
   {
      if (isalpha(story[i][0]) && isalpha(story[i + 1][0]))
      {
         cout << story[i] << " ";
      }
      else if (isPunctuationTag(story[i]) && story[i][1] == '!')
      {
         if (isalpha(story[i - 1][0]))
         {
            cout << story[i - 1] << '\n';
         }
         else 
         {
            cout << '\n';
         }
      }
      else if (isPunctuationTag(story[i]) && story[i][1] == '.')
      {
         if (isalpha(story[i - 1][1]) && story[i + 1][1] == '!')
         {
            cout << story[i - 1] << '.';
         }
         else if (isalpha(story[i - 1][1]) && isalpha(story[i + 1][0]))
         {
            cout << story[i - 1] << ". ";
         }
         else if (isalpha(story[i - 1][1]) && story[i + 1][1] == '>')
         {
            cout << story[i - 1] << '.';
         }
         else if (isalpha(story[i - 1][0]))
         {
            cout << story[i - 1] << '.';
         }
      }
      else if (isPunctuationTag(story[i]) && story[i][1] == ',')
      {
         if (isalpha(story[i - 1][0]) && isalpha(story[i + 1][0]))
         {
            cout << story[i - 1] << ", ";
         }
         else if (isalpha(story[i - 1][0]) && story[i + 1][1] == '!')
         {
            // cerr << "story[i-1]= " << story[i - 1] << endl;
            cout << story[i - 1] << ',';
         }
      }
      else if (isalpha(story[i][1]) && isalpha(story[i + 1][1]))
      {
         // cerr << "story[i] = " << story[i] << endl;
         cout << story[i] << " ";
      }
      // Open double quote '<' = "word
      else if (isPunctuationTag(story[i]) && story[i][1] == '<')
      {
         if (isalpha(story[i - 1][0]) && isalpha(story[i + 1][0]))
         {
            cout << story[i - 1] << " \"";
         }
         else if (isPunctuationTag(story[i - 1]))
         {
            cout << '\"';
         }
      }
      // Closed double quote '>' = word"
      else if (isPunctuationTag(story[i]) && story[i][1] == '>')
      {
         if (isalpha(story[i - 1][0]) && isalpha(story[i + 1][0]))
         {
            cout << story[i - 1] << "\" ";
         }
         else if (isalpha(story[i - 1][0]) && story[i + 1][1] == '!')
         {
            cout << story[i - 1] <<  '\"';
         }
         else if (story[i - 1][1] == '.' && isalpha(story[i + 1][0]))
         {
            cout << "\" ";
         }
         else if (story[i - 1][1] == '.' && story[i + 1][1] == '!')
         {
            cout << '\"';
         }
         else if (isalpha(story[i - 1][0]))
         {
            cout << story[i - 1] <<  "\" ";
         }
      }      
   }
   cout << "\n";
}

/**********************************************************************
 * Driver program for all the other functions. It will store multiple
 * arrays that will be used throughout the story and each variable will
 * be used through pass by reference. Lastly this function will use a
 * while loop to prompt the user if they want to play again or not.
 ***********************************************************************/
int main()
{
   char fileName[256];
   char story [256][32];
   int numWords = 0;
   
   getFileName(fileName);
   cin.ignore();
   readFile(fileName, story, numWords);
   displayStory(story, numWords);
   bool askplayAgain();
   
   while (askplayAgain())
   {
      char fileName[256];
      char story [256][32];
      int numWords = 0;
      getFileName(fileName);
      cin.ignore();
      readFile(fileName, story, numWords);
      displayStory(story, numWords);
   }
   cout << "Thank you for playing.\n";

   return 0;
}
