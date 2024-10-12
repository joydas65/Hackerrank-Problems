class Result {

    /*
     * Complete the 'surfaceArea' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY A as parameter.
     */

    public static int surfaceArea(List<List<Integer>> A) {
    // Write your code here
        int h = A.size();
        int w = A.get(0).size();
        
        int area = 2*h*w;
        
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (j == 0) area += A.get(i).get(j);
                if (j == w-1) area += A.get(i).get(j);
                if (j > 0 && j < w) area += Math.abs(A.get(i).get(j) - A.get(i).get(j-1));
                
                if (i == 0) area += A.get(i).get(j);
                if (i == h-1) area += A.get(i).get(j);
                if (i > 0 && i < h) area += Math.abs(A.get(i).get(j) - A.get(i-1).get(j));
            }
        }
        
        return area;
    }

}
