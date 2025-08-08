using EDA.Core.Interfaces;
using EDA.Core.Node;
using System;
namespace EDA.Core.MyList;

public class MyList<T> : IMyList<T>
{
    private Node<T>? _head;
    private int _size;

    public MyList()
    {
        _head = null;
        _size = 0;
    }
    public int Size => _size;
    public bool isEmpty() => _head == null;
    public void Add(T item)
    {
        Node<T> newNode = new Node<T>(item);

        if (_head == null)
        {
            _head = newNode;
        }
        else
        {
            Node<T> current = _head;
            while (current.Next != null)
            {
                current = current.Next;
            }
            current.Next = newNode;
        }
        _size++;
    }

    public void Delete(T item)
    {
        if (_head == null)
            return;

        if (_head.Value != null && _head.Value.Equals(item))
        {
            _head = _head.Next;
            _size--;
            return;
        }

        Node<T> current = _head;
        while (current.Next != null && current.Next.Value != null && !current.Next.Value.Equals(item))
        {
            current = current.Next;
        }

        if (current.Next != null)
        {
            current.Next = current.Next.Next;
            _size--;
        }
    }

    public T? Search(T item)
    {
        Node<T>? current = _head;

        while (current != null)
        {
            if (current.Value != null && current.Value.Equals(item))
            {
                return current.Value;
            }
            current = current.Next;
        }

        return default;
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