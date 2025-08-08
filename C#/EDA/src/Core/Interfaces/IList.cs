
using System.Dynamic;
namespace EDA.Core.Interfaces
{
    public interface IMyList<T>
    {
        void Add(T item);
        void Delete(T item);
        T? Search(T item);
        int Size { get; }
        bool isEmpty();
        void Print();
    }
}