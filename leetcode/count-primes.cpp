class Solution {
public:
    int countPrimes(int n) {
        if(n==0) return 0;
        int primes[n], count = 0;
        for(int i = 0; i <n ; i++)
            primes[i] = 1;
        for(int p = 2 ; p*p < n ; p++)
        {
            if(primes[p])
                for(int i = p*p ; i< n ; i+=p)
                    primes[i] = 0;
        }
        for(int i = 2 ; i < n ; i++)
        {
            if(primes[i])
                count++;
        }
        return count;
    }
};