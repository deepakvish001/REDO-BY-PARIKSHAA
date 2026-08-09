class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        x = (nums, queries)
        n = len(nums)
        def getfunc(length: int)-> int:
            if length <3:
                return 0
            return (length - 1) * (length -2) //2
        def merge(left:tuple, right:tuple)-> tuple:
            if left[0]==-1: return right
            if right[0]==-1: return left
            return(left[0],right[1],left[2]+right[2]+getfunc(right[0]-left[1]+1))
        tree = [(-1,-1,0)]*(2*n)
        def peak(i:int)->bool:
            if i<=0 or i>=n-1:
                return False
            return nums[i]>nums[i-1] and nums[i]>nums[i+1]
        for i in range(1,n-1):
            if peak(i):
                tree[n+i]=(i,i,0)
        for i in range(n-1, 0, -1):
            tree[i] = merge(tree[i<<1],tree[i<<1 | 1])
        def update(idx:int):
            if idx <= 0 or idx >= n-1:
                return
            p=idx+n
            tree[p] = (idx,idx,0) if peak(idx) else (-1,-1,0)
            p>>=1
            while p>0:
                tree[p] = merge(tree[p<<1],tree[p<<1 | 1])
                p>>=1
        def query(l:int,r:int)->tuple:
            leftr = (-1,-1,0)
            rightr=(-1,-1,0)
            l += n
            r += n
            while l<=r:
                if l & 1:
                    leftr = merge(leftr, tree[l])
                    l += 1
                if not (r & 1):
                    rightr = merge(tree[r], rightr)
                    r -= 1
                l>>= 1
                r>>= 1
            return merge(leftr, rightr)
        ans = []
        for q in queries:
            if q[0] == 1:
                _, l, r = q
                if r - l + 1 < 3:
                    ans.append(0)
                else:
                    res = query(l+1,r-1)
                    tsum = getfunc(r-l+1)
                    if res[0]==-1:
                        ans.append(0)
                    else:
                        z = res[2]+getfunc(res[0]-l+1)+getfunc(r-res[1]+1)
                        ans.append(tsum-z)
            else:
                _,idx,val = q
                nums[idx] = val
                for i in (idx-1,idx,idx+1):
                    update(i)
        return ans