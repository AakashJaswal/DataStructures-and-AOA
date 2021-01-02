package Trees.HandsOn;

import java.io.*;
import java.util.*;

public class testsort {
    public static void swap(int arr[], int low,int high){
        int temp = arr[low];
        arr[low] = arr[high];
        arr[high] = temp;
    }
    public static int partition(int arr[], int low, int high){
        int pivot = arr[low];
        int l = low, h=high;
        while(l<h){
            while(arr[l]<=pivot && l<h) l++;
            while(arr[h]>pivot ) h--;
            if(l<h)
                swap(arr, l, h);
        }
        swap(arr,low,h);
        return h;
    }

    public static void quickSort(int arr[], int low, int high){
        int pivot;
        if(low>=high)
            return;
        pivot = partition(arr, low,high);
        quickSort(arr, low,pivot);
        quickSort(arr, pivot+1,high);

    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = Arrays.stream(br.readLine().strip().split(" ")).mapToInt(Integer::parseInt).toArray();
        quickSort(arr,0,arr.length-1);
        for(int ar : arr){
            System.out.print(ar+" ");
        }

    }

}
