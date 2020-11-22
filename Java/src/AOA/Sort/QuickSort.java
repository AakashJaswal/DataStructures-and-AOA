package AOA.Sort;

public class QuickSort {
    int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        System.out.println(i);
        // Put the elements smaller than pivot on the left and
        // greater than pivot on the right of pivot
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;
        return (i + 1);
    }

    void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivot = partition(arr, low, high);
            quickSort(arr, low, pivot-1);
            quickSort(arr, pivot + 1, high);
        }
    }

    public static void main(String[] args) {
        QuickSort qs = new QuickSort();
        int[] ar = {10, 4, 2, 6, 3};
        qs.quickSort(ar, 0, ar.length - 1);
        for (int a : ar) {
            System.out.print(a + " ");
        }

    }

}