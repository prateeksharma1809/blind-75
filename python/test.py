from collections import deque, defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Initialize graph and in-degree
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        all_chars = set()

        # Add all characters to the set
        for word in words:
            for char in word:
                all_chars.add(char)

        # Build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_length = min(len(w1), len(w2))
            found_diff = False
            for j in range(min_length):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    found_diff = True
                    break
            if not found_diff and len(w1) > len(w2):
                return ""

        # Topological sort using Kahn's Algorithm (BFS)
        q = deque([c for c in all_chars if in_degree[c] == 0])
        result = []
        
        while q:
            char = q.popleft()
            result.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        # Check if the topological sort is valid
        if len(result) != len(all_chars):
            return ""
        
        return "".join(result)