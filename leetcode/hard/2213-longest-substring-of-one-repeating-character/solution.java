class SegmentTree {
    static class Node {
        char leftChar, rightChar;
        int leftLen, rightLen, best;
    }
    private Node[] tree;
    private String s;
    private int n;

    public SegmentTree(String s) {
        this.s = s;
        this.n = s.length();
        tree = new Node[4 * n];
        for (int i = 0; i < tree.length; i++) tree[i] = new Node();
        build(1, 0, n - 1);
    }

    private void pull(int node, int l, int r) {
        int mid = (l + r) / 2;
        int left = node * 2, right = node * 2 + 1;
        tree[node].leftChar = tree[left].leftChar;
        tree[node].rightChar = tree[right].rightChar;

        tree[node].leftLen = tree[left].leftLen;
        if (tree[left].leftLen == (mid - l + 1) && tree[left].leftChar == tree[right].leftChar)
            tree[node].leftLen += tree[right].leftLen;

        tree[node].rightLen = tree[right].rightLen;
        if (tree[right].rightLen == (r - mid) && tree[right].rightChar == tree[left].rightChar)
            tree[node].rightLen += tree[left].rightLen;

        tree[node].best = Math.max(tree[left].best, tree[right].best);
        if (tree[left].rightChar == tree[right].leftChar) {
            tree[node].best = Math.max(tree[node].best, tree[left].rightLen + tree[right].leftLen);
        }
    }

    private void build(int node, int l, int r) {
        if (l == r) {
            char ch = s.charAt(l);
            tree[node].leftChar = tree[node].rightChar = ch;
            tree[node].leftLen = tree[node].rightLen = tree[node].best = 1;
            return;
        }
        int mid = (l + r) / 2;
        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);
        pull(node, l, r);
    }

    public void update(int pos, char ch) {
        update(1, 0, n - 1, pos, ch);
    }

    private void update(int node, int l, int r, int pos, char ch) {
        if (l == r) {
            tree[node].leftChar = tree[node].rightChar = ch;
            tree[node].leftLen = tree[node].rightLen = tree[node].best = 1;
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid) update(node * 2, l, mid, pos, ch);
        else update(node * 2 + 1, mid + 1, r, pos, ch);
        pull(node, l, r);
    }

    public int getBest() {
        return tree[1].best;
    }
}

class Solution {
    public int[] longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        SegmentTree st = new SegmentTree(s);
        int k = queryIndices.length;
        int[] ans = new int[k];
        for (int i = 0; i < k; i++) {
            st.update(queryIndices[i], queryCharacters.charAt(i));
            ans[i] = st.getBest();
        }
        return ans;
    }
}