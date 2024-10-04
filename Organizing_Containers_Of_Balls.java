import java.util.List;
import java.util.Map;
import java.util.HashMap;

class Result {

    /*
     * Complete the 'organizingContainers' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts 2D_INTEGER_ARRAY container as parameter.
     */

    public static String organizingContainers(List<List<Integer>> container) {
    // Write your code here
        Map<Integer, Integer> hmap = new HashMap<>();
        
        int n = container.size();
        
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                count += container.get(i).get(j);
            }
            hmap.put(count, hmap.getOrDefault(count, 0) + 1);
            count = 0;
        }
        
        count = 0; boolean flag = true;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                count += container.get(j).get(i);
            }
            if (!hmap.containsKey(count) || hmap.get(count) == 0) {
                flag = false;
                break;
            }
            hmap.put(count, hmap.get(count) - 1);
            count = 0;
        }
        
        return flag == true ? "Possible" : "Impossible";
    }

}
