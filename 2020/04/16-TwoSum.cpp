#IFNDEF TWOSUM_CPP
#DEFINE TWOSUM_CPP


class Solution {
public:
  vector<int> twoSum(vector<int>& nums, int target) {
    std::unordered_map<int, int> sMap;
    std::vector<int> sol(2, -1);

    for(size_t x = 0; x < nums.size(); ++x) {
      unordered_map<int, int>::iterator search;
      if ((search = sMap.find(nums[x])) != sMap.end()) {
	sol[0] = search->second;
	sol[1] = x;

	return sol;
      } else {
	sMap[(target - nums[x])] = x;
      }
    }

    return sol;
  }

}

#ENDIF
