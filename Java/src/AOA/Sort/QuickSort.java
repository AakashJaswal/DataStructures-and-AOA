package AOA.Sort;

import java.io.*;
import java.util.Arrays;

public class QuickSort {
    static void swap(int arr[], int a, int b) {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }

    static int partition(int[] arr, int low, int high) {
        int pivot = arr[low];
        int temp;
        int l = low, h = high;
        while (l < h) {
            while (arr[l] <= pivot && l < h) l++;
            while (arr[h] > pivot) h--;
            if (l < h) {
                swap(arr, l, h);
            }
        }
        swap(arr, low, h);
        return h;
    }

    static void sort(int[] arr, int low, int high){
        if (low >= high)
            return;
        int piv = partition(arr, low, high);
        sort(arr,low, piv);
        sort(arr,piv+1,high);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        sort(arr, 0, arr.length - 1);
        for (int ar : arr) System.out.print(ar + " ");
    }

}