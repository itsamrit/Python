# //Part of divide and conquer
# //You can also find inversion with merge sort. Inversion means :a[i]>a[j] & i<j
# //t.c=0(n*logn)              s.c=o(n) because of left[n/2] + right[n/2].


class Solution:
    inversion = 0

    def mergeSort(self, arr, l, r):
        if l>=r: return
	m = floor((l + r)/2)               #dont use ceil in python CEIL gives wrong in python , can use ROUND but it also provides wrong in some casess
	self.mergeSort(arr, l, m)
	self.mergeSort(arr, m + 1, r)

	#🟩😊😊start to mid and mid to end are already sorted so just compare arr[i] and arr[j] && MERGE THEM
	temp = []
        i = l
        j = m + 1
        while i <= m and j <= r:
            if arr[i] > arr[j]:                  #To find pairs/inversion such that arr[i]>2*arr[j] with i<j  : if arr[i] > 2*arr[j]
		self.inversion += m - i + 1
		temp.append(arr[j])
                j += 1
            else:
                temp.append(arr[i])
                i += 1
                
	temp.extend(arr[i:m+1])  
        temp.extend(arr[j:r+1])
        arr[l:r+1] = temp

    def inversionCount(self, arr, n):
        self.inversion = 0
        self.mergeSort(arr, 0, len(arr) - 1)
        return self.inversion
