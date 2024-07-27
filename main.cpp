#include <iostream>

using namespace std;

int main() {

    int roomCapacity;
    int numberOfPeople;

    cout << "What is the maximum room capacity? ";
    cin >> roomCapacity;

    cout << "What is the number of people who will attend the meeting? ";
    cin >> numberOfPeople;

    if (numberOfPeople <= roomCapacity) {
        int addlPeople = roomCapacity - numberOfPeople;
        cout << "It is legal to hold the meeting\n" << endl;
        cout << "An additional " << addlPeople << " people may legally attend the meeting." << endl;
    } else {
        int excluded_people = numberOfPeople - roomCapacity;
        cout << "The meeting cannot be held as planned due to fire regulations." << endl;
        cout << excluded_people << " people must be excluded in order to meet fire regulations." << endl;
    }

    return 0;
}