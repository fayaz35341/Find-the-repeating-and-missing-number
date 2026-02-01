class Solution {
    findMissingRepeatingNumbers(arr) {
        let n=arr.length
        let s1=0
        let s2=0
        let s1n=(n*(n+1))/2
        let s2n= (n*(n+1)*(2*n+1))/6
        for (let i=0; i<n;i++){
            s1+=arr[i]
            s2+=(arr[i]*arr[i])
        }
        let val1= s1-s1n
        let val2 =s2-s2n
        val2=(val2/val1)
        let x=(val1+val2)/2
        let y=x-val1
        return [Math.floor(x),Math.floor(y)] 

    }
}
