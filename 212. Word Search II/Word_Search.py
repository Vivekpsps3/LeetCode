class Solution(object):
    def findWords(board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """


if __name__ == '__main__':
    board =[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    test = Solution.findWords(board, words)
    print(test)