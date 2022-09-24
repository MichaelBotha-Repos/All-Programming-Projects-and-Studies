/**************************************************************
     Stop Sequence Display version Beta
     Author: Michael Botha
     Email: mbotha88@gmail.com

     Changes:
     
 *************************************************************/


#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct TRAIN_STATION
{
    string name = "";
    bool stop = false;
};

int main(int argc, char * argv[])
{
    struct TRAIN_STATION all_stations[20];  // Assume a max of 20 stations 
    ifstream text_file;
    int number_of_stations = 0, number_of_stops = 0, number_of_express = 0; 
    int express_stations_between_stops[20] = {0};
    char file_char; // Use to read a single character at a time from the file stream 
    string stopping_stations[20], express_stations[20]; // Stores names of stations
    bool debug_flag = false; // Enable to display helpful information 

    if(argc >2) 
    {
        cout << "You have entered too many arguments";
        text_file.close();
        return 0;
    }
    else
    {
        text_file.open(argv[1]);
        if(text_file.fail() == true)
        {
            cout << "You have entered an incorrect path or path format";
            text_file.close();
            return 0;
        }
    }

    // Line 48-142 is primarily for reading the data from the text
    // file and validating the inputs
    int comma_count = 0, bool_ready_flag = 0;
    string is_stop = "";
    while(!text_file.eof())
    {   
        text_file.get(file_char); 

        // when the EOF is reached the last character read still remains 
        // therefore set the current iteration to the necessary newline character
        if(text_file.eof())
        {
            file_char = '\n';
            text_file.close();
        }

        // Remember when a comma is reached to build the ", " delimiter
        if(file_char == ',') 
        {
            ++comma_count;
            continue;
        }
        else if(comma_count == 1 && file_char == ' ') //check for the ", " delimiter
        {
            bool_ready_flag = 1;
            continue;
        }

        // Ensure that the relevant name is made of appropriate
        // characters: capital/lowercase letter, an apostraphe, hyphen, or space 
        if(bool_ready_flag == 0 && 
            (   
                (file_char > 64 && file_char < 90) || 
                (file_char > 96 && file_char < 123) || 
                (file_char == '-')|| 
                (file_char == '\'') ||
                (file_char == ' ')
            )   
        )
        {
            all_stations[number_of_stations].name += file_char; //conacatenate char to station name in appropriate struct
        }
        else if(bool_ready_flag == 1)
        {
            if( 
                file_char == 'F' ||
                file_char == 'a' ||
                file_char == 'l' ||
                file_char == 's' ||
                file_char == 'e' ||
                file_char == 'T' ||
                file_char == 'r' ||
                file_char == 'u' 
              )
            {
                is_stop += file_char; // Try build bool value through concatenation
            }
            else if(file_char == ' ')
            {
                continue;
            }
            else if(file_char == '\n') // Once an EOL is reached the previous bool must be validated
            {    
                if(is_stop == "True")
                {
                    all_stations[number_of_stations].stop = true;
                }
                else if(is_stop == "False")
                {
                    all_stations[number_of_stations].stop = false;
                }
                else
                {
                    cout << "Incorrect format in text - False/True not correct format";
                    return 1;
                }
                is_stop.clear();
                comma_count--;
                ++number_of_stations;
                bool_ready_flag = 0;
            }
            else
            {
                cout<< "incorrect Boolean format";
                text_file.close();
                return 0;
            }
        }
        else if(file_char == '\n')
        {
            continue;
        }
        else
        {   
            if(file_char == '\n' && text_file.eof())
            {
                break;
            }
            else
            {
                cout << "Incorrect format in text";
                text_file.close();
                return 0;
            } 
        }
    }
    
    // Line 149-172 Gathers statistics about the events and sequencing pertaining to the route 
    int x = 0;
    for(int i=0; i < number_of_stations; i++)
    {
        if(debug_flag)
        {
            cout << endl << all_stations[i].name << "--->" << all_stations[i].stop;
        }
        
        // Determine data related to stopping stations
        if(all_stations[i].stop == true)
        {   
            stopping_stations[number_of_stops] = all_stations[i].name;
            number_of_stops ++;
            x++;       
        }
        else //determine data related to express stations 
        {
            express_stations[number_of_express] = all_stations[i].name;
            number_of_express++;
            ++express_stations_between_stops[x];
        }
    }

    // Display data related to trips
    if(debug_flag)
    {
        cout << endl << number_of_stops << endl << number_of_express << endl << number_of_stations << endl;
    }
    

    // Line 180-215 outputs information according to events and sequencing 
    if(number_of_stations == 2)
    {
        cout << "\nThis train stops at " << stopping_stations[0] << " and " << stopping_stations[1] << " only";
    }
    else if(number_of_stations == number_of_stops)
    {
        cout << "\nThis train stops at all stations";
    }
    else if(number_of_stops == (number_of_stations-1))
    {
        cout << "\nThis train stops at all stations except " << express_stations[0];
    }
    else if(number_of_express == (number_of_stations-2))
    {
        cout << "\nThis train runs express from " << stopping_stations[0] << " to " << stopping_stations[1];
    }
    else if (number_of_express == (number_of_stations-3))
    {
        cout << "\nThis train runs express from " << stopping_stations[0] << " to " << stopping_stations[2]
        << ", stopping only at " << stopping_stations[1];
    }
    else if(number_of_stops == 5) // One express section with no stops and one with one stop
    {
        //check correct sequence of stops and express stations
        if(express_stations_between_stops[4] >= 2 && express_stations_between_stops[3] == 0)
        {
            cout << "\nThis train runs express from " << stopping_stations[0] << " to " << stopping_stations[2]
            << ", stopping only at " << stopping_stations[1] << " then runs express from " << stopping_stations[3]
            << " to " << stopping_stations[4];
        }
    }
    else
    {
        cout << "No matching route sequencing found";
    }
    
    return 0;
}