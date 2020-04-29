// Solution originally given on leetcode Oct 2019
// Runtime: 8 ms
// Memory Usage: 8.5 MB

class Solution {
public:

    std::string getOnes(int num) {
        if (num == 9) return "IX";
        if (num == 4) return "IV";

        std::string ret = "";

        if(num > 4) {
            ret.push_back('V');
            num -= 5;
        }

        ret.append(num, 'I');

        return ret;
    }

    std::string getTens(int num) {
        if (num == 4) return "XL";
        if (num == 9) return "XC";

        std::string ret = "";


        if (num > 4) {
            ret.push_back('L');
            num -= 5;
        }

        ret.append(num, 'X');

        return ret;
    }

    std::string getHuns(int num) {

        if(num == 4) return "CD";
        if(num == 9) return "CM";

        std::string ret = "";

        if (num > 4) {
            ret.push_back('D');
            num -= 5;
        }

        ret.append(num, 'C');
        return ret;
    }

    std::string getThou(int num) {
        std::string ret = "";

        ret.append(num, 'M');

        return ret;
    }

    string intToRoman(int num) {
        std::string ret = "";

        int curr = 0;

        while (num > 0) {
            if (curr == 0) ret.insert(0, getOnes(num % 10));
            if (curr == 1) ret.insert(0, getTens(num % 10));
            if (curr == 2) ret.insert(0, getHuns(num % 10));
            if (curr == 3) ret.insert(0, getThou(num % 10));
            num /= 10;
            ++curr;
        } // end while loop
        return ret;
    }
};
