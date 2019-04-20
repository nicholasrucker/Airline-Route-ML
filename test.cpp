
#include <vector>


int main(int argc, char** argv) {

	vector<int> firstVec;
	vector<int> secondVec;

	for(int i = 0; i < 5; i++)
	{
		firstVec.push_back(i*2);
		secondVec.push_back(i*3);
	}

	sort(firstVec.begin(), firstVec.end());
	sort(secondVec.begin(), secondVec.end());

	int closestNum;
	int target = 10;

	for(int i = 0; i < firstVec.size(); i++)
	{
		for(int j = 0; j < secondVec.size(); j++)
		{
			if( i == 0 && j == 0)
				closestNum = firstVec.at(i) + secondVec.at(j);
			else if(target - firstVec.at(i) + secondVec.at(j) < target - closestNum)
				closestNum = firstVec.at(i) + secondVec.at(j);
		}
	}
}