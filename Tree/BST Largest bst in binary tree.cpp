You can solve it by making NodeValue datasturcture as normal vector<int> . See codelibrary by yogesh video. 
// tc:o(n) sco(n) 

class NodeValue {
public:
    int maxNode, minNode, maxSize;
    
    NodeValue(int minNode, int maxNode, int maxSize) {
        this->maxNode = maxNode;
        this->minNode = minNode;
        this->maxSize = maxSize;
    }
};

class Solution {
private:
    NodeValue largestBSTSubtreeHelper(TreeNode* root) {
        // An empty tree is a BST of size 0.
        if (!root) {
            return NodeValue(INT_MAX, INT_MIN, 0);
        }
        
        auto left = largestBSTSubtreeHelper(root->left);
        auto right = largestBSTSubtreeHelper(root->right);
        
        if (left.maxNode < root->val && root->val < right.minNode) {            //🟩 If Current node is greater than max in left AND smaller than min in right, it is a BST.
            return NodeValue( min(root->val, left.minNode), max(root->val, right.maxNode), left.maxSize + right.maxSize + 1);
        }
        
        return NodeValue(INT_MIN, INT_MAX, max(left.maxSize, right.maxSize));   // Otherwise, return [-inf, inf] so that parent can't be valid BST
    }

    public:
    int largestBSTSubtree(TreeNode* root) {
        return largestBSTSubtreeHelper(root).maxSize;
    }
};
