import java.util.*;

class Solution {
    public int[][] highFive(int[][] items) {
        HashMap<Integer, ArrayList> scores = new HashMap<>();
        // iterate through the list of tuples
        HashSet<Integer> ids = new HashSet<>();
        for (int i = 0; i < items.length; i++) {
            // Save the scores of each student in a scores map, where id is the key, scores are a maxHeap
            int[] item = items[i];
            scores.putIfAbsent(item[0], new ArrayList<>());
            scores.get(item[0]).add(item[1]);
            ids.add(item[0]);
        }

        ArrayList<Integer> sortedIds = new ArrayList<>(ids);
        int[][] res = new int[ids.size()][2];
        int i = 0;
        for(Integer id: sortedIds){
            // for each student in scores.keySet().sort(), get top 5 values from scores, compute the avg,
            ArrayList<Integer> curStudentScores = scores.get(id);
            Collections.sort(curStudentScores, Collections.reverseOrder());
            Integer sum = 0;
            Integer avg = 0;
            // add avg along with id to a res array
            for (int j=0; j< 5; j++){
                sum = sum + curStudentScores.get(j);
            }
            avg = sum / 5;
    
            res[i][0] = id;
            res[i][1] = avg;
            i ++;
        }
        return res;
    }
}