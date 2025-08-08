using EDA.Core.Interfaces;
using EDA.Core.Node;
using System;
namespace EDA.Core.MyQueue;

public class MyQueue<T> : IMyQueue<T>
{
    private Node<T>? _head;
    private Node<T>? _tail;
    private int _size;

    public MyQueue()
    {
        _head = null;
        _tail = null;
        _size = 0;
    }
    public int Size => _size;

    public void Enqueue(T item)
    {
        _size++;
        Node<T> newNode = new Node<T>(item);
        if (_head == null)
        {
            _head = newNode;
            _tail = newNode;

        }
        else
        {
            if (_tail == null)
            {
                throw new Exception("Tail nulo");
            }
            _tail.Next = newNode;
            _tail = newNode;
        }


    }
    public bool isEmpty() => _head == null;
    public Node<T>? Dequeue()
    {
        if (_head == null)
        {
            throw new Exception("Cola vacia");
        }
        Node<T> current = _head;
        _head = _head.Next;
        _size--;
        if (_head == null)
        {
            _tail = null;
        }
        return current;

    }
    public Node<T>? Peak()
    {
        return _head;
    }
    public void Print()
    {
        Node<T>? current = _head;
        while (current != null)
        {
            Console.Write(current.Value);
            if (current.Next != null)
            {
                Console.Write(" -> ");

            }
            current = current.Next;
        }

        Console.WriteLine();
    }
}
