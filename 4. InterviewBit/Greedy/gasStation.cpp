int Solution::canCompleteCircuit(const vector<int> &gas, const vector<int> &cost) {
    int n = gas.size();
    //cout<<n<<endl;

    long long tank = 0;
    int in = -1;
    for( int i = 0; i < n; i++){
        int next = i;
        int flag = 0;
        int count = 0;
        tank = 0;
        while(count < n){
            tank += gas[next];
            if( tank >= cost[next])
                tank -= cost[next];

            else{
                count++;
                next = (next + 1) % n;
                flag = 1;
                break;
            }
            count++;
            next = (next + 1) % n;
        }

        if( count == n && !flag){
            in = i;
            break;
        }
        i = i + count - 1 ;
    }
    return in;
}
