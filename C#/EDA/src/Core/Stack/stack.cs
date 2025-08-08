using EDA.Core.Interfaces;
using EDA.Core.Node;
using System;
namespace EDA.Core.MyStack;

public class MyStack<T> : IMyStack<T>
{
    private Node<T>? _tail;
    private int _size;
    public int Size => _size;
    public bool isEmpty() => _tail == null;
    public void Add(T item)
    {
        Node<T> newNode = new Node<T>(item);
        if (_tail == null)
        {
            _tail = newNode;

        }
        else
        {
            newNode.Back = _tail;
            _tail = newNode;
        }
        _size++;
    }
    public Node<T> pop()
    {
        if (_tail == null)
        {
            throw new Exception("Pila vacia");

        }
        Node<T> aux = _tail;
        _tail = _tail.Back;
        _size--;
        return aux;
    }
    public void Print()
    {
        Node<T>? current = _tail;
        Console.Write("[");
        while (current != null)
        {
            Console.Write(current.Value);
            if (current.Back != null)
            {
                Console.Write(",");

            }
            current = current.Back;
        }
        Console.Write("]");
        Console.WriteLine();
    }
}