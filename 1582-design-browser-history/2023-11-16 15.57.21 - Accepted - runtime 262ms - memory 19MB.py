class ListNode:
    def __init__(self, val = "", next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.head.next = ListNode(url)
        prev = self.head
        self.head = self.head.next
        self.head.prev = prev

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.head.prev:
            self.head = self.head.prev
            i += 1
        
        return self.head.val

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.head.next:
            self.head = self.head.next
            i += 1
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)