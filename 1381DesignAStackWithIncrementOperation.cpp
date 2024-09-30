class CustomStack {
public:
    vector<int> arr;
    int capacity;

    CustomStack(int maxSize) {
        capacity = maxSize;
    }
    
    void push(int x) {
        if (int(arr.size()) < capacity)
            arr.push_back(x);
    }
    
    int pop() {
        if (arr.size() == 0)
            return -1;
        else{
            int pop_num = arr[arr.size() -1];
            arr.pop_back();
            return pop_num;
        }
    }
    
    void increment(int k, int val) {
        if (k > arr.size()){
            for (int i = 0 ; i < arr.size() ; i++){
                arr[i] += val;
            }
        }
        else{
            for (int i = 0 ; i < k ; i++){
                arr[i] += val;
            }
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
