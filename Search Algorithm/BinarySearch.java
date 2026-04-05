import java.util.Scanner;
public class BinarySearch{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int size = s.nextInt();
        int arr[] = new int[size];
        
        System.out.println("Enter the values of array: ");
        for(int i=0;i<size;i++){
            arr[i] = s.nextInt();

        }

        System.out.println("Enter the Target value: ");
        int Target = s.nextInt();

        System.out.println(Search(arr,Target));

    }

    static int Search(int arr[], int target){
        int index = -1;
        int l=0,r=arr.length -1;

        while(l<=r){
            int mid = (r+l)/2;
            System.out.println("Mid: "+mid);
            System.out.println("val: "+arr[mid]);
            if(arr[mid] == target){
                return mid;
            }
            else if(arr[mid]>target){
                r = mid -1;
            }
            else{
                l = mid+1;
            }
        }
        return index;
    }
}