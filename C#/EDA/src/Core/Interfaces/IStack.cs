using EDA.Core.Interfaces;
using EDA.Core.Node;
namespace EDA.Core.MyStack
{
    public interface IMyStack<T>
    {
        void Add(T item);
        bool isEmpty();
        Node<T>? pop();
        int Size { get; }
        void Print();

    }
}