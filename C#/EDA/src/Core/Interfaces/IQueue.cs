
using System.Dynamic;
using EDA.Core.Node;
namespace EDA.Core.Interfaces

{
    public interface IMyQueue<T>
    {
        void Enqueue(T itme);
        Node<T>? Dequeue();
        Node<T>? Peak();
        int Size { get; }
        void Print();
        bool isEmpty();
    }
}