#include <algorithm>
class MinStack {
    std::vector<int> con;
    std::vector<int> min;
public:
    MinStack() {
    }
    
    void push(int val) {
        con.push_back(val);
        if(min.size() == 0){
            min.push_back(val);
        }else{
            min.push_back(std::min(val, min[min.size() - 1]));
        }
    }
    
    void pop() {
        con.pop_back();
        min.pop_back();
    }
    
    int top() {
        return con[con.size() - 1];
    }
    
    int getMin() {
        return min[min.size() - 1];
    }
};
