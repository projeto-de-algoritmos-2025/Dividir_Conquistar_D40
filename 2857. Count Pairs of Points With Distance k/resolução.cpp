class Solution {
public:
    int countPairs(vector<vector<int>>& c, int k) {
        // Mapa para contar quantos pares (x, y) já foram processados
        map<pair<int,int>,int> mp;
        int n = c.size();
        int ans = 0;

        // Laço sobre cada ponto (i)
        for(int i = 0; i < n; i++){
            for(int val = 0; val <= k; val++){
                int x = val ^ c[i][0];
                int y = (k - val) ^ c[i][1];
                // Soma ao resultado o número de vezes que esse par (x, y) já apareceu
                ans += mp[make_pair(x, y)];
            }
            // Adiciona o ponto atual ao mapa para futuras comparações
            mp[make_pair(c[i][0], c[i][1])]++;
        }
        return ans;
    }
};
