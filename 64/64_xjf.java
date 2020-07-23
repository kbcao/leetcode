class Solution {
    public int minPathSum(int[][] grid) {
        for (int j = 1; j < grid[0].length; ++j) grid[0][j] += grid[0][j - 1];
        for (int i = 1; i < grid.length; ++i) {
            for (int j = 0; j < grid[0].length; ++j) {
                grid[i][j] += Math.min(i > 0 ? grid[i - 1][j] : 0x7fffffff, j > 0 ? grid[i][j - 1] : 0x7fffffff);
            }
        }
        return grid[grid.length - 1][grid[0].length - 1];
    }
}