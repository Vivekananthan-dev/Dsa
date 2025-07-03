public class ArrayManipulate{
    public static void main(String[] args){
        int[] arr = {1,3,4,6};
        System.out.println(arr);
        // Access individual value
        System.out.println(arr[0]);
        System.out.println(arr[1]);

        // accessing every single element in the array
        System.out.println("Using for loop");
        for(int i=0;i<arr.length;i++){ 
            System.out.println(arr[i]);
        }

        //For loop like for each loop
        System.out.println("Using for each loop");
        for(int i : arr)
        System.out.println(i);
    }

}