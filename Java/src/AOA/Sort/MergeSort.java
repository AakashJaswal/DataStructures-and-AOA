package AOA.Sort;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class MergeSort {
    void divide(int ar[], int l, int h) {
        int middle;
        if (l < h) {
            middle = (l + h) / 2;
            divide(ar, l, middle);
            divide(ar, middle + 1, h);
            merge(ar, l, h, middle);
        }
    }

    void merge(int ar[], int start, int end, int middle) {
        int sizeL = middle - start + 1, sizeR = end - middle;
        int[] L = new int[sizeL];
        int[] R = new int[sizeR];
        for (int i = 0; i < sizeL; ++i)
            L[i] = ar[start + i];
        for (int j = 0; j < sizeR; ++j)
            R[j] = ar[middle + j + 1];

        int i = 0, j = 0;

        // Initial index of merged subarry array
        int k = start;
        while (i < sizeL && j < sizeR) {
            if (L[i] < R[j]) ar[k++] = L[i++];
            else ar[k++] = R[j++];
        }

        while (i < sizeL) ar[k++] = L[i++];

        while (j < sizeR) ar[k++] = R[j++];


    }

    public static void main(String[] args) throws IOException {
        MergeSort ob = new MergeSort();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int arr[] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        ob.divide(arr, 0, arr.length - 1);
        for (int ar : arr) {
            System.out.print(ar + " ");
        }
    }
}
