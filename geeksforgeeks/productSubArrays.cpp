int productSubArrays(int arr[], int n)
{
    int i, j;
    long long int result = 1;
    for( i = 0 ; i < n ; i++ )
    {
        long long int product = 1;
        for( j = i ; j < n ; j++ )
        {
            product = product * arr[j];
            result = result * product;
        }
    }
    return result;
}