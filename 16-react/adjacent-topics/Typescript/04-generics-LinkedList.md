# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  Example Linked List with typing enforced by use of generic


Codealong template:
```typescript
type ListNode<T> = LLNode<T> | null;

export class LLNode<T> {
  constructor(
    private _data: T,
    public next: ListNode<T> = null) { }

  get data(): T {
    return this._data
  }

  set data(payload) {
    this._data = payload
  }
}

export class LinkedList<T> {
  constructor(
    private head: ListNode<T> = null,
    private tail: ListNode<T> = null,
    public length: number = 0) { }

  add(data: T): void {
    let node = new LLNode<T>(data)
    if (this.head === null) {
      this.head = node
    } else {
      let current = this.tail
      current.next = node
    }
    this.tail = node
    this.length++
  }

  insert(index: number, data: T): void {
    if (index >= this.length) {
      this.add(data)
    } else {
      let node = new LLNode<T>(data)
      let current = this.head
      if (index === 0) {
        node.next = current
        this.head = node
      } else {
        let currentIndex = 0;
        while (currentIndex < index - 1) {
          current = current.next
          currentIndex++
        }
        node.next = current.next
        current.next = node
      }
      this.length++
    }
  }

  delete<T>(deleteIndex: number): T {
    if (this.length > 0 && deleteIndex <= this.length - 1) {
      let result
      if (deleteIndex === 0) {
        result = this.head.data
        this.length--
        if (this.head.next) {
          this.head = this.head.next
          return result
        } else {
          this.head = null
          this.tail = null
          return result
        }
      } else {
        let currentIndex = 0
        let current = this.head
        let previous
        while (currentIndex < deleteIndex) {
          previous = current
          current = current.next
          currentIndex++
        }
        result = current.data
        if (deleteIndex === this.length - 1) {
          this.tail = previous
        }
        previous.next = current.next
        this.length--
        return result
      }
    } else {
      return null
    }
  }

  print(): void {
    if (this.head !== null) {
      let arr: any[] = []
      let current = this.head
      while (current.next !== null) {
        arr.push(current.data)
        current = current.next
      }
      arr.push(current.data)
      console.log(arr)
    } else {
      console.log('empty list')
    }
  }
}

```
## Stack and Queue from Linked List
```typescript
export class Storable<T> {
  constructor(
    protected store: LinkedList<T> = new LinkedList<T>()
  ) { }

  print(): void {
    this.store.print()
  }

  get length(): number {
    return this.store.length
  }
}

export class Stack<T> extends Storable<T> {
  push(data: T): void {
    this.store.add(data)
  }

  pop(): T {
    return this.store.delete(this.store.length - 1)
  }
}

export class Queue<T> extends Storable<T>{
  enqueue(data: T): void {
    this.store.add(data)
  }

  dequeue(): T {
    return this.store.delete(0)
  }
}
```

## Putting them to work
```typescript

const s = new Stack<number>() // s, is implicitly typed as a Stack that only accepts numbers

s.push(3) // ok!
s.push(0xf00d) // weird, but ok!
s.push('Hello, world') // TSError: Argument of type '"Hello, world"' is not assignable to parameter of type 'number'.


```
