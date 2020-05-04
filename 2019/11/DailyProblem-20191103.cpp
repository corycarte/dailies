// DailyProblem-20191103.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>

bool check(std::vector<int> nums)
{
  bool mark = false;

  for (int i = 0; i < (nums.size() - 2); ++i) {
    if (nums[i] > nums[i + 1]) {
      if (mark) return false;
      else mark = true;
    }
  }

  return true;
}


int main()
{
  std::vector<int> test1, test2;

  test1.push_back(13);
  test1.push_back(4);
  test1.push_back(7);

  test2.push_back(5);
  test2.push_back(1);
  test2.push_back(3);
  test2.push_back(2);
  test2.push_back(5);

  std::cout << "Test 1: " << check(test1) << std::endl;
  std::cout << "Test 2: " << check(test2) << std::endl;


  return 0;
}
