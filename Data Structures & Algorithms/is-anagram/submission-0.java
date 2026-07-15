class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        sArray = bubbleSort(sArray);
        tArray = bubbleSort(tArray);
        
        
        for (int i = 0; i < sArray.length; i++) {
            if (sArray[i] != tArray[i]) {
                return false;
            } 

            if (sArray.length != tArray.length) {
                return false;
            }
        }

        return true;
    }

    public char[] bubbleSort(char[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - 1 - i; j++) {
                if (arr[j] > arr[j+1]) {
                    char temp = arr[j];
                    arr[j] = arr[j+ 1];
                    arr[j+1] = temp;
                }
            }
        }
        return arr;
    }
}
