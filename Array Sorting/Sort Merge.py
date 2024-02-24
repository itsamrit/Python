//Part of divide and conquer
//You can also find inversion with merge sort. Inversion means :a[i]>a[j] & i<j
//t.c=0(n*logn)              s.c=o(n) because of left[n/2] + right[n/2].


class Solution:
    inversion = 0

    def merge(self, arr, l, m, r):
	//🟩😊😊start to mid and mid to end are already sorted so just compare arr[i] and arr[j] && MERGE THEM
        temp = []
        i = l
        j = m + 1
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
                self.inversion += m - i + 1
	//To find pairs/inversion such that arr[i]>2*arr[j] with i<j  : if(arr[i] <= arr[j]*2)  && Rest same in above loop
        while i <= m:
            temp.append(arr[i])
            i += 1
        while j <= r:
            temp.append(arr[j])
            j += 1
        for i in range(l, r + 1):
            arr[i] = temp[i - l]
            i += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)

    def inversionCount(self, arr, n):
        self.inversion = 0
        self.mergeSort(arr, 0, len(arr) - 1)
        return self.inversion



class Solution:
    inversion = 0

    def merge(self, arr, l, m, r):
	//🟩😊😊start to mid and mid to end are already sorted so just compare arr[i] and arr[j] && MERGE THEM
        temp = []
        i = l
        j = m + 1
        while i <= m and j <= r:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
                self.inversion += m - i + 1
	//To find pairs/inversion such that arr[i]>2*arr[j] with i<j  : if(arr[i] <= arr[j]*2)  && Rest same in above loop
        while i <= m:
            temp.append(arr[i])
            i += 1
        while j <= r:
            temp.append(arr[j])
            j += 1
        for i in range(l, r + 1):
            arr[i] = temp[i - l]
            i += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)

    def inversionCount(self, arr, n):
        self.inversion = 0
        self.mergeSort(arr, 0, len(arr) - 1)
        return self.inversion
    




    def inversionCount(self, arr, n):
        self.inversion = 0
        self.mergeSort(arr, 0, len(arr) - 1)
        return self.inversion