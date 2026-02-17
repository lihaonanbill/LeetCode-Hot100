from typing import List, Optional

class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        # children[i] 对应字符 chr(ord('a') + i)
        self.children: List[Optional["TrieNode"]] = [None] * 26
        self.is_end: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        # word 的最后一个字符对应的节点：标记为单词结束
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        # 必须是某个单词的结尾才算存在
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        # 只要前缀路径存在即可
        return True

"""
Docstring for AdvancedDataStructureAndGraph.GraphTheory.Trie

算法思路
    insert(word)：从根开始，按字符往下走；没有子节点就创建；最后把终点标记 is_end = True
    search(word)：同样往下走；如果中途断了返回 False；走完后必须 is_end == True 才算“完整单词存在”
    startsWith(prefix)：往下走；只要能走完整个前缀就返回 True（不要求 is_end）

    
1. List[...]
    表示这是一个列表类型
    来自 typing 模块（Python 3.9+ 也可以直接用内置 list）
    表明 children 是一个列表
2. Optional["TrieNode"]
    Optional[X] 表示：这个值要么是 X 类型，要么是 None
    这里 X 是 "TrieNode"，所以意思是：
    可以是 TrieNode 对象
    也可以是 None
3. "TrieNode" 带引号
    这是前向引用（Forward Reference） 的写法
    因为在定义类的时候，TrieNode 这个类名还没完全定义好
    用引号括起来表示："这里指的是当前正在定义的 TrieNode 类"

"""